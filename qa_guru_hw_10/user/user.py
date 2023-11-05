import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobby: str
    photo: str
    address_street: str
    address_house: str
    address_flat: str
    state: str
    city: str
