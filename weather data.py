#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


data= pd.read_csv(r"D:\weather data\Prayagraj.csv")


# In[10]:


data


# In[11]:


# Re-importing libraries
data_full = {
    "datetime": [
        "2024-12-05", "2024-12-06", "2024-12-07", "2024-12-08", "2024-12-09",
        "2024-12-10", "2024-12-11", "2024-12-12", "2024-12-13", "2024-12-14",
        "2024-12-15", "2024-12-16", "2024-12-17", "2024-12-18", "2024-12-19"
    ],
    "tempmax": [27.6, 26.3, 26.3, 26.9, 27.9, 25.7, 25.2, 25.2, 25.4, 24.9, 23.5, 24.5, 25.5, 26.4, 26.3],
    "tempmin": [15.6, 14.3, 14.3, 14.3, 16.2, 13.6, 14.3, 12.5, 12.3, 11.8, 10.4, 10.7, 11.4, 12.0, 12.2],
    "temp": [20.8, 19.5, 19.7, 20.3, 21.2, 19.1, 18.8, 17.8, 17.7, 17.1, 15.9, 16.4, 17.2, 17.8, 17.9],
    "feelslikemax": [26.7, 26.3, 26.3, 26.7, 27.0, 25.7, 25.2, 25.2, 25.4, 24.9, 23.5, 24.5, 25.5, 26.4, 26.3],
    "feelslikemin": [15.6, 14.3, 14.3, 14.3, 16.2, 13.6, 14.3, 12.5, 12.3, 11.8, 10.4, 10.7, 11.4, 12.0, 12.2],
    "feelslike": [20.7, 19.5, 19.7, 20.2, 21.1, 19.1, 18.8, 17.8, 17.7, 17.1, 15.9, 16.4, 17.2, 17.8, 17.9]
}

# Create a DataFrame
df_full = pd.DataFrame(data_full)
df_full["datetime"] = pd.to_datetime(df_full["datetime"])

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df_full["datetime"], df_full["tempmax"], label="Max Temperature (°C)", color="red", marker="o")
plt.plot(df_full["datetime"], df_full["tempmin"], label="Min Temperature (°C)", color="blue", marker="o")
plt.plot(df_full["datetime"], df_full["temp"], label="Average Temperature (°C)", color="green", linestyle="--")
plt.plot(df_full["datetime"], df_full["feelslike"], label="Feels Like Temperature (°C)", color="purple", linestyle="-.")

# Graph customization
plt.title("Detailed Temperature Trends in Prayagraj (December 2024)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)

# Show plot
plt.tight_layout()
plt.show()


# In[12]:


data.head()


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data['temp'].unique()


# In[12]:


data['icon'].unique()


# In[13]:


data['description'].unique()


# In[14]:


data.nunique()


# In[15]:


data.count


# In[16]:


data.value_counts


# In[17]:


data.info()


# ## Q) 1. Find all the unique'temp value'value in the data.

# In[18]:


data.head(2)


# In[19]:


data.nunique()


# In[20]:


data['visibility'].nunique()


# In[21]:


data['visibility'].unique()


# In[22]:


data['temp'].plot()


# ## Q)2.Find the number of times when the 'Weather is exactly clear'.

# In[23]:


data.head(2)


# In[24]:


# value_count()
data.dew.value_counts()


# In[25]:


# Filtering
#data.head(2)
data[data.dew =='icon']


# In[26]:


[data.dew =='icon']


# ## Q)3.Find the number of times when the'When humidity was exactly 37.8'.

# In[ ]:


data.head(2)


# In[23]:


data['humidity'].plot()


# In[24]:


data[data['humidity'] == 37.8]#answer


# ## Q. 4) Find out all the values in the data.

# In[25]:


data.isnull().sum()                                                                


# In[26]:


data.notnull().sum()


# ## Q.5) Rename the column name 'temp'of the dataframe to'temp condition'.

# In[27]:


data.head(2)


# In[28]:


data.rename(columns ={'temp': 'temp condition'}, inplace = True)


# In[29]:


data.head()


# ## Q.6)What is the mean 'solarenergy'?

# In[30]:


data.head(2)


# In[31]:


data["solarenergy"].plot()


# In[32]:


data.solarenergy.mean()


# ## Q.7) What is the Standard Deviation of 'MOONPHASE'in this data?

# In[33]:


data.moonphase.std()


# ## What is the Varience of 'Humidity'in this data?

# In[34]:


data['humidity'].var()


# ## Q.9) Find all instances when '17.8' was recorded.

# In[35]:


#value_count()
#data.head(2)
data['temp condition'].value_counts()


# In[36]:


#filltering
data[data['temp condition'] == 17.8]


# ## Q.10)Find all instances when 'tempmax is above 23.5' and 'feelslikemax is 26.7'.

# In[37]:


data.head(2)


# In[38]:


data[(data['tempmax'] > 23.5) & (data['feelslikemax'] == 26.7)]


# ## Q.11) What is the minimum & maximum value of each column against each 'temp condition'?

# In[39]:


data.head(4)


# In[40]:


data.groupby('temp condition').min()


# In[41]:


data.groupby('temp condition').max()


# ## Q.12) Show all the records where conditions is Partially Cloudy.

# In[42]:


data[data['conditions'] =='Partially cloudy']


# ## Q.13) Find all the 'conditions is clear'or 'temp condition is above 20.8'.

# In[43]:


data[(data['conditions'] == 'Clear') | (data['temp condition'] > 20.8)]


# In[44]:


data[(data['conditions'] == 'Clear') | (data['temp condition'] > 20.8)].plot()


# ## Q.14)Find all instances when:

# #### A. 'Conditions is clear'and 'Humidity is grater then 37.8'

# ##### OR

# #### B. 'temp condition is above 20.8'

# In[45]:


data.head(2)


# In[46]:


data[(data['conditions'] == 'Clear') & (data['humidity'] > 37.8)|(data['temp condition'] > 20.8)]


# In[47]:


data[(data['conditions'] == 'Clear') & (data['humidity'] > 37.8)|(data['temp condition'] > 20.8)].plot()


# In[ ]:




