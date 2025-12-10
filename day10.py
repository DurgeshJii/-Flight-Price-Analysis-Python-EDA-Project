# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('airlines_flights_data.csv')
print(data)

# ------------------ CLEANING ------------------

# Remove index column
data.drop(columns='index', inplace=True)
print(data)

# Dataset information
data.info()

# Statistical summary
print(data.describe())

# ------------------ EXPLORATORY ANALYSIS ------------------

# Q1: Airlines and their frequencies
print(data['airline'].nunique())
print(data['airline'].unique())
print(data['airline'].value_counts())

data['airline'].value_counts(ascending=True).plot.barh()
plt.title("Airlines with Frequencies")
plt.xlabel("Number of Flights")
plt.ylabel("Airlines")
plt.show()

# Q2: Departure and Arrival time analysis
print(data['departure_time'].value_counts())
print(data['arrival_time'].value_counts())

plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.bar(data['departure_time'].value_counts().index,
        data['departure_time'].value_counts().values)
plt.title("Departure Time")

plt.subplot(1, 2, 2)
plt.bar(data['arrival_time'].value_counts().index,
        data['arrival_time'].value_counts().values)
plt.title("Arrival Time")
plt.show()

# Q3: Source & Destination cities
print(data['source_city'].value_counts())
print(data['destination_city'].value_counts())

plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
plt.barh(data['source_city'].value_counts().index,
         data['source_city'].value_counts().values)
plt.title("Source Cities")

plt.subplot(1, 2, 2)
plt.barh(data['destination_city'].value_counts().index,
         data['destination_city'].value_counts().values)
plt.title("Destination Cities")
plt.show()

# Q4: Price variation with airlines
print(data.groupby('airline')['price'].mean())
sns.catplot(x='airline', y='price', kind='bar',
            hue='class', data=data)
plt.show()

# Q5: Price change by departure and arrival time
print(data.groupby('departure_time')['price'].mean())
print(data.groupby('arrival_time')['price'].mean())

sns.catplot(x='departure_time', y='price', kind='bar', data=data)
plt.show()

sns.relplot(x='arrival_time', y='price',
            col='departure_time', kind='line', data=data)
plt.show()

# Q6: Price change by source & destination city
print(data.groupby('source_city')['price'].mean())
print(data.groupby('destination_city')['price'].mean())

sns.relplot(x='destination_city', y='price', col='source_city',
            kind='line', data=data)
plt.show()

# Q7: Ticket price vs days_left
print(data['days_left'].unique())
print(data.groupby('days_left')['price'].mean())

sns.relplot(x='days_left', y='price', kind='line', data=data)
plt.show()

# Q8: Economy vs Business class pricing
economy = data[data['class'] == 'Economy']
business = data[data['class'] == 'Business']

print(economy['price'].mean())
print(business['price'].mean())

# Q9: Avg price – Vistara, Delhi → Hyderabad, Business class
new_data = data[(data['airline'] == 'Vistara') &
                (data['source_city'] == 'Delhi') &
                (data['destination_city'] == 'Hyderabad') &
                (data['class'] == 'Business')]

print(new_data['price'].mean())
