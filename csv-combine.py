#!/usr/bin/python3

import pandas as pd

drop_fields = ["Access IPAddress","Latitude","Home Latitude","Longitude","Home Longitude","Result"]

# Reading CSVs
file1 = pd.read_csv('CSVs/datalog.csv')
file2 = pd.read_csv('CSVs/dept_resources.csv')
file3 = pd.read_csv('CSVs/employee_details.csv')

# Merge function using "inner" join
output1 = pd.merge(file1, file2, on="ResourceID",how="inner")
output2 = pd.merge(output1, file3, on="EmployeeID",how="inner")

# Specifying new dataset.
df = pd.DataFrame(output2)
# Renaming Fields
df.rename(columns = {"Department_x":"Accessed Department","Department_y":"Belonging Department"},inplace=True)
# Dropping Fields
df_update = df.drop(drop_fields,axis=1)
# Converting and saving as csv
convert_csv_data = df_update.to_csv('datalog-emp-task2.csv', header=True, index=False)
print('Conversion was successful.')

# https://stackoverflow.com/questions/17978133/python-pandas-merge-only-certain-columns
# https://www.geeksforgeeks.org/how-to-merge-two-csv-files-by-specific-column-using-pandas-in-python/
# https://www.w3schools.com/sql/sql_join.asp
# https://www.geeksforgeeks.org/how-to-export-pandas-dataframe-to-a-csv-file/
# https://stackoverflow.com/questions/52396477/printing-a-pandas-dataframe-without-row-number-index
# https://pythonexamples.org/pandas-dataframe-delete-column/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html