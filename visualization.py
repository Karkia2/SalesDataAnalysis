import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_sales(monthly_sales):
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Total Sales Per Month')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.show()

def plot_city_sales(city_sales):
    city_sales.plot(kind='bar', color='green')
    plt.title('Total Sales by City')
    plt.xlabel('City')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()

def plot_product_sales(product_sales):
    sns.barplot(x=product_sales.index, y='Sales', data=product_sales)
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.show()

def plot_hourly_sales(hourly_sales):
    hourly_sales.plot(kind='line', marker='o')
    plt.title('Sales by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.show()
