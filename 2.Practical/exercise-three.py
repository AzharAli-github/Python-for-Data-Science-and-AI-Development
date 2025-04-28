import requests
import json
import pandas as pd
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results2 = json.loads(data2.text)
df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
print(df3)
