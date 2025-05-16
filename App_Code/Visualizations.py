
# For donations type 


# Create a styled bar chart for total donations by type
plt.figure(figsize=(12, 6))
bar_plot = sns.barplot(data=donations_summary, x='Donation_Type', y='Quantity_kg', estimator=sum, ci=None, palette='pastel')
bar_plot.set_title('Total Donations by Type', fontsize=24, fontweight='bold', color='#222222')
bar_plot.set_xlabel('Donation Type', fontsize=18, color='#333333', labelpad=10)
bar_plot.set_ylabel('Total Quantity (kg)', fontsize=18, color='#333333', labelpad=10)
plt.xticks(rotation=45)

# Adding value annotations on top of the bars
for p in bar_plot.patches:
    bar_plot.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='bottom', fontsize=12, color='#333333')

plt.tight_layout()
plt.show()  # Display the enhanced bar chart

# Create a styled pie chart for the distribution of donations by type
plt.figure(figsize=(8, 8))
pie_data = donations_summary.groupby('Donation_Type')['Quantity_kg'].sum()
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribution of Donations by Type', fontsize=24, fontweight='bold', color='#222222')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()  # Display the enhanced pie chart




# For Location based insights

# Importing necessary libraries for data analysis and visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Loading the dataset
file_path = 'delivery_data_with_coordinates.csv'
delivery_data = pd.read_csv(file_path)

# Displaying the head of the dataframe to understand its structure
print(delivery_data.head())
print(delivery_data.columns)


# Checking for any missing values in the dataset
missing_values = delivery_data.isnull().sum()
print(missing_values)


# Since there are no missing values in the dataset, we can proceed to generate heatmaps and maps.

# Setting up the figure for heatmap
plt.figure(figsize=(10, 8))

# Creating a heatmap of delivery times by city
heatmap_data = delivery_data.pivot_table(values='Delivery_Time_Minutes', index='City', aggfunc='mean')
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='.1f')
plt.title('Average Delivery Time (Minutes) by City', fontsize=20)
plt.xlabel('City', fontsize=16)
plt.ylabel('Average Delivery Time (Minutes)', fontsize=16)
plt.show()


# a map to visualize the delivery locations based on their coordinates.

# Creating a GeoDataFrame from the delivery data
geometry = gpd.points_from_xy(delivery_data['Longitude'], delivery_data['Latitude'])
delivery_gdf = gpd.GeoDataFrame(delivery_data, geometry=geometry)

# Setting up the map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plotting the delivery locations on the map
plt.figure(figsize=(12, 10))
ax = world.plot(color='lightgrey', edgecolor='black')

# Plotting the delivery points
delivery_gdf.plot(ax=ax, color='blue', markersize=10, alpha=0.5)
plt.title('Delivery Locations', fontsize=20)
plt.xlabel('Longitude', fontsize=16)
plt.ylabel('Latitude', fontsize=16)
plt.show()



# Delivery Time BoxPlot 

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
file_path = 'delivery_data.csv'
delivery_data = pd.read_csv(file_path)

# Displaying the first few rows of the dataset to understand its structure
print(delivery_data.head())
print(delivery_data.describe())


# Setting the style for the plots
sns.set(style='whitegrid')

# Creating a histogram of delivery times
plt.figure(figsize=(10, 6))
plt.hist(delivery_data['Delivery_Time_Minutes'], bins=20, color='#766CDB', edgecolor='black')
plt.title('Distribution of Delivery Times', fontsize=20, fontweight='semibold', color='#222222', pad=15)
plt.xlabel('Delivery Time (Minutes)', fontsize=16, color='#333333', labelpad=10)
plt.ylabel('Frequency', fontsize=16, color='#333333', labelpad=10)
plt.xticks(fontsize=14, color='#555555')
plt.yticks(fontsize=14, color='#555555')
plt.grid(axis='y', color='#E0E0E0')
plt.show()

# Creating a line plot for delivery times over time
# First, converting the Timestamp to datetime
delivery_data['Timestamp'] = pd.to_datetime(delivery_data['Timestamp'])

# Sorting the data by Timestamp
delivery_data = delivery_data.sort_values('Timestamp')

plt.figure(figsize=(10, 6))
sns.lineplot(x='Timestamp', y='Delivery_Time_Minutes', data=delivery_data, color='#DA847C', marker='o')
plt.title('Delivery Times Over Time', fontsize=20, fontweight='semibold', color='#222222', pad=15)
plt.xlabel('Date', fontsize=16, color='#333333', labelpad=10)
plt.ylabel('Delivery Time (Minutes)', fontsize=16, color='#333333', labelpad=10)
plt.xticks(rotation=45, fontsize=14, color='#555555')
plt.yticks(fontsize=14, color='#555555')
plt.grid(color='#E0E0E0')
plt.show() 


