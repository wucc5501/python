import pandas as pd
import matplotlib.pyplot as plt
#讀取資料    
df=pd.read_csv('RODS_EnteroviralInfection.csv')
#整理資料
df1=df[df.年==2020]
df2=df1[df1.縣市.isin(['台南市','高雄市','屏東縣'])]
print(df2)
#樞紐分析
df3=pd.pivot_table(df2, index='縣市', columns='年齡別', values='腸病毒急診就診人次',aggfunc='sum')
print(df3)
reorderlist = ['台南市','高雄市','屏東縣']
df3=df3.reindex(reorderlist)
print(df3)
#繪製堆疊直條圖
plt.bar(df3.index, df3['0'] )
plt.bar(df3.index, df3['1-3'], bottom=df3['0'])
plt.bar(df3.index, df3['4-6'], bottom=df3['0']+df3['1-3'])
plt.bar(df3.index, df3['7-15'], bottom=df3['0']+df3['1-3']+df3['4-6'])
plt.bar(df3.index, df3['16+'], bottom=df3['0']+df3['1-3']+df3['4-6']+df3['7-15'])
plt.legend(['0','1-3','4-6','7-15','16+'])
plt.title('2020年南部地區腸病毒急診就診人數統計圖')
#解決中文亂碼
plt.rcParams['font.sans-serif']=['Lisu']
plt.rcParams['axes.unicode_minus']=False

plt.show()
