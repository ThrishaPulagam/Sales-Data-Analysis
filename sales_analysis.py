import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

print("\nMissing Values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

df["Month"] = df["Sale_Date"].dt.month_name()

print("\nDataset Info:")
print(df.info())

total_sales = df["Sales_Amount"].sum()

print("\nTotal Sales:", total_sales)

top_categories = (
    df.groupby("Product_Category")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Product Categories:")
print(top_categories)

region_sales = (
    df.groupby("Region")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRegion-wise Sales:")
print(region_sales)

monthly_sales = (
    df.groupby("Month")["Sales_Amount"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)

# Visualization 
# Monthly Sales Chart

plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/monthly_sales.png")

plt.show()

print("Monthly Sales Chart Saved Successfully!")

# Product Category Sales Chart

plt.figure(figsize=(8,5))

top_categories.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Amount")

plt.tight_layout()

plt.savefig("visualizations/product_category_sales.png")

plt.close()

print("Product Category Chart Saved!")

# Region-wise Sales Chart

plt.figure(figsize=(8,5))

region_sales.plot(kind="bar")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales Amount")

plt.tight_layout()

plt.savefig("visualizations/region_sales.png")

plt.close()

print("Region Sales Chart Saved!")