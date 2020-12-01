import numpy as np 
import pandas as pd 

file_path = "C:\\Users\\internet\\OneDrive - Bank Of Israel" + \
"\\Data\\MacroHistory\\JSTdatasetR3.xlsx"

raw_df = pd.read_excel(file_path, sheet_name='Data')
raw_df.sort_values(['country', 'year'], ignore_index = True, inplace = True)
raw_df.to_csv("C:\\Users\\internet\\Desktop\\raw_df.csv")


# Clean df

years_to_mask = raw_df['year'].apply(lambda y: y in list(range(1914,1919)) + list(range(1934, 1946)))

clean_df = raw_df.copy()

for col in clean_df.columns:
    if col not in ['year', 'country']:
        clean_df[col][years_to_mask] = np.nan
        

clean_df.to_csv("C:\\Users\\internet\\Desktop\\clean_df.csv")