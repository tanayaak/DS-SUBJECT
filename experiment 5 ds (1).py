#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wine_data = pd.read_csv(url, sep=';')

# Display the first few rows of the dataset
print(wine_data.head())


# In[4]:


import matplotlib.pyplot as plt

# Calculate the average quality for each alcohol level
average_quality = wine_data.groupby('alcohol')['quality'].mean()

# Plot the line chart
plt.plot(average_quality.index, average_quality.values, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title('Average Wine Quality by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality')
plt.grid(True)
plt.show()


# In[5]:


import seaborn as sns

# Plot a count plot for wine quality
sns.countplot(x='quality', data=wine_data, palette='viridis')
plt.title('Count of Wine Quality Ratings')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()


# In[6]:


# Plot the line chart with legend
plt.plot(average_quality.index, average_quality.values, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Average Quality')
plt.title('Average Wine Quality by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality')
plt.legend(loc='upper left')  # Add legend
plt.grid(True)
plt.show()


# In[7]:


# Find the maximum and minimum quality points
max_quality = average_quality.max()
min_quality = average_quality.min()
max_alcohol = average_quality.idxmax()
min_alcohol = average_quality.idxmin()

# Plot the line chart with live markers
plt.plot(average_quality.index, average_quality.values, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Average Quality')
plt.scatter([max_alcohol], [max_quality], color='red', marker='^', s=100, label='Max Quality')
plt.scatter([min_alcohol], [min_quality], color='green', marker='v', s=100, label='Min Quality')
plt.title('Average Wine Quality by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality')
plt.legend(loc='upper left')  # Add legend
plt.grid(True)
plt.show()


# In[ ]:




