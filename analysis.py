def monthly_sales_analysis(df):
    return df.groupby('Month')['Sales'].sum()

def city_sales_analysis(df):
    return df.groupby('City')['Sales'].sum()

def product_sales_analysis(df):
    return df.groupby('Product').agg({'Quantity Ordered': 'sum', 'Sales': 'sum'})

def hourly_sales_analysis(df):
    return df.groupby('Hour')['Sales'].sum()
