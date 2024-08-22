""" utility functions are defined here """

import requests
import json
import os
from django.conf import settings


def load_data(country):
    response = requests.get("http://universities.hipolabs.com/search?country=" + country)
    data = response.json()
    return data

def main():
    get_state('Turkey')

if __name__ == "__main__":
    main()