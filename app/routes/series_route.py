from flask import Blueprint
from app.controllers import series_controller

bp_series = Blueprint("series", __name__, url_prefix="/series")

bp_series.get("")(series_controller.get_all_series)
bp_series.get("/<int:id>")(series_controller.get_specific_serie)
bp_series.post("")(series_controller.add_new_serie)