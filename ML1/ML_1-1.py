from __future__ import division, print_function, unicode_literals

# Code example
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


# Load the data
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")

print("2017250045 정태환\n")
print("oecd_bli.head(2):\n")
print(oecd_bli.head(2))
print("\n\noecd_bli['Life satisfaction'].head():\n")
print(oecd_bli["Life satisfaction"].head())

gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t',
                             encoding='latin1', na_values="n/a")
gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
gdp_per_capita.set_index("Country", inplace=True)
print("\n\ngdp_per_capita.head(2):\n")
print(gdp_per_capita.head(5))

full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
print("\n\nfull_country_stats:\n", full_country_stats)
print("\n\nUnited States' Life satisfaction:")
print(full_country_stats[["GDP per capita", 'Life satisfaction']].loc["United States"])

keep_indices = list(set(range(36)))
sample_data = full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

def prepare_country_stats(oecd_bli, gdp_per_capita):
    return sample_data

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

# Select a linear model
model = linear_model.LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus

print("\n\n# Make a prediction for Cyprus\n")
X_new = [[22587.0]] # Cyprus' GDP per capita

print(model.predict(X_new))

