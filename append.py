import pandas as pd
import numpy as np
import os

# Read the data from the Excel files
df1 = pd.read_excel('~/Downloads/excel.xlsx')
df2 = pd.read_excel('~/Downloads/generated_question.xlsx')

# Remove the first row from the second DataFrame
df1 = df1.iloc[1:]

df_empty = pd.DataFrame(np.nan, index=[0], columns=df1.columns)

# Append the empty DataFrame to the first one
df1 = df1.append(df_empty, ignore_index=True)

# Append the second DataFrame to the first one
df2 = df2.append(df1, ignore_index=True)


# Write the result back to 'first.xlsx'
df2.to_excel('~/Downloads/generated_question.xlsx', index=False)
