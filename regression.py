#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.show()
#Подготавливаем данные по BTC
#Считываем
data_btc = pd.read_csv("BTC-Daily.csv")
#Выбираем нужные нам значения - цену для сравнения и дату для сортировки
data_btc = data_btc[['unix','close']]
#Переименуем колонки
data_btc = data_btc.rename(columns={'unix':'time','close':'btc_price'})
#В данный момент значение даты убывает, мы перевернем список для более удобного использования
#Переворачиваем (reverse) список
data_btc = data_btc[::-1]
#Подготавливаем данные по ETH
#Считываем
data_eth = pd.read_csv("EtherPriceHistory(USD).csv")
#Выбираем нужные нам значения - цену для сравнения и дату для сортировки
data_eth = data_eth[['UnixTimeStamp', 'Value']]
#Переименуем колонки
data_eth = data_eth.rename(columns={'UnixTimeStamp':'time','Value':'eth_price'})
#Выровним два списка по дате
#Выравниваем по нижней границе даты
data_btc = data_btc[data_btc.time >= data_eth.time[0]]
#Выравниваем по верхней границе даты
data_btc = data_btc[data_btc.time <= data_eth.time.iloc[-1]]
#Сбрасываем индех для двух списков для удобной работы в дальнейшем
data_btc = data_btc.reset_index(drop=True)
data_eth = data_eth.reset_index(drop=True)
#(BTC) Избавляемся от ненужной метки времени и создаем простой список
#(ETH) Избавляемся от ненужной метки времени и создаем простой список
#создаем единый DF
df = pd.concat([data_btc.btc_price, data_eth.eth_price], axis=1)
def show_graph(df):
    '''Показывает график зависимости цены ETH и BTC'''
    df.plot(x='btc_price', y='eth_price', kind='scatter')
    plt.show()
def correlation(df):
    '''Показывает корреляцию между ценой ETH и BTC'''
    print(df['eth_price'].corr(df['btc_price']))
def show_graph_btc_time(data_btc):
    '''Временной график роста BTC'''
    data_btc.plot(x='time', y='btc_price', kind='scatter')
    plt.show()
def show_graph_eth_time(data_eth):
    '''Временной график роста ETH'''
    data_eth.plot(x='time', y='eth_price', kind='scatter')
    plt.show()
show_graph(df)
correlation(df)
# %%
