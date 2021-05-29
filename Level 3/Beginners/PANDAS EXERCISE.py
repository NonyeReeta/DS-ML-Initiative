import pandas as pd
automobile_data = pd.read_csv("Automobile_data.csv")

"""Question 1: Printing first 5 rows and last 5 rows"""
print(automobile_data.head())
print(automobile_data.tail())

"""Question 2: Clean data and update csv file."""
print(automobile_data.replace(["?", "n.a"], "NaN"))


"""Question 3; Find and print the most expensive car company name and price"""
expensive = automobile_data.loc[automobile_data.price == automobile_data.price.max(), ["company", "price"]]
print(expensive)

"""Question 4: Print all Toyota car details"""
toyota_details = automobile_data.loc[automobile_data.company == "toyota"]
print(toyota_details)

"""Question 5: Count cars per company"""
print(automobile_data.groupby("company")["company"].count())


"""Question 6: Find each company's highest priced car"""
print(automobile_data[["company", "price"]].groupby("company").max())

"""Question 7: Find the average mileage of each car making company"""
print(automobile_data[["company", "average-mileage"]].groupby("company").mean())

"""Question 8: sort all cars by Price column"""
print(automobile_data.sort_values(by="price"))

"""Question 9: Concatenate two dataframes and create a key for each dataframe"""
german_cars = {
    "Company": ["Ford", "Mercedes", "BMW", "Audi"],
    "Price": [23845, 171995, 135925, 71400]
}
japanese_cars = {
    "Company": ["Toyota", "Honda", "Nissan", "Mitsubishi"],
    "Price": [29995, 23600, 61500, 58900]
}
df1 = pd.DataFrame(german_cars)
df2 = pd.DataFrame(japanese_cars)
frames = [df1, df2]
print(pd.concat(frames, keys=["German Cars", "Japanese Cars"]))

"""Question 10: Merge two dataframes and append the second dataframe as a new column to the first dataframe"""

car_price = {
    "Company": ["Toyota", "Honda", "BMW", "Audi"],
    "Price": [23845, 17995, 135925, 71400]
}
car_horsepower = {
    "Company": ["Toyota", "Honda", "BMW", "Audi"],
    "horsepower": [141, 80, 182, 160]
}
df_1 = pd.DataFrame(car_price)
df_2 = pd.DataFrame(car_horsepower)
merged_df = pd.merge(df_1, df_2)
print(merged_df)
