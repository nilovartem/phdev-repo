import pandas as pd

#Подготавливаем данные по BTC
#Считываем
data_btc = pd.read_csv("BTC-Daily.csv")
#Выбираем нужные нам значения - цену для сравнения и дату для сортировки
data_btc = data_btc[['unix','close']]
#Переименуем колонки
data_btc = data_btc.rename(columns={'unix':'time','close':'price'})
#В данный момент значение даты убывает, мы перевернем массив для более удобного использования
#Переворачиваем (reverse) массив
data_btc = data_btc[::-1]
#Подготавливаем данные по ETH
#Считываем
data_eth = pd.read_csv("EtherPriceHistory(USD).csv")
#Выбираем нужные нам значения - цену для сравнения и дату для сортировки
data_eth = data_eth[['UnixTimeStamp', 'Value']]
#Переименуем колонки
data_eth = data_eth.rename(columns={'UnixTimeStamp':'time','Value':'price'})
#Выровним два массива по дате
#Выравниваем по нижней границе даты
data_btc = data_btc[data_btc.time >= data_eth.time[0]]
#Выравниваем по верхней границе даты
data_btc = data_btc[data_btc.time <= data_eth.time.iloc[-1]]
#Сбрасываем индех для двух сетов для удобной работы в дальнейшем
data_btc = data_btc.reset_index(drop=True)
data_eth = data_eth.reset_index(drop=True)
print(data_btc)
print(data_eth)


