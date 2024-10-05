import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Product': ['Damascus Knife', 'Axe', 'Sword', 'Bow', 'Pens'],
    'Region': ['US', 'Canada', 'Switzerland', 'Saudi Arabia', 'Singapore'],
    'Sales': [12000, 8500, 15000, 10000, 500],  
    'Units Sold': [100, 80, 120, 90, 200],      
    'Customer Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Product Category': ['Cutlery', 'Tools', 'Weapons', 'Weapons', 'Stationery'],
    'Product Price': [120, 85, 150, 100, 5],    
    'Discount': [10, 5, 15, 0, 1],    
    'Sales Channel': ['Online', 'In-Store', 'Online', 'In-Store', 'Third-Party'],
    'Rating': [4.8, 4.5, 4.9, 4.2, 4.0],
    'Return Status': ['No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("Updated Dataset:\n", df)
plt.figure(figsize=(8, 5))
sns.barplot(x='Product', y='Sales', data=df, palette='muted')
plt.title('Sales per Product')
plt.xlabel('Product')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.show()

sales_by_region = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(7, 7))
plt.pie(sales_by_region, labels=sales_by_region.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales Distribution by Region')
plt.axis('equal')  
plt.show()


plt.figure(figsize=(8, 5))
sns.stripplot(x='Product', y='Units Sold', data=df, size=10, color='blue', jitter=False)
plt.title('Units Sold per Product')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

sales_sum = df['Sales'].sum()
units_sold_sum = df['Units Sold'].sum()

print(f"\nSummary of Findings:")
print(f"Total Sales: ${sales_sum}")
print(f"Total Units Sold: {units_sold_sum}")
print(f"Highest Sales from Product: {df.iloc[df['Sales'].idxmax()]['Product']}")
print(f"Region with Maximum Sales: {sales_by_region.idxmax()}")

average_rating = df.groupby('Product')['Rating'].mean()
print("\nAverage Rating per Product:")
print(average_rating)

return_rate = df.groupby('Product')['Return Status'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nReturn Rate per Product (%):")
print(return_rate)