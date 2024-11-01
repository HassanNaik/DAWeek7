import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal


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

# df = df.set_index("Transaction ID")
# df = df.drop(columns=["Staff","Transaction Type","Basket","Transaction ID"])
df = df.drop(columns=["Staff","Transaction Type","Transaction ID"])
df = df.dropna(how="any" )

df['Payment Method'] = df['Payment Method'].str.capitalize()
# df['Payment Method'] = df['Payment Method'].replace('cash', 'Cash')
# df['Payment Method'] = df['Payment Method'].replace('debit', 'Debit')

df = df.drop_duplicates()                                     

def split_basket(basket_item):
    items = basket_item.split(",")
    stripped_items = [item.strip() for item in items]

    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

exploded_data = df.explode("Basket", ignore_index=False)

# print(exploded_data["Basket"] )

df.to_excel('combine.xlsx', index=False)
            
print(df)

print(exploded_data[exploded_data["Basket"] == 'Gift Voucher']['Cost'].sum())
print(exploded_data[exploded_data["Basket"] == 'Gift Voucher']['Total Items'].sum())
print(df[df['Payment Method'] == 'Voucher']['Cost'].sum())
print(df['Cost'].sum())
print(exploded_data["Basket"].value_counts())
print(exploded_data["Basket"].count())

payment_costs = df.groupby('Payment Method')['Cost'].sum()

print(payment_costs)

# plt.pie(df['Payment Method'].value_counts().values, labels=df['Payment Method'].value_counts().index, autopct="%.2f%%", explode = [0, 0, 0, 0.1, 0])
# plt.pie(df.groupby('Payment Method')['Cost'].sum(), labels=payment_costs.index, autopct=lambda p: f'£{round(p * sum(payment_costs) / 100):.2f}' if p > 0 else '')
    
# plt.title("Percentage of Vouchers used")

basket_counts = exploded_data['Basket'].value_counts()

# plt.bar(basket_counts.index, basket_counts.values)

# plt.xlabel('Basket Items') 

# plt.ylabel('Frequency') 

# plt.title('Frequency of Basket Items')

total_sales = basket_counts * basket_counts.index.map(products)
if pd.isna(total_sales['Gift Voucher']): 
    total_sales['Gift Voucher'] = exploded_data[exploded_data["Basket"] == 'Gift Voucher']['Cost'].sum()
print(total_sales.sum())

plt.bar(basket_counts.index, total_sales)
plt.xlabel('Basket Items') 

plt.ylabel('Cost in £') 

plt.title('Total Cost of Basket Items')
# plt.legend(loc="upper right",bbox_to_anchor=(1.3, 1) )

plt.show()

