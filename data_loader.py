import pandas as pd

file_name = "data/Evolution_DataSets.csv"

pd = raw_data.read_csv(file_name)

print(raw_data.head(10))

#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd

# In[ ]:

evl=pd.read_csv('data/Evolution_DataSets.csv')
evl

# In[ ]:

evl.info()

# In[ ]:

evl.dtypes

# In[ ]:

evl.Location=evl['Location'].astype('category')

# In[ ]:

evl.dtypes

# In[ ]:

evl.describe()

# In[ ]:

evl.Migrated=evl['Migrated'].astype('object')

# In[ ]:

evl.dtypes

# In[ ]:

fields=['Cranial_Capacity','Height']

# In[ ]:

evl[fields].corr

# In[ ]:

pip install parquet

# In[ ]:

pip install pyarrow

# In[ ]:

pip install fastparquet

# In[ ]:

evl.to_parquet('data/Evolution_DataSets.parquet')