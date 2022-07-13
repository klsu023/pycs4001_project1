import pandas as pd
import matplotlib.pyplot as plt

# data source: https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data
# loading data
df = pd.read_csv('Top YouTube Channels Data.csv')
# print out first 5 samples from the data
pd.set_option('display.max_columns', 7)
print(df.head(5))
# We don't need rank
df = df.drop(columns=['rank'])
# We want to know views per subscriber
df['video views'] = df['video views'].str.replace(',','').astype(int)
df['views per subscriber'] = df['video views'] / df['subscribers']
print(df.head(5))

# some statistical properties
print(df.describe())
# see some more information e.g. data type
print(df.info())

# number of subscribers
plt.hist(df['subscribers'], bins=10)
plt.title('Subscribers')
plt.xlabel("number of subscribers")
plt.ylabel("number of channels")
plt.show()

# total number of each category
category_count = df['category'].value_counts()
print(category_count)
pie_chart = df['category'].value_counts().plot.pie(autopct = '%1.1f%%', fontsize = 8)
plt.show()

# correlation matrix
corr = df.corr()
print(corr)
plt.imshow(corr,cmap='seismic')
plt.title('Correlation Matrix')
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);
plt.colorbar()
plt.show()

# Number of Top Youtube Channels Started Each Year
print(df['started'].value_counts().sort_index(ascending=True))
line_plot = df['started'].value_counts().sort_index(ascending=True).plot()
plt.title('Number of Top Youtube Channels Started Each Year')
plt.xlabel('year')
plt.ylabel('number of channels')
plt.show()