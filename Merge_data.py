import pandas as pd
import sqlite3

orders = pd.read_csv("orders.csv")

print(orders.head())

users = pd.read_json("users.json")
print(users.head())

conn = sqlite3.connect(":memory:")

with open("restaurants.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)
print(restaurants.head())

merged_data = pd.merge(
    orders,
    users,
    on="user_id",
    how="left"
)

# Step 5: Merge with restaurants (Left Join)
merged_data = pd.merge(
    merged_data,
    restaurants,
    on="restaurant_id",
    how="left"
)
print(merged_data.head())

merged_data.to_csv("final_food_delivery_dataset.csv", index=False)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter only Gold members
gold_df = df[df["membership"] == "Gold"]

# Calculate total revenue city-wise
city_revenue = (
    gold_df
    .groupby("city")["total_amount"]
    .sum()
    .reset_index()
)

# Find city with highest revenue
highest_city = city_revenue.loc[city_revenue["total_amount"].idxmax()]

print("City with highest Gold member revenue:")
print(highest_city)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter Gold members
gold_orders = df[df["membership"] == "Gold"]

# Count total orders
total_gold_orders = gold_orders.shape[0]

print("Total orders placed by Gold members:", total_gold_orders)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter orders from Hyderabad city
hyd_df = df[df["city"] == "Hyderabad"]

# Calculate total revenue
total_revenue = hyd_df["total_amount"].sum()

# Round to nearest integer
total_revenue_rounded = round(total_revenue)

print("Total revenue from Hyderabad:", total_revenue_rounded)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Count distinct users who placed at least one order
distinct_users = df["user_id"].nunique()

print("Number of distinct users who placed at least one order:", distinct_users)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter Gold members
gold_df = df[df["membership"] == "Gold"]

# Calculate average order value
avg_order_value = gold_df["total_amount"].mean()

# Round to 2 decimals
avg_order_value_rounded = round(avg_order_value, 2)

print("Average order value for Gold members:", avg_order_value_rounded)

import pandas as pd

# Load final merged dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter orders for restaurants with rating >= 4.5
high_rated_orders = df[df["rating"] >= 4.5]

# Count number of orders
total_orders = high_rated_orders.shape[0]

print("Orders placed for restaurants with rating ≥ 4.5:", total_orders)

import pandas as pd

# Load final dataset
df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter Gold members only
gold_df = df[df["membership"] == "Gold"]

# Find top revenue city among Gold members
city_revenue = gold_df.groupby("city")["total_amount"].sum()
top_city = city_revenue.idxmax()

# Count orders in that top revenue city
orders_in_top_city = gold_df[gold_df["city"] == top_city].shape[0]

print("Top revenue city (Gold members):", top_city)
print("Number of orders in that city:", orders_in_top_city)

