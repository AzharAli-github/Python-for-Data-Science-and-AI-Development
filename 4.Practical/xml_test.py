import requests
import pandas as pd

# File URL
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

# Download file synchronously
response = requests.get(filename)
if response.status_code == 200:
    with open("file_example_XLSX_10.xlsx", "wb") as f:
        f.write(response.content)

# Read Excel file
df = pd.read_excel("file_example_XLSX_10.xlsx")
print(df)
