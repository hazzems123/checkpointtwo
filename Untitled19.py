#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


url='https://drive.google.com/file/d/1YdbRKJZ0Kz742yDxIStLZIPIEUGlc1Cc/view'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]


# In[12]:


df = pd.read_csv(url2,sep=";")


# In[13]:


print (df.head)


# In[15]:


df.isnull().sum()


# In[18]:


df['Age'].fillna(df['Age'].mean(), inplace=True)


# In[19]:


print (df)


# In[21]:


print (df["Cabin"].value_counts())


# In[22]:


df["Cabin"].fillna('G6',inplace=True)


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt

grid = sns.FacetGrid(df, col = "Survived" ,row = "Sex" , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Age", bins = 20)


# In[27]:





# In[25]:





# In[26]:





# In[ ]:


print (grid)


# In[31]:


grid = sns.FacetGrid(df, col = "Survived" ,row = "PClass" , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Cabin", bins = 20)


# In[33]:


grid = sns.FacetGrid(df, col = "Survived"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[34]:


def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )


# In[36]:


plot_correlation_map(df)


# In[37]:


#this graph simply means the correlation between each column against the other one , the values above zeros shows a positive correlation means when a value increase the other value increase as well, the values below zero means negative correlation , zero means no correlation between them.


# In[39]:


df.groupby(['Pclass', 'Survived']).mean()


# In[40]:


df.drop('Name',
  axis='columns', inplace=True)


# In[41]:


print (df.head)


# In[42]:


url='https://drive.google.com/file/d/1YdbRKJZ0Kz742yDxIStLZIPIEUGlc1Cc/view'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]


# In[43]:


df = pd.read_csv(url2,sep=";")


# In[44]:


print (df)


# In[59]:


title = [];
for i in df['Name'].str.split('.').str[0]:
    title.append(i)


# In[63]:


titles =[];
for i in title :
    titles.append(i.split(',', 1)[1])


# In[64]:


print (titles)


# In[65]:


df.insert(1, "Title", titles, True)


# In[70]:


print (df)


# In[69]:


corrone= df["Title"].corr(df["Pclass"])


# In[68]:


print (g)


# In[71]:


grid = sns.FacetGrid(df, col = "Title"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[76]:


Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer",

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty",

                  "the Countess": "Royalty",

                    "Dona":       "Royalty",

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs",

                    "Master" :    "Master"

                    }
    


# In[99]:


newTitles = []
for i in titles :
     i=i.lstrip()
     newTitles.append(Title_Dictionary[i])


# In[100]:


print (newTitles)


# In[103]:


df.drop('Title',
  axis='columns', inplace=True)


# In[104]:


df.insert(1, "Title", newTitles, True)


# In[105]:


print (df)


# In[106]:


grid = sns.FacetGrid(df, col = "Title"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[107]:


sum_column = df["Parch"] + df["SibSp"]
print (sum_column)


# In[ ]:




