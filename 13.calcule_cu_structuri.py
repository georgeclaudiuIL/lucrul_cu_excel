import pandas as pd


data_a = pd.Series([10,20,30,40,50], name = "Values")
data_b = pd.Series([5,4,3,2,1], name = "Values")

result = data_a * data_b
print(result)

