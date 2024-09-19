from data_loader import load_and_clean_data
from analysis import monthly_sales_analysis, city_sales_analysis, product_sales_analysis, hourly_sales_analysis
from visualization import plot_monthly_sales, plot_city_sales, plot_product_sales, plot_hourly_sales
from report_generator import save_to_excel

# Load and clean the data
df = load_and_clean_data('Sales Data.csv')

# Run analyses
monthly_sales = monthly_sales_analysis(df)
city_sales = city_sales_analysis(df)
product_sales = product_sales_analysis(df)
hourly_sales = hourly_sales_analysis(df)

# Visualize the results
plot_monthly_sales(monthly_sales)
plot_city_sales(city_sales)
plot_product_sales(product_sales)
plot_hourly_sales(hourly_sales)

# Save the analysis to Excel
save_to_excel(monthly_sales, city_sales, product_sales, hourly_sales, 'sales_analysis_report.xlsx')
