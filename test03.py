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
#計算直條圖位移位置
w=0.18  #假設直條圖的寬度
x3=[i for i in range(len(df3.index))]
x1=[i-w*2 for i in range(len(df3.index))]
x2=[i-w for i in range(len(df3.index))]
x4=[i+w for i in range(len(df3.index))]
x5=[i+w*2 for i in range(len(df3.index))]
#繪製分組直條圖
plt.bar(x1, df3['0'], width=w)
plt.bar(x2, df3['1-3'], width=w)
plt.bar(x3, df3['4-6'], width=w)
plt.bar(x4, df3['7-15'], width=w)
plt.bar(x5, df3['16+'], width=w)
plt.legend(['0','1-3','4-6','7-15','16+'])
plt.title('2020年南部地區腸病毒急診就診人數統計圖')
plt.xticks(x3,df3.index)
#解決中文亂碼
plt.rcParams['font.sans-serif']=['Lisu']
plt.rcParams['axes.unicode_minus']=False

plt.show()
