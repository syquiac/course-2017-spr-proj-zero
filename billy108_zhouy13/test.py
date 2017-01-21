import json
import sodapy

client = sodapy.Socrata("data.cityofboston.gov", None)
response = client.get("awu8-dc52", limit=10)
print(json.dumps(response, sort_keys=True, indent=2))