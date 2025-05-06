import pandas as pd
from pandasql import sqldf
# This imported the pandas library and the pandas MySQL library

pysqldf = lambda q: sqldf(q, globals())
# This creates a function and a shortcut so i can query the data cleaner and not have to include other things from the pandas library constantly

df = pd.read_csv("C:\\Users\\Gerar\\Downloads\\inventory(1).csv")
# This loades the df -> "DataFrame" so that you can use the csv file in the future

print(df.head())
# simple print line to see the first 5 rows of the database inside of the dataframe. 

query1 = """
SELECT
    *
FROM
    df
WHERE
    StoreName = "Family Dollar"
"""

result1 = pysqldf(query1)
print(result1)

query2 = """
SELECT
    *
FROM
    df
GROUP BY
    StoreName
"""

result2 = pysqldf(query2)
print(result2)