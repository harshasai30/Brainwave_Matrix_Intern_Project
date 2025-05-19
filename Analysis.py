import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Load the dataset

os.chdir("C:/Users/harsha/Braniwave_Matrix_Intern_Project/Project/")
df = pd.read_csv("sales_data.csv")  # Make sure the CSV file is in the same directory or provide the full path

# Exploratory Data Analysis (EDA)
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data type conversion (if necessary)
df['Date'] = pd.to_datetime(df['Date'])

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Visualizations

# Trends over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Quantity', data=df, hue='Product')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.show()

# Best-selling products
plt.figure(figsize=(8, 6))
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title('Best-Selling Products')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product')
plt.show()

# Revenue by store
df['Revenue'] = df['Quantity'] * df['UnitPrice']
store_revenue = df.groupby('Store')['Revenue'].sum()
plt.figure(figsize=(8, 6))
sns.barplot(x=store_revenue.index, y=store_revenue.values)
plt.title('Revenue by Store')
plt.xlabel('Store')
plt.ylabel('Total Revenue')
plt.show()

# Distribution of Unit Price
plt.figure(figsize=(8, 6))
sns.histplot(df['UnitPrice'], kde=True)
plt.title('Distribution of Unit Price')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.show()

# Insights (Example - adapt based on your analysis)
print("\nInsights:")
print("- Product X is the best-selling product overall.")
print("- Store A generates the highest revenue.")
print("- There might be a seasonal trend in sales (further investigation needed).")
print("- The unit price distribution shows that most products fall within a certain range.")

# ...add more insights as you analyze the data...
