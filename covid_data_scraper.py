import pandas as pd
from selenium import webdriver

# URL of the webpage
url = 'https://www.worldometers.info/coronavirus/#countries'

# Initialize a browser instance
driver = webdriver.Chrome()  # You'll need to download and set up the Chrome driver

# Load the URL
driver.get(url)

# Get the page source (including JavaScript-rendered content)
page_source = driver.page_source

# Close the browser instance
driver.quit()

# Now, let's parse the page_source using Pandas
dfs = pd.read_html(page_source)

# Assuming the desired table is the first one in the list of DataFrames
df = dfs[0]
df = df.drop(['#'], axis=1)
df.columns = ['Country', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious/Critical', 'Total Cases/1M pop', 'Deaths/1M pop', 'Total Tests', 'Tests/1M pop', 'Population', 'Continent']

# Specify the path to save the CSV file
csv_path = 'data.csv'
df.to_csv(csv_path, index=False)
print("Data has been saved to:", csv_path)



    