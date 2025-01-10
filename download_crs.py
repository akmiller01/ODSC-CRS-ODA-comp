import os
from oda_reader import download_crs
import pandas as pd

# All disbursements
for year in range(2014, 2024):
    year_filename = 'large_input/crs_{}.csv'.format(year)
    if not os.path.exists(year_filename):
        crs_data = download_crs(
            start_year=year, 
            end_year=year, 
            filters={
                'flow_type': 'D', # Disbursements
                'price_base': 'V', # Current price
                'microdata': True
            }, 
            dataflow_version='1.3'
        )
        crs_data.to_csv(year_filename)

# Collate
all_filename = 'large_input/crs_2014_2023.csv'
if not os.path.exists(all_filename):
    all_dataframes = []

    for year in range(2014, 2024):
        year_filename = 'large_input/crs_{}.csv'.format(year)
        df = pd.read_csv(year_filename, encoding='utf-8')
        all_dataframes.append(df)
    concatenated_df = pd.concat(all_dataframes, ignore_index=True)
    concatenated_df.to_csv(all_filename)
else:
    concatenated_df = pd.read_csv(all_filename)

crs_aggregated = concatenated_df.groupby(['year','donor_code', 'donor_name','category_code','category_name'])['value'].sum()
crs_aggregated.to_csv('output/crs_aggregated_2014_2023.csv')
