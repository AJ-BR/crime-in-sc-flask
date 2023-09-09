import json
import os.path

import pytest

from src.app import home, app


@pytest.fixture
def app_context():
    with app.app_context():
        yield


def test_files_exist():
    assert os.path.isfile('src/resources/agency_data.csv') is True
    assert os.path.isfile('src/resources/ori_crime_year_data.csv') is True


def test_home(app_context):
    json_response = home()
    assert json_response.status_code == 200
    assert json_response.json == {}


def test_goose_creek_robbery_2021():
    with app.test_client() as c:

        response = c.get('fbi/?location=goose-creek&year=2021&crime=robbery')
        assert response is not None
        assert response.status_code == 200

        keys = {'crime', 'location', 'year', 'total'}
        response_dict = json.loads(response.text)
        assert response_dict is not None
        assert keys == response_dict.keys()
        assert keys == response_dict.keys()

        total = response_dict['total']
        assert total == '8'



