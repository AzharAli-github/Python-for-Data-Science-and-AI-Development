import pandas as pd
import numpy as np
import ssl

# Ignore SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Fetch tables from the webpage
tables = pd.read_html("https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29")

# Select the correct table
df = tables[3]

# Reset column names to numeric indices
df.columns = range(df.shape[1])

# Extract relevant columns
df = df[[0, 2]]

# Remove the header row and select the top 10 countries
df = df.iloc[1:11, :]

# Rename columns
df.columns = ['Country', 'GDP (Million USD)']

# Convert GDP values to numeric

df['GDP (Million USD)'] = df['GDP (Million USD)'].replace(r'[\$,]', '', regex=True).astype(float)


df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert GDP from Million USD to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000

# Round to 2 decimal places
df['GDP (Million USD)'] = np.round(df['GDP (Million USD)'], 2)

# Rename column properly
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# Save the cleaned data to CSV
df.to_csv('./Largest_economies.csv', index=False)

# Print the cleaned DataFrame
print(df)
