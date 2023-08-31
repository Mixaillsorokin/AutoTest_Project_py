import pytest
import yaml
from conftest import *

with open("config.yaml") as f:
    data = yaml.safe_load(f)
    username, password, url = data["username"], data["password"], data["url"]


def test_some_api_functionality(token):
    print(token())