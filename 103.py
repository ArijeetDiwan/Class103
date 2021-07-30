import pandas as pd
df=pd.DataFrame()
print(df)

import pandas as pd
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

import pandas as pd
data=[['s101','arijeet',100],['s102','okmam',1000],['s103','uchiha','10000']]
df=pd.DataFrame(data,columns=['ID','Name','Marks'])
print(df) 