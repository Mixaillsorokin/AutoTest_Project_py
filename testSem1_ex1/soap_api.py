from zeep import Client, Settings
import yaml

with open("config.yaml", encoding="utf=8") as f:
    data = yaml.safe_load(f)
    wsdl = data["wsdl"]

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)

def checkText(text) -> list[str]:
    response = client.service.checkText(text)
    return response[0]["s"]