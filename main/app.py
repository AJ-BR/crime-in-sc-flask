import psycopg2
from flask import Flask, make_response, request

from constants import COUNTIES, YEARS, CRIMES
from config import db_config

# import logging

app = Flask(__name__)

# logging.basicConfig(filename="application.log",
#                     filemode='w',
#                     format="%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S")


@app.route("/", methods=['GET'])
def home():
    resp = make_response({}, 200)
    return resp


@app.route("/sled/", methods=['GET'])
def calculate_crime_count():
    connection = None

    if len(request.args) == 0:
        response = create_error_response("URL incorrectly constructed. Format should be /sled/?county={county}&year={"
                                         "year}&crime={crime}", 400)
    else:
        county = request.args.get("county")
        year = request.args.get("year")
        crime = request.args.get("crime")

        response = {}
        if not county or county.lower() not in COUNTIES:
            response = create_error_response(f"{county} is not a valid county. Valid counties are{COUNTIES}", 400)
        elif not year or int(year) not in YEARS:
            response = create_error_response(f"{year} is not a valid year. Valid years are {YEARS}", 400)
        elif not crime or crime.lower() not in CRIMES.keys():
            response = create_error_response(f"{crime} is not a valid crime. Valid crimes are {list(CRIMES.keys())}", 400)

        else:
            try:
                dbparams = db_config()
                connection = psycopg2.connect(**dbparams)

                crime = CRIMES[crime]

                # Create cursor
                cursor = connection.cursor()

                query = """
                        select * from sled_county_crime_table 
                        where lower(county)=lower('{county}') and year={year} and lower(crime)=lower('{crime}');
                        """.format(county=county, year=year, crime=crime)

                cursor.execute(query)
                connection.commit()

                result = cursor.fetchall()
                if result and result[0]:
                    response = create_data_response(result[0])

            except(Exception, psycopg2.DatabaseError) as error:
                print(error)
                response = create_error_response("Failed to connect to the database. No data is available", 404)
            finally:
                if connection is not None:
                    connection.close()
                    print('Database connection terminated.')
    return response


def create_error_response(message: str, status_code: int):
    resp = make_response({"message": message}, status_code)
    return resp


def create_data_response(data: tuple):
    resp = {}
    if len(data) != 4:
        resp = create_error_response(f"Data from database is incomplete or corrupted: {data}", 500)
    else:
        try:
            response_dict = {
                "county": str(data[0]).lower(),
                "crime": str(data[1]).lower(),
                "year": data[2],
                "count": data[3]
            }
        except Exception as error:
            print(error)
        resp = make_response(response_dict, 200)
    return resp
