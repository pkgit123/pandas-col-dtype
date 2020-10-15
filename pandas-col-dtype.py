import pandas as pd
import numpy as np

# create sample dataframe
df = pd.DataFrame({
    'num1': [1, 2, 3],
    'num2': [4.0, 5.0, 6.0],
    'str1': ['blah', 'abc', 'now']
})

print(df.head())
print()

# create list of columns with numeric data type
col_numeric = df.select_dtypes(include=[np.number]).columns

# create list of columns with str data type
col_str = df.select_dtypes(include=object).columns

print('Numeric columns: ', col_numeric)
print('String columns: ', col_str)

# fill nulls by column type
df_clean = df.copy()
_ = [df_clean[each_col].fillna(0, inplace=True) for each_col in col_numeric]
_ = [df_clean[each_col].fillna("", inplace=True) for each_col in col_str]

print("Fill nulls operation completed.", "\n")

# convert str to UPPER-CASE
for each_col in col_str:
    df_clean[each_col] = df_clean[each_col].str.upper()
    
print("Modify str to UPPER-CASE complete.", "\n")
