#All the duplicate columns and NaN values were removed when I merged the data in the previous project
#Link --> https://github.com/Sravya2007/Project-129-Data-Merging
import pandas as pd

star_data = pd.read_csv("star_data.csv")
print("Columns in star data --> ", list(star_data))

try:
    del star_data["Luminosity"]
except:
    print("No Luminosity column in the merged data")

if star_data.isnull().values.any() == True:
    sum_of_NaNs = star_data.isnull().sum().sum()
    print(f"Found {sum_of_NaNs} NaN values in the dataset")
    star_data.dropna()
else:
    print("No NaN values found in the data")