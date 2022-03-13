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
# QUESTION 7
# QUESTION 8
# QUESTION 9
# QUESTION 10
