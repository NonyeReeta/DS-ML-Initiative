from matplotlib import pyplot as plt, style
import pandas as pd

company_sales = pd.read_csv("company_sales_data.csv")

"""Exercise 1: Read total profit of all months and show it using a line plot"""
total_sales = company_sales.total_profit
month_num = company_sales.month_number
# plt.plot(month_num, total_sales)
# plt.title("Company Profit per Month")
# plt.xlabel("MonthNumber")
# plt.ylabel("Total Profit")
# plt.show()

"""Exercise 2: Read all product sales data and show it using multi line plot"""
facecream_sales = company_sales.facecream
facewash_sales = company_sales.facewash
toothpaste_sales = company_sales.toothpaste
bathingsoap_sales = company_sales.bathingsoap
shampoo_sales = company_sales.shampoo
moisturizer_sales = company_sales.moisturizer

font_dict = {
    "family": "Times New Roman",
    "color": "black",
    "weight": "bold",
    "size": 18
}
plt.plot(month_num, facecream_sales, "o-", label="Face Cream Sales Data", linewidth=4)
plt.plot(month_num, facewash_sales, "o-", label="Face Wash Sales Data", linewidth=4)
plt.plot(month_num, toothpaste_sales, "o-", label="Toothpaste Sales Data", linewidth=4)
plt.plot(month_num, bathingsoap_sales, "o-", label="Bathing Soap Sales Data", linewidth=4)
plt.plot(month_num, shampoo_sales, "o-", label="Shampoo Sales Data", linewidth=4)
plt.plot(month_num, moisturizer_sales, "o-", label="Moisturizer Sales Data", linewidth=4)
plt.title("Sales Data", fontdict=font_dict)
plt.ylabel("Sales Unit in numbers", fontdict=font_dict)
plt.xlabel("Month Number", fontdict=font_dict)
plt.legend()
plt.show()


