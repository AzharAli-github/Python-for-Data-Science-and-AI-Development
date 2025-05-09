import pandas as pd
import requests

# Download CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
response = requests.get(url)

# Save file locally
with open("addresses.csv", "wb") as f:
    f.write(response.content)

# Load CSV into Pandas DataFrame
df = pd.read_csv("addresses.csv", header=None)
# print(df.head())

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)