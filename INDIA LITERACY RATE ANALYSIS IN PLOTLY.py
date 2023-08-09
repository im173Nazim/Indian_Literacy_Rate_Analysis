#!/usr/bin/env python
# coding: utf-8

# In[1]:


#INDIA LITERACY RATE ANALYSIS IN PLOTLY


# In[17]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# plotly offline mode
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)


# In[28]:


import os
print(os.getcwd())

df_ele = pd.read_csv('2015_16_Statewise_Elementary.csv')
df_ele.shape


# In[29]:


df_sec = pd.read_csv('2015_16_Statewise_Secondary.csv')
df_sec.shape


# In[30]:


df_ele.columns


# In[31]:


df_sec.columns


# In[32]:


df_sec.head(2)


# In[33]:


display(df_ele['STATNAME'].unique())


# In[34]:


display(df_sec['statname'].unique())


# In[35]:


df_ele.describe()


# In[36]:


trace1 = go.Scatter(
      x = df_ele.STATNAME,
      y = df_ele.OVERALL_LI,
)

trace2 = go.Scatter(
    x=df_sec.statname,
    y=df_sec.literacy_rate,
    xaxis='x2',
    yaxis='y2'
)

data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45],
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[37]:


literacy_data = df_ele.loc[:,['STATNAME','OVERALL_LI','MALE_LIT','FEMALE_LIT']]
literacy_data.head(5)


# In[38]:


literacy_data_sec = df_sec.loc[:,['statname','literacy_rate','male_literacy_rate','female_literacy_rate']]
literacy_data_sec.head(5)


# In[39]:


# Create and style traces
trace0 = go.Scatter(
    x = df_ele.STATNAME,
    y = df_ele.OVERALL_LI,
    mode = "lines+markers",
    name = 'Elementary literacy',
    line = dict(
        color = ('rgba(255,10,10, 0.8)'),
        width = 1)
)
trace1 = go.Scatter(
    x = df_ele.STATNAME,
    y = df_ele.MALE_LIT,
    mode = "lines+markers",
    name = 'Elelmentary male literacy',
    line = dict(
        width = 1)
)

trace2 = go.Scatter(
    x = df_ele.STATNAME,
    y = df_ele.FEMALE_LIT,
    mode = "lines+markers",
    name = 'Elelmentary female literacy',
    line = dict(
        width = 1,
        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x = df_ele.STATNAME,
    y = df_sec.literacy_rate,
    mode = "lines+markers",
    name = 'secondary literacy rate',
    line = dict(
        width = 1,
        dash = 'dash')
)
trace4 = go.Scatter(
    x = df_ele.STATNAME,
    mode = "lines+markers",
    y = df_sec.male_literacy_rate,
    name = 'secondary male literacy rate',
    line = dict(
        width = 1,
        dash = 'dot')
)

trace5 = go.Scatter(
    x = df_ele.STATNAME,
    y = df_sec.female_literacy_rate,
    mode = "lines+markers",
    name = 'secondary female literacy rate',
    line = dict(
        width = 1,
        dash = 'dot')
)
data = [trace0, trace1, trace2, trace3, trace4, trace5]

# Edit the layout
layout = dict(title = 'Statewise literacy rate in India',
                      xaxis= dict(
                          ticklen= 5,
                          tickangle=90,
                          zeroline= False),

                      yaxis=dict(
                            title='Statewise literacy rate'
                        )
                     )

fig = dict(data=data, layout=layout)
iplot(fig)


# In[41]:


#add columns total_number of district
district_dic = {'WEST BENGAL':23,
'UTTARAKHAND':13,
'UTTAR PRADESH':75,
'TRIPURA':8,
'TELANGANA':31,
'TAMIL NADU':32,
'SIKKIM':4,
'RAJASTHAN':33,
'PUNJAB':22,
'PUDUCHERRY':4,
'ODISHA':30,
'DELHI':11,
'NAGALAND':11,
'MIZORAM':8,
'MEGHALAYA':11,
'MANIPUR':16,
'MAHARASHTRA':36,
'MADHYA PRADESH':51,
'LAKSHADWEEP':1,
'KERALA':14,
'KARNATAKA':30,
'JHARKHAND':24,
'JAMMU & KASHMIR':22,
'HIMACHAL PRADESH':12,
'HARYANA':22,
'GUJARAT':33,
'GOA':2,
'DAMAN & DIU':2,
'DADRA & NAGAR HAVELI':1,
'CHHATTISGARH':27,
'CHANDIGARH':1,
'BIHAR':38,
'ASSAM':33,
'ARUNACHAL PRADESH':21,
'ANDHRA PRADESH':13,
'A & N ISLANDS':3}


# In[42]:


df_ele['TOT_DISTRICT'] = df_ele['STATNAME'].map(district_dic)


# In[43]:


#df_ele['PER_DIST'] = df_ele.apply(lambda x: (df_ele['DISTRICTS']*100)/df_ele['TOT_DISTRICT'])
df_ele['PER_DIST'] = (df_ele.DISTRICTS * 100)/df_ele.TOT_DISTRICT
df_ele.head(2)


# In[44]:


x = df_ele.STATNAME

# Creating trace1
trace1 = go.Scatter(
                    x = x,
                    y = df_ele.PER_DIST,
                    mode = "lines+markers",
                    name = "District count",
                    text= df_ele.STATNAME)

data = [trace1]
layout = dict(title = 'Data reported from District (in %) from each state',
              xaxis= dict(
                  ticklen= 5,
                  tickangle=90,
                  zeroline= False),
                  
              yaxis=dict(
                    title='Data reported from District (in %)'
                )
             )
fig = dict(data = data, layout = layout)
iplot(fig)


# In[45]:


# Creating trace1
trace1 = go.Scatter(
                    x = df_ele.STATNAME,
                    y = df_ele.TOT_6_10_15,
                    mode = "lines+markers",
                    name = "Age Group 6 to 10",
                    text= df_ele.STATNAME)
trace2 = go.Scatter(
                    x = df_ele.STATNAME,
                    y = df_ele.TOT_11_13_15,
                    mode = "lines+markers",
                    name = "Age Group 11 to 13",
                    text= df_ele.STATNAME
                    )
trace3 = go.Scatter(
                    x = df_ele.STATNAME,
                    y = df_ele.OVERALL_LI,
                    mode = "lines+markers",
                    name = "Overall Literacy",
                    text= df_ele.STATNAME,
                    yaxis='y2')
data = [trace1, trace2, trace3]
layout = dict(title = 'Projected Population vs Literacy',
              xaxis= dict(
                  ticklen= 5,
                  tickangle=90,
                  zeroline= False),
                  
              yaxis=dict(
                    title='Projected Population'
                ),
              yaxis2=dict(
              title='Overall Literacy',
              titlefont=dict(
               color='rgb(148, 103, 189)'
              ),
              tickfont=dict(
              color='rgb(148, 103, 189)'
           ),
             overlaying='y',
             side='right'
         )
       )

fig = dict(data = data, layout = layout)
iplot(fig)


# In[ ]:




