import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Εισάγω τα δεδομένα μου
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Επιθεώρηση Δεδομένων
print(df.head())
print(df.shape)
print(df.describe())

# Χειρισμός τιμών που λείπουν
print(df.isnull().sum())
df_clean = df.fillna(0)

# Φιλτράρισμα 2016-2019
df["date"] = pd.to_datetime(df["date"])
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index()

# Διάκριση του δημοφιλέστερου είδους για κάθε τ.κ.
bottles_sold = filtered_df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
bottles_sold['zip_code'] = bottles_sold['zip_code'].astype(int)
idx = bottles_sold.groupby('zip_code')['bottles_sold'].idxmax()
max_bottles = bottles_sold.loc[idx].reset_index()
sorted_values = max_bottles.sort_values(by='bottles_sold', ascending=False).head(20)
print(sorted_values.head())

# Υπολογισμός ποσοστού πωλήσεων ανά κατάστημα(σε $)
store_sales = filtered_df.groupby('store_name')['sale_dollars'].sum().reset_index()
total_sales = store_sales['sale_dollars'].sum()
store_sales['salesPercentage'] = (store_sales['sale_dollars'] / total_sales) * 100
store_sorted_sales = store_sales.sort_values(by='sale_dollars',ascending=False)
print(store_sorted_sales.round(2).head(15))

# Δημιουργία σχεδιαγράμματος πρώτου ερωτήματος
plt.figure(figsize=(10,6))
plt.bar(sorted_values['zip_code'].astype(str), sorted_values["bottles_sold"], color="r")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.title("Max bottles sold per zip code")
plt.show()

# Δημιουργία γραφήματος για το δεύτερο ερώτημα
import plotly.express as px

fig = px.pie(store_sorted_sales.head(10),
             values='salesPercentage',
             names='store_name',
             title='Top 10 Stores by Sales Percentage (2016-2019)')
fig.show()
