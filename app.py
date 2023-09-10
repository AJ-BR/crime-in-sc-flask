from flask import Flask, make_response, request

from constants import YEARS, CRIMES, LOCATIONS, COUNTIES
import pandas as pd

app = Flask(__name__)

with app.app_context():
    agency_data_df = pd.read_csv('resources/agency_data.csv')
    crime_data_df = pd.read_csv('resources/ori_crime_year_data.csv')


def run():
    app.run(debug=False)


# Landing point of the url
@app.route("/", methods=['GET'])
def home():
    return make_response({}, 200)


# The format of this url is fbi/?location={location}&year={year}&crime={crime}
@app.route("/fbi/", methods=['GET'])
def calculate_crime_count():

    _response = {}
    if len(request.args) == 0:
        _response = create_error_response("URL incorrectly constructed. Format should be /fbi/?"
                                          "location={location}"
                                          "&isCounty={iscounty}"
                                          "&year={year}"
                                          "&crime={crime}",
                                          400)
    else:
        is_county = request.args.get('iscounty')
        location = request.args.get('location')
        _year = request.args.get('year')
        crime = request.args.get('crime')

        if not location or (location.lower() not in LOCATIONS and location.lower() not in COUNTIES):
            return create_error_response(f"{location} is not a valid location. Valid locations are {LOCATIONS} "
                                         f"Valid counties are {COUNTIES}", 400)
        elif (is_county and not isinstance(is_county, str)) or (
                is_county and is_county.lower() not in ('true', 'false')):
            return create_error_response(f"iscounty value should be true/false. Instead received {is_county}.", 400)
        elif is_county and is_county.lower() == 'true' and location.lower() not in COUNTIES:
            return create_error_response(f"iscounty was set to {is_county} but location was not a county. Valid "
                                         f"counties are {COUNTIES}", 400)
        elif not _year or int(_year) not in YEARS:
            return create_error_response(f"{_year} is not a valid year. Valid years are {YEARS}", 400)
        elif not crime or crime.lower() not in CRIMES.keys():
            return create_error_response(f"{crime} is not a valid crime. Valid crimes are {list(CRIMES.keys())}", 400)

        else:
            if not agency_data_df.empty and not crime_data_df.empty:
                _oris = []
                if is_county == 'true':
                    _oris = agency_data_df[agency_data_df['county'] == location]['ori'].tolist()
                else:
                    _oris = agency_data_df[agency_data_df['location'] == location]['ori'].tolist()

                if _oris:
                    _year = int(_year)
                    filtered_df = crime_data_df[
                        (crime_data_df['ori'].isin(_oris))
                        & (crime_data_df['year'] == _year)
                    ]
                    _total = 0
                    if crime == 'all':
                        _total = filtered_df['total'].sum()
                    else:
                        _total = filtered_df[filtered_df['crime_name'] == crime]['total'].sum()

                    response_dict = {'location': location, 'crime': crime, 'year': _year, 'total': str(_total)}
                    _response = make_response(response_dict, 200)
    return _response


# Create error message notifying that something was wrong with the url construction or something on the backend
def create_error_response(message: str, status_code: int):
    resp = make_response({"message": message}, status_code)
    return resp


# Data extraction was successful and ready to be put into a JSON response
def create_data_response(data: tuple):
    resp = {}
    if len(data) != 4:
        resp = create_error_response(f"Data from database is incomplete or corrupted: {data}", 500)
    else:
        try:
            resp = {
                "county": str(data[0]).lower(),
                "crime": str(data[1]).lower(),
                "year": data[2],
                "count": data[3]
            }
        except Exception as error:
            print(error)
    return resp
