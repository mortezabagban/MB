import pandas as pd
import numpy as np
# import matplotlib as mb
df=pd.DataFrame(
    {
    "name":["ali","hamid","mariza"],
    "age":[22,30,20],
    "sex":["man","woman","sair"],
}
)
#print(df)
#print(df["name"])#show the series and name
agess=pd.Series([22,80,90],name="aagess")#creation a series 
# agess
# df["age"].max()
# df.describe()#sumari Descrbtion creation
# df["age"].sum()
# agess.max()
# agess.max()
s=pd.DataFrame(np.random.randn(1000,5),columns=['a','s','d','f','g'])
# s[::2]=np.nan
# s.describe()
# pd.Series(["a","a","a","b","b",np.nan,"b"]).describe()
frame=pd.DataFrame({
    "aa":["yy","yy","xx","xx"],
    "bb":range(4)
})
# frame.describe(include="all")#for both numberical and textual data 
# frame.describe(include="object")# for textual Datat
# frame.describe(include="number")#for numberical data
#argmin and argmax in numpy ~ idxmin and idxmax in pandas
# s1=pd.Series(np.random.randn(5))
# print(s1)
# print(s1.idxmin(),s1.idxmax())
df1=pd.DataFrame(np.random.randn(5,3),columns=["A","B","C"])
print(df1.idxmin(axis=0))
print("******************************")
print(df1.idxmax(axis=1))
print("////////////////////////////*")
df1
iris=pd.read_csv("D:/m11.csv")
iris.head(8)
# iris.tail(8)
iris.assign(sepl_reque = iris["sepale2"]/iris["sepale1"])
iris.assign(sepl_reque2 = lambda x:(x["sepale2"]/x["sepale1"])) #add a function to assign func

#assign() merging the resulte of the calclutions to the dataframe>return a copy of Data
#query over the dataset 
aa=iris.query("sepale1 >70").assign(
sepl_reque2 = lambda x:(x["sepale2"]/x["sepale1"]),
petal_reque2 = lambda x:(x["petallengh2"]/x["petallengh"])
)
#.plot (kind="scatter",x= "sepl_reque2",y= "petal_reque2")