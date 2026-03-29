import pandas as pd
import numpy as np
data = {'Name': ['A', 'B', 'C', 'D', 'E'],'Age': [20, 21, np.nan, 23, 22],'Marks': [85, np.nan, 78, 90, 88]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Total'] = df['Marks'] + 10
df.rename(columns={'Marks': 'Score'}, inplace=True)
df.drop('Age', axis=1, inplace=True)
df.loc[1, 'Score'] = 95
print("Modified and Cleaned DataFrame:")
print(df)
