class CountyData:
    
    def __init__(self):
        """County & State Level Data Object"""
        
    def rawdata(self):
        #Extracting Data & removing unnecessary column
        data=pd.read_csv('confirmed-covid-19-deaths-in-us-by-state-and-county.csv').drop(['Unnamed: 0','geometry'], axis=1)
        data=data.rename(columns={'county_fips':'COUNTY_FIPS','county_name':'COUNTY_NAME','state_name':'STATE_NAME','state_fips':'STATE_FIPS','date':'DATE','deaths':'DEATHS','lat':'LATITUDE','long':'LONGITUDE'})
        
        #Dropping null data
        data=data.dropna(subset=data.columns[[0,3,6,7]],how='any')
        
        #Replace cases and deaths blank value to 0
        data['DEATHS']=data['DEATHS'].replace(to_replace='',value=0)
        
        data.to_csv('Covid_County_Level_Data.csv',index=False)
        print("Data has been cleaned & saved as Covid_County_Level_Data.csv")
        
        return data
        
