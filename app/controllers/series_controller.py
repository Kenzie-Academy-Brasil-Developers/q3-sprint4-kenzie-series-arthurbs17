from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from app.services.database_service import KEYNAMES
from psycopg2.errors import UniqueViolation

def get_all_series():
    series = Series.read_all_series()

    series_list = [dict(zip(KEYNAMES, serie)) for serie in series]

    return jsonify(series_list), HTTPStatus.OK

def add_new_serie():
    data = request.get_json()

    serie = Series(**data)

    try:
        added_serie = serie.to_add_serie()
    except UniqueViolation:
        return (jsonify({"error": "Falha na requisição!"}), HTTPStatus.UNPROCESSABLE_ENTITY)
    
    new_serie = dict(zip(KEYNAMES, added_serie))

    return jsonify(new_serie), HTTPStatus.CREATED