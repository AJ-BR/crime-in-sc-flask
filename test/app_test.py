import psycopg2

from main.config import db_config


def test_db_connection():
    connection_passed = False
    connection = None
    try:
        dbparams = db_config()
        connection = psycopg2.connect(**dbparams)

        connection_passed = True
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

    assert connection is not None
    assert connection_passed is True


def test_sled_table_exists():
    result = None
    connection = None
    try:
        dbparams = db_config()
        connection = psycopg2.connect(**dbparams)

        cursor = connection.cursor()

        query = "select * from sled_county_crime_table limit 1;"

        cursor.execute(query)
        connection.commit()

        result = cursor.fetchall()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

    assert result is not None

def test_counties_exist():
    result = None
    connection = None
    try:
        dbparams = db_config()
        connection = psycopg2.connect(**dbparams)

        cursor = connection.cursor()

        query = "select distinct county from sled_county_crime_table;"

        cursor.execute(query)
        connection.commit()

        result = cursor.fetchall()
        print(result)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 46