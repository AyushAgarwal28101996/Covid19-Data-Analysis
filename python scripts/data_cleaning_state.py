import pandas as pd

class StateData:
    
    def __init__(self):
        """STate Level Data Object"""
        
    def rawdata(self):
        #Extracting Data & removing unnecessary column
        data= pd.read_csv("covid-19-state-level-data.csv").drop('Unnamed: 0',axis=1)
        data= data.rename(columns = {'date':'DATE','state':'STATE','fips':'FIPS','cases' : 'CASES', 'deaths' : 'DEATHS'})
        
        #Dropping null data
        data=data.dropna(subset=data.columns[[0,1]],how='any')
        
        #Replace cases and deaths blank value to 0
        data=data.replace(to_replace="",value=0)
        
        data.to_csv('Covid_State_Level_Data.csv',index=False)
        print("Data has been cleaned & saved as Covid_State_Level_Data.csv")
        
        return data
     
