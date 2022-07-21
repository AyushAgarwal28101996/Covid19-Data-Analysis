import pandas as pd
data2 = pd.read_csv("Covid_State_Level_Data.csv")
data2 = data2.groupby(["STATE","FIPS"]).sum().nlargest(3,"DEATHS")
data2.reset_index(level=[0,1], inplace=True)
data3=pd.read_csv("Covid_County_Level_Data.csv")

x=0
for i in data2.FIPS:
    print (data2.STATE[x],data2.DEATHS[x])
    
    data4 = pd.DataFrame({'COUNTY_FIPS':int(),'COUNTY_NAME':str(),'STATE_NAME':str(),'STATE_FIPS':int(),
                    'DEATHS':int(),'LATITUDE':float(),'LONGITUDE':float()}, index=[])
    
    y=0
    z=0
    for j in data3.STATE_FIPS:
        if data2.FIPS[x]==j:
            data4.loc[z]=data3.iloc[y]
            z+=1
        y+=1  
    data5 = data4.groupby(["COUNTY_FIPS","COUNTY_NAME","STATE_FIPS"]).sum().nlargest(3,"DEATHS")
    data5.reset_index(level=[0,1,2], inplace=True)
    data5=data5.drop(['COUNTY_FIPS','STATE_FIPS','LATITUDE','LONGITUDE'], axis=1)
    print(data5)
    x+=1
