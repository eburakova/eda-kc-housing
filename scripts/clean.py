import pandas as pd
import numpy as np

CURRENT_YEAR = 2015
SQFT2M = 10.764

df = pd.read_csv('data/houses.csv', parse_dates=['sale_date'], date_format='%d/%m/%Y')
df['yr_renovated'].fillna(0, inplace=True) 
df['yr_renovated'] = (df.yr_renovated / 10).astype(int)
df['yr_renovated'].replace(0, np.nan, inplace=True) # this is the only way that works!

df['waterfront'] = df.waterfront.fillna(0).astype('int0') # converting to the approprite type as well
df[(df.sqft_living - df.sqft_above != df.sqft_basement)].sqft_basement.unique() 
df.eval('sqft_basement = sqft_living - sqft_above', inplace=True)

# Adding a column that is easier to analyse
df.eval('basement_share = sqft_basement / sqft_living', inplace=True)
cols = df.columns

cols_area = [c for c in cols if 'sqft' in c]
cols_area_new = [c.replace('sqft', 'm2') for c in cols_area]

df[cols_area] = df[cols_area] / SQFT2M

df.rename(columns={old: new for old, new in zip(cols_area, cols_area_new)}, inplace=True)

df = df.assign(age = CURRENT_YEAR - df.yr_built,
          yrs_since_renovation = CURRENT_YEAR - df.yr_renovated,
          p_per_m2 = np.round(df.price / df.m2_living, 1) # digits beyond the decimal are not relevant
          )

df.drop(15856, inplace=True)

df = df[df.price < 1.12e6]
df.to_csv('data/houses_processed.csv', index=False)