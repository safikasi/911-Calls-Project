import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('911.csv')

# Basic info
print(df.info())
print(df.head())

# Top ZIP codes
print("Top 5 ZIP codes:\n", df['zip'].value_counts().head(5))

# Top townships
print("Top 5 Townships:\n", df['twp'].value_counts().head(5))

# Unique title codes
print("Number of unique titles:", df['title'].nunique())

# Extract reason from title
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
print("Reason value counts:\n", df['Reason'].value_counts())

# Countplot of Reason
plt.figure(figsize=(8, 5))
sns.countplot(x='Reason', data=df, palette='viridis')
plt.title('911 Calls by Reason')
plt.xlabel('Reason')
plt.ylabel('Number of Calls')
plt.tight_layout()
plt.show()

# Convert timeStamp to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Extract Hour, Month, and Day of Week
df['Hour'] = df['timeStamp'].apply(lambda t: t.hour)
df['Month'] = df['timeStamp'].apply(lambda t: t.month)
df['Day Of Week'] = df['timeStamp'].apply(lambda t: t.dayofweek)

# Map day numbers to names
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day Of Week'].map(dmap)

# Countplot of calls by Day of Week
plt.figure(figsize=(10, 6))
sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.title('Calls by Day of Week and Reason')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Countplot by Month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=df, hue='Reason', palette='Set2')
plt.title('Calls by Month and Reason')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Group by month and plot call count trend
byMonth = df.groupby('Month').count()
byMonth['lat'].plot(figsize=(10, 5), marker='o')
plt.title('911 Calls Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.grid(True)
plt.tight_layout()
plt.show()

# Linear regression plot of Month vs Number of Calls
sns.lmplot(x='Month', y='lat', data=byMonth.reset_index())
plt.title('Linear Trend of Calls by Month')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.tight_layout()
plt.show()

# Create Date column
df['Date'] = df['timeStamp'].apply(lambda t: t.date())

# Plot calls per day
df.groupby('Date').count()['lat'].plot(figsize=(12, 5))
plt.title('911 Calls Per Day')
plt.xlabel('Date')
plt.ylabel('Number of Calls')
plt.tight_layout()
plt.grid(True)
plt.show()

# Plot calls per EMS,FIRE OF TRAFFIC
df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot(figsize=(12, 5))
plt.title('911 Calls of Traffic')
plt.tight_layout()
plt.grid(True)
plt.show()
df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot(figsize=(12, 5))
plt.title('911 Calls of EMS')
plt.tight_layout()
plt.grid(True)
plt.show()
df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot(figsize=(12, 5))
plt.title('911 Calls of Fire')
plt.tight_layout()
plt.grid(True)
plt.show()
# Heatmap: Day of Week vs Hour
day_hour = df.pivot_table(index='Day of Week', columns='Hour', values='Reason', aggfunc='count')
plt.figure(figsize=(12, 6))
sns.heatmap(day_hour, cmap='YlGnBu')
plt.title('911 Calls Heatmap (Day of Week vs Hour)')
plt.tight_layout()
plt.show()

#Cluster Map: Day Of Week vs Hour
day_hour = df.pivot_table(index='Day of Week', columns='Hour', values='Reason', aggfunc='count')
plt.figure(figsize=(12, 6))
sns.clustermap(day_hour, cmap='viridis')
plt.title('911 Calls Clustermap (Day of Week vs Hour)')
plt.tight_layout()
plt.show()

#dataset of Day of week vs Month

day_Month = df.pivot_table(index='Day of Week', columns='Month', values='Reason', aggfunc='count')
plt.figure(figsize=(12, 6))
sns.clustermap(day_Month, cmap='coolwarm')
plt.title('911 Calls Clustermap (Day of Week vs Month)')
plt.tight_layout()
plt.show()