""" 可运行测试
from app.schemas import CarInput
 
def test_car_text_fields_are_trimmed():
    car = CarInput(
        make="Mazda",
        model="MX-5",
        year=2020,
        color="Red",
    )
    #assert car.make == "Honda"  # deliberately wrong（故意写错）
    assert car.make == "Mazda"
    assert car.model == "MX-5"
    assert car.color == "Red"
"""
###  Write a new integration test
import pytest
from pydantic import ValidationError

from app.schemas import CarInput


def test_car_text_fields_are_trimmed():
    car = CarInput(
        make="Mazda",
        model="MX-5",
        year=2020,
        color="Red",
    )

    assert car.make == "Mazda"
    assert car.model == "MX-5"
    assert car.color == "Red"


def test_blank_model_is_rejected():
    with pytest.raises(ValidationError):
        CarInput(make="Mazda", model="", year=2020)
