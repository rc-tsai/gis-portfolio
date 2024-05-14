import pandas as pd
import os

# read in data
df = pd.read_csv('ZIPCodetoZCTACrosswalk2022UDS.csv')
tanf = pd.read_csv('New_all_states.csv')

# filter data on Georgia
df = df[df['STATE'] == 'GA']
tanf = tanf[(tanf['STATE'] == 'GA') & (tanf['year'] == '2021')]

# check data types
df.dtypes
tanf.dtypes

# change data type
tanf['ZIP'] = tanf['ZIP'].astype('Int64')

# rename columns
tanf.rename(columns={'ZIP':'zip', 'recipients':'rec', 'blk_recipients':'blk_rec'}, inplace = True)

# The data exported from the Administrative Data Research Facility (ADRF) suppresses values that are less than 10, representing them as '<10' in the dataset. Additionally, the maximum value is expressed as 'MAX' in the data
# To address these issues, I replace the '<10' value with 0 and the 'MAX' value with the maximum value in the dataset plus 1

# address the issues for total TANF recipients column
# create a list then remove non-integer value to find the maximum value
ls = tanf['rec'].tolist()
ls = list(set(ls))
ls.remove('MAX')
ls.remove('<10')
integer_list = [int(x) for x in ls]
integer_list.sort()

# print the maximum value
print(integer_list[-1] + 1)

# replace the value in data: '<10' --> 0 ;  'MAX' --> maximum value in the dataset plus 1
tanf['rec'] = tanf['rec'].replace('<10', 0); tanf['rec'] = tanf['rec'].replace('MAX', integer_list[-1] + 1); tanf

# address the issues for black TANF recipients column
ls1 = tanf['blk_rec'].tolist()
ls1 = list(set(ls1))
ls1.remove('MAX')
ls1.remove('<10')
integer_list1 = [int(x) for x in ls1]
integer_list1.sort()
print(integer_list1[-1] + 1)
tanf['blk_rec'] = tanf['blk_rec'].replace('<10', 0); tanf['blk_rec'] = tanf['blk_rec'].replace('MAX', integer_list1[-1] + 1); tanf

# change data type
tanf['rec'] = tanf['rec'].astype('int64')
tanf['blk_rec'] = tanf['blk_rec'].astype('int64')
tanf.dtypes

# merge TANF with crosswalk reference
master_zip = tanf[['zip', 'rec', 'blk_rec']].merge(df[['ZIP_CODE', 'zcta']], left_on='zip', right_on='ZIP_CODE',how='outer')
master_zip['rec'] = master_zip['rec'].astype('Int64')
master_zip['blk_rec'] = master_zip['blk_rec'].astype('Int64')
master_zip['zcta'] = master_zip['zcta'].astype('Int64')
master_zip.dtypes
print(master_zip.dtypes)

# remove Null 'zip'
master_zip = master_zip[master_zip['zip'].notnull()]
master_zip

# get the total recipients and black recipients by zcta level
newdf = master_zip.groupby(['zcta'])[['rec', 'blk_rec']].sum()
newdf = newdf.reset_index()

# get the percent of black recipients
newdf['blk_pct'] = newdf['blk_rec'] / newdf['rec']

# export data
newdf.to_csv('TANF_GA21_zcta.csv', index = False)
