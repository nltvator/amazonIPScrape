import json
from urllib.request import urlopen
import json
import pandas as pd

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

response = urlopen(url)

json_data = json.loads(response.read())

print(json_data)
prefix = json_data["prefixes"]

df = pd.DataFrame.from_dict(prefix)

print(df)

df.to_csv("AmazonIPs.csv")