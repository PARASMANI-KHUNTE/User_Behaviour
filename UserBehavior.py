import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
filename = "user_behavior_dataset.csv"
df = pd.read_csv(filename)

# Preview the data
print(df.head())


# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Basic statistics of numerical columns
print("Statistical Summary:\n", df.describe())

# Data types
print("Data Types:\n", df.dtypes)





plt.figure(figsize=(10, 6))
sns.histplot(df['App Usage Time (min/day)'], kde=True, color='skyblue')
plt.title('Distribution of App Usage Time')
plt.xlabel('App Usage Time (min/day)')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Screen On Time (hours/day)', y='Battery Drain (mAh/day)', hue='Operating System')
plt.title('Screen On Time vs. Battery Drain')
plt.xlabel('Screen On Time (hours/day)')
plt.ylabel('Battery Drain (mAh/day)')
plt.legend(title='Operating System')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='App Usage Time (min/day)', palette='pastel')
plt.title('App Usage Time by Gender')
plt.xlabel('Gender')
plt.ylabel('App Usage Time (min/day)')
plt.show()


plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='User Behavior Class', palette='viridis')
plt.title('User Behavior Class Distribution')
plt.xlabel('User Behavior Class')
plt.ylabel('Count')
plt.show()

