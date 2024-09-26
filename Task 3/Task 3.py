import pandas as pd
import matplotlib.pyplot as plt

file_path = "bike_sales.csv"
df = pd.read_csv(file_path)

print("Bike Sales Dataset:\n", df.head())
print("\nStatistical Summary:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

plt.figure(figsize=(10, 6))
brand_revenue = df.groupby("Brand")["Revenue"].sum().sort_values(ascending=False)
brand_revenue.plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("Total Revenue by Bike Brand", fontsize=14)
plt.xlabel("Brand", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))
category_dist = df["Category"].value_counts()
category_dist.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=['#ffcc99','#66b3ff','#99ff99','#ff9999'])
plt.title("Bike Category Distribution", fontsize=14)
plt.ylabel("")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["Price"], df["Units Sold"], color="darkorange", edgecolors="black", alpha=0.8)
plt.title("Price vs Units Sold", fontsize=14)
plt.xlabel("Price", fontsize=12)
plt.ylabel("Units Sold", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Revenue"], marker="o", linestyle="-", color="blue", markersize=6)
plt.title("Revenue Trend Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("\nTotal Revenue by Brand:\n", brand_revenue)