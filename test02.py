import pandas as pd
import matplotlib.pyplot as plt
#讀取資料
df=pd.read_csv('RODS_EnteroviralInfection.csv')
#整理資料
df1=df[df.年==2020]
df2=df1[df1.縣市.isin(['台南市','高雄市','屏東縣'])]
print(df2)
#統計
df3=df2.groupby('縣市').sum()
print(df3)
#改變index排列順序
reorderlist = ['台南市','高雄市','屏東縣']
df3=df3.reindex(reorderlist)
#繪製統計圖
plt.bar(df3.index, df3['腸病毒急診就診人次'])
plt.title('2020年南部地區腸病毒急診就診人數統計圖')
plt.ylabel('人數')
#解決中文亂碼
plt.rcParams['font.sans-serif']=['Lisu']
plt.rcParams['axes.unicode_minus']=False
plt.show()
