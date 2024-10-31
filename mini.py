import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# The brief
# “Should we stop making MegaBytes Vouchers?”

# MegaBytes’ CEO is wondering if the MegaBytes gift vouchers are worth producing. 
# She doesn’t think enough people use them and thinks they should be phased out. 
# The store’s manager thinks enough people use them to keep them in place.

# Using the data provided produce a number of visualisations, which will help inform this decision.
# Examples include:
# • How many sales were made on each payment type?
# • How many unique items were paid for by each payment type?
# • What percentage of income made came from vouchers?

# 3 graphs or more afterwords
# todo list
# label on slide who did what

# Desk 3
# Hammad
# Hassan
# Laura

products = {
    'Tea' : 1.00,
    'Americano' : 1.70,
    'Latte' : 1.90,
    'Cappuccino' : 1.90,
    'Mocha' : 2.00,
    'Hot Chocolate' : 2.20,
    'Croissant' : 1.50,
    'Muffin' : 2.10,
    'Toast' : 1.00,
    'Panini' : 2.90,
    'Buttered Roll' : 0.70,
    'Stroopwafel': 0.50,
    }


df1 = pd.read_excel("monday_voucher_data.xlsx")
df2 = pd.read_excel("tuesday_voucher_data.xlsx")
df3 = pd.read_excel("wednesday_voucher_data.xlsx")
df4 = pd.read_excel("thursday_voucher_data.xlsx")
df5 = pd.read_excel("friday_voucher_data.xlsx")
df6 = pd.read_excel("saturday_voucher_data.xlsx")
df7 = pd.read_excel("sunday_voucher_data.xlsx")

df1['Days'] = 'Monday' 
df2['Days'] = 'Tuesday'
df3['Days'] = 'Wednesday' 
df4['Days'] = 'Thursday'
df5['Days'] = 'Friday' 
df6['Days'] = 'Saturday'
df7['Days'] = 'Sunday' 

df = pd.concat([df1,df2,df3,df4,df5,df6,df7], ignore_index=True)

df = df.set_index("Transaction ID")
df = df.drop(columns=["Staff","Transaction Type","Basket"])
df = df.dropna(how="any" )

df['Payment Method'] = df['Payment Method'].replace('cash', 'Cash')
df['Payment Method'] = df['Payment Method'].replace('debit', 'Debit')
                                                

# def split_basket(basket_item):
#     items = basket_item.split(",")
#     stripped_items = [item.strip() for item in items]

#     return stripped_items

# df["Basket"] = df["Basket"].apply(split_basket)
# exploded_data = df.explode("Basket", ignore_index=False)

# print(df)

# print(df.describe())

# print(df.info())


# print(df.value_counts('Payment Method'))

plt.pie(df['Payment Method'], labels=df['Payment Method'], autopct='%1.1f%%'explode=[0.2,0.2,0.1,0.1])
plt.show( )



