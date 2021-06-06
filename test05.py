import pandas as pd
import matplotlib.pyplot as plt

def readData():
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
    
    return df3

def drawBar(df):
    #繪製多個直條圖
    plt.subplot(2,3,1)
    plt.bar(df.index, df['0'] )
    plt.title('0歲')
    plt.subplot(2,3,2)
    plt.bar(df.index, df['1-3'])
    plt.title('1-3歲')
    plt.subplot(2,3,3)
    plt.bar(df.index, df['4-6'])
    plt.title('4-6歲')
    plt.subplot(2,3,4)
    plt.bar(df.index, df['7-15'])
    plt.title('7-15歲')
    plt.subplot(2,3,5)
    plt.bar(df.index, df['16+'])
    plt.title('16+歲')

    #解決中文亂碼
    plt.rcParams['font.sans-serif']=['Lisu']
    plt.rcParams['axes.unicode_minus']=False

    plt.show()

df=readData()
drawBar(df)