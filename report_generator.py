import pandas as pd

def save_to_excel(monthly_sales, city_sales, product_sales, hourly_sales, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        monthly_sales.to_excel(writer, sheet_name='Monthly Sales')
        city_sales.to_excel(writer, sheet_name='Sales by City')
        product_sales.to_excel(writer, sheet_name='Product Sales')
        hourly_sales.to_excel(writer, sheet_name='Hourly Sales')

