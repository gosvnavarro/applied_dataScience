# QUESTION 1
def answer_one():
   df_E = pd.read_excel("assets/Energy Indicators.xls")
   df_E.drop(columns = ['Unnamed: 0', 'Unnamed: 1'],inplace=True)
   df_E.drop(df_E.index[0:17],0,inplace=True)
   df_E.drop(df_E.index[227:],0,inplace=True)
   df_E.rename(columns={'Unnamed: 2': 'Country', 'Unnamed: 3': 'Energy Supply', 'Unnamed: 4': 'Energy Supply per Capita', 'Unnamed: 5': '% Renewable' }, inplace=True )
   df_E.replace({'...':np.nan}, inplace= True)
   df_E['Energy Supply'] = df_E['Energy Supply']*1000000
    
   a = []
   for i in df_E['Country']:
       i = i.split(' (')
       a.append(i[0])
   df_E['Country'] = a
    
   b = []
   for i in df_E['Country']:
       i = re.findall("[^0-9]+", i)
       b.append(i[0])
   df_E['Country'] = b
    
   df_E.replace({"Republic of Korea": "South Korea", 
                 "United States of America": "United States", 
                 "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", 
                 "China, Hong Kong Special Administrative Region": "Hong Kong"}, 
                inplace= True)
   
   GDP = pd.read_csv("assets/world_bank.csv")
   GDP.drop(GDP.index[0:3],0,inplace=True)
   GDP.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
   
   il = GDP.iloc[0]
   di = {}
   i = 0
   for d in GDP.columns:
       if type(il[i]) == np.float64:
           di[d] = str(int(il[i]))
       else:
           di[d] = il[i]
       i += 1
   
   GDP.rename(columns = di, inplace=True)
   GDP.drop(GDP.index[0:1],0,inplace=True)
   GDP.rename(columns = {'Country Name': 'Country'}, inplace=True)
   
   ScimEn = pd.read_excel("assets/scimagojr-3.xlsx")
   
   j1 = pd.merge(ScimEn,Energy)
   j2 = pd.merge(j1, GDP)
   j2.set_index('Country', inplace = True)
   j2 = j2[0:15]
   j2.drop(j2.columns[[np.arange(10,59)]], axis='columns', inplace = True)
   
   return j2
   raise NotImplementedError()

answer_one()

# QUESTION 2
def answer_two():
    Energy = pd.read_excel("assets/Energy Indicators.xls")
    Energy.drop(columns=['Unnamed: 0', 'Unnamed: 1'],inplace=True)
    Energy.drop(Energy.index[0:17],0,inplace=True)
    Energy.drop(Energy.index[227:],0,inplace=True)
    Energy.rename(columns={'Unnamed: 2': 'Country', 'Unnamed: 3': 'Energy Supply', 'Unnamed: 4': 'Energy Supply per Capita', 'Unnamed: 5': '% Renewable' }, inplace=True )
    Energy.replace({'...':np.nan}, inplace= True)
    Energy['Energy Supply'] = Energy['Energy Supply']*1000000
    
    l= []
    for i in Energy['Country']:
        i=i.split(' (')
        l.append(i[0])
    Energy['Country'] = l
    
    li = []
    for i in Energy['Country']:
        i = re.findall("[^0-9]+", i)
        li.append(i[0])
    Energy['Country'] = li
    
    Energy.replace({"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace= True)
    
    GDP = pd.read_csv("assets/world_bank.csv")
    GDP.drop(GDP.index[0:3],0,inplace=True)
    GDP.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    
    il = GDP.iloc[0]
    di = {}
    i = 0
    for d in GDP.columns:
        if type(il[i]) == np.float64:
            di[d] = str(int(il[i]))
        else:
            di[d] = il[i]
        i += 1
    
    GDP.rename(columns=di, inplace=True)
    GDP.drop(GDP.index[0:1],0,inplace=True)
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    
    ScimEn = pd.read_excel("assets/scimagojr-3.xlsx")
    
    ji = pd.merge(ScimEn,Energy)
    ji = pd.merge(ji, GDP)
    ji.set_index('Country', inplace = True)
    
    j1 = pd.merge(ScimEn,Energy, how="outer")
    j2 = pd.merge(j1, GDP, how="outer")
    j2.set_index('Country', inplace = True)
    
    diff = j2.shape[0] - ji.shape[0]
    
    return  diff
    raise NotImplementedError()

answer_two()

# QUESTION 3
def answer_three():
    ng = np.arange(10,20)
    dat = answer_one().columns[[ng]]
    avgGDP = answer_one()[dat].mean(axis=1).sort_values(ascending=False)
    
    return avgGDP
    raise NotImplementedError()

answer_three()

# QUESTION 4
def answer_four():
    pg = answer_one().loc['United Kingdom', ['2006']]['2006']
    dg = answer_one().loc['United Kingdom', ['2015']]['2015']
    dkd = dg - pg
    
    return dkd
    raise NotImplementedError()

answer_four()

# QUESTION 5
def answer_five():
    mpc = answer_one()['Energy Supply per Capita'].mean()
    
    return mpc
    raise NotImplementedError()

answer_five()

# QUESTION 6
def answer_six():
   max_ren = answer_one()['% Renewable'].max()
   ind = answer_one().index[answer_one()['% Renewable'] == max_ren][0]
   
   return ind, max_ren
   raise NotImplementedError()

answer_six()

# QUESTION 7
def answer_seven():
   new_df = answer_one().assign(ratio = answer_one()['Self-citations']/answer_one()['Citations'])
   max_ra = new_df['ratio'].max()
   con = new_df.index[new_df['ratio'] == max_ra][0]
    
   return con, max_ra
   raise NotImplementedError()

answer_seven()

# QUESTION 8
def answer_eight():
    Top15 = answer_one()
    Top15['pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    dpop = Top15['pop'].sort_values(ascending=False)[2]
    py = Top15.index[Top15['pop'] == dpop][0]
    
    return py
    raise NotImplementedError()

answer_eight()

# QUESTION 9
def answer_nine():
    Top15 = answer_one()
    Top15 = Top15.assign(pop = Top15['Energy Supply']/Top15['Energy Supply per Capita'])
    Top15 = Top15.assign(Citable_docs_per_Capita = Top15['Citable documents'] / Top15['pop'])
    corre = Top15['Citable_docs_per_Capita'].corr(Top15['Energy Supply per Capita'])
    
    return corre
    raise NotImplementedError()

answer_nine()


def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
      
plot9()

# QUESTION 10
def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew'] = 1
    j = 0
    for i in Top15['% Renewable']:
        if i >= Top15['% Renewable'].median():
            Top15['HighRenew'].iloc[j] = 1
        else:
            Top15['HighRenew'].iloc[j] = 0
        j+=1
    
   return Top15['HighRenew']
   raise NotImplementedError()

answer_ten()

# QUESTION 11
def answer_eleven():
    ContinentDict  = {'China':'Asia', 
                      'United States':'North America', 
                      'Japan':'Asia', 
                      'United Kingdom':'Europe', 
                      'Russian Federation':'Europe', 
                      'Canada':'North America', 
                      'Germany':'Europe', 
                      'India':'Asia',
                      'France':'Europe', 
                      'South Korea':'Asia', 
                      'Italy':'Europe', 
                      'Spain':'Europe', 
                      'Iran':'Asia',
                      'Australia':'Australia', 
                      'Brazil':'South America'}
    
    j = 0
    Top15 = answer_one()
    new_df = pd.DataFrame(index=['Asia', 'Australia', 'Europe', 'North America', 'South America'], columns = ['size', 'sum', 'mean', 'std'])
    
    Top15['pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Continent'] = 'cont'
    for v in ContinentDict.values():
        Top15['Continent'].iloc[j] = v
        j += 1
    new_df['size'] = Top15.groupby(Top15['Continent']).size()
    new_df['sum'] = Top15['pop'].groupby(Top15['Continent']).sum()
    new_df['mean'] = Top15['pop'].groupby(Top15['Continent']).mean()
    new_df['std'] = Top15['pop'].groupby(Top15['Continent']).std()
   
    return new_df 
    raise NotImplementedError()

answer_eleven()

# QUESTION 12
def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                      'United States':'North America', 
                      'Japan':'Asia', 
                      'United Kingdom':'Europe', 
                      'Russian Federation':'Europe', 
                      'Canada':'North America', 
                      'Germany':'Europe', 
                      'India':'Asia',
                      'France':'Europe', 
                      'South Korea':'Asia', 
                      'Italy':'Europe', 
                      'Spain':'Europe', 
                      'Iran':'Asia',
                      'Australia':'Australia', 
                      'Brazil':'South America'}
    
    j = 0
    Top15 = answer_one()
    Top15['Continent'] = None
    for v in ContinentDict.values():
        Top15['Continent'].iloc[j] = v
        j += 1
    Top15['% Renewable'] = pd.cut(Top15['% Renewable'],bins=5)
    new_renou = Top15.groupby(['Continent','% Renewable']).size()
    
    return new_renou
    raise NotImplementedError()

answer_twelve()

# QUESTION 13
def answer_thirteen():
    Top15 = answer_one()
    Top15['pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['pop'].map('{:,}'.format)

    return Top15['PopEst']
    raise NotImplementedError()
    
answer_thirteen()

# OPTIONAL QUESTION
def plot_optional():
    import matplotlib as plt
    
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
         ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
    This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
    2014 GDP, and the color corresponds to the continent.")
   
plot_optional()
