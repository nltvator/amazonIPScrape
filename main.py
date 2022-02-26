import json
import requests
import pandas as pd

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

response = requests.get(url)

json_data = json.loads(response.text)

prefix = json_data["prefixes"]

df = pd.DataFrame.from_dict(prefix)

df.to_csv("AmazonIPs.csv")