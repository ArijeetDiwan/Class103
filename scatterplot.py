import pandas as pd
import plotly.express as ps 

df=pd.read_csv("data.csv")
fig=ps.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=100)
fig.show()
#Population,Per capita