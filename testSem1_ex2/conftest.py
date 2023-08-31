import pytest
import yaml
import requests


with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def token():
    res1 = requests.post(data["url"],data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def testtext1():
    return "text"


