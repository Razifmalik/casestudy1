
# coding: utf-8

# In[156]:

# I would be using the following libraries to work on the project. 
# Pandas mainly for analysis, seaborn & matplotlib for visualization purposes.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
import datetime as dt
from datetime import datetime


# In[3]:

# let us import the two csv files & create a object
data_p = pd.read_csv("exercise_providers.csv")
data_j = pd.read_csv("exercise_jobs.csv")

# Creating a dataframe using pandas DataFrame tool

df_provider = pd.DataFrame(data_p)
df_jobs = pd.DataFrame(data_j)




# In[40]:


#let us get a quick glimse of our provider data set
df_provider.head()


# In[41]:

# let us also see how our jobs data set looks like

df_jobs.head()


# In[42]:

# let us also get a whole picture of the provider data set
# We see that we have 9878 unique provider_id

df_provider.describe()


# In[43]:

# let us also get a whole picture of the job data set
# We have 6126 unique provider_id in this data set

df_jobs.describe()


# In[44]:

# let us create a new dataframe which only has the provider_id's of users who actually 
# signed up and did a job
# A inner join here on provider_id would do the trick.

df_result = pd.merge(df_jobs,df_provider,how = "inner", on = "provider_id")


# In[189]:

# let us see the details of our new data frame.

# here we have 6026 unique provider_ id which is less than our data frame data_j. 
# This is because some values are present in data_j but are not included in data_p

df_result.describe()


# In[58]:

# let us use Groupby to check which city has the maximum  unique providers active on a job

df_result.groupby("city").provider_id.nunique()

# let us create a new datafrme using groupby to see the unique provider_id's
data_c = df_result.groupby("city").provider_id.nunique()

df_city = pd.DataFrame(data_c)

df_city.head()




# In[60]:

# Let us now go back to our provider data frame to check how many providers are signing up from each city
df_provider.groupby("city").provider_id.nunique()


# In[72]:

# also would be interesting to know how many provider_id's we have overall. 
# Maybe in some city users do job multiple time, would be interesting if we find some trends.
df_result.groupby("city").count()



# In[191]:

# Now that we know how many providers sign up from each city,do the job 
# and also if these providers do a job multiple times.
# let us make a new data frame with all this info & then visualize it to answer 
# the first question of our case study


data_f = {"City":['Berlin','Cologne','Hamburg','Munich','Munster'],'Provider': ['1917','2013','1971','2032','1945'],'Provider working':  ['1180','1211','1210','1217','1208'],'Total':  ['3441','3569','3567','3582','3565']}

df_first = pd.DataFrame(data_f)



# In[192]:

# let us quickly take a look at our dataframe

df_first.head()


# In[197]:

# change the type to int so that we could plot it later using seaborn
df_first['Provider'] = df_first['Provider'].astype(int)
df_first['Provider working'] = df_first['Provider working'].astype(int)
df_first['Total'] = df_first['Total'].astype(int)

# Finally we have all the data we need to check which city has how many providers 
# & how many of them actually got a job
# let us do a factorplot on the data frame to see where we stand

sns.factorplot('Provider', 'Provider working', hue='City', data=df_first)

#  results -  Munich tops the list with 2032 sign ups & 1215 active workers 
#  & the least active city is Berlin at the moment
#  Hamburg, Munster & Cologne are also close in terms of active workers



# In[159]:

# Let us tackle the second question to check where the biggest drop is coming in provider sign ups
# Let us quickly take a look at our data set again
df_provider.head()


# In[158]:

# Let us convert our sign_up_date column to datetime

df_provider['sign_up_date'] = pd.to_datetime(df_provider['sign_up_date'])


# In[ ]:

# Let us create a new column called month which extracts the month from our sign up date

df_provider['month'] = pd.DatetimeIndex(df_provider['sign_up_date']).month


# In[199]:

# let us see our new column

df_provider.head()


# In[200]:

# Let us visualize the data to check how many providers we are getting per month per city.

sns.factorplot("month", data = df_provider, kind = 'count',hue = 'city')

# result - Feb seems to be the slowest month but also it has less days so that 
# should also be kept in mind.


# In[201]:

# Let us now find more about people who signed up but did not do a job.
# we will be using our df_first data frame for it.
# Let us check the difference between provider and provider working

df_first.head()


# In[202]:


df_first['difference'] = df_first[['Provider']].sub(df_first['Provider working'], axis=0)


# In[203]:



df_first.head()



# In[218]:

# now let us calculate the % of people who to not work but sign up.
# Let us create a new column again called percentage.
# for this let us convert provider and difference column to int first

df_first['Provider working'] = df_first['Provider working'].astype(int)
df_first['difference'] = df_first['difference'].astype(int)

df_first['percentage'] = (df_first['difference']/df_first['Provider'])*100


# In[219]:

# let us quicly take a look at our data base
df_first.head()


# In[ ]:

# results - Almost all cities have more than 37% providers
# who sign up but to not work due to different reasons.
# This is definetely a big number & a bottleneck and something 
# which if streamlined can  increase the revenues significantly.

