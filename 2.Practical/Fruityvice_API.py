import requests
import json
import pandas as pd
# Get the data from the API

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
print(df2)

cal_banana = df2.loc[df2["name"] == 'Banana']
cal_banana.iloc[0]['nutritions.calories']