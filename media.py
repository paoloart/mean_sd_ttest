import pandas as pd
from scipy import stats

dataset = pd.read_csv('dataset.csv') # legge il csv e lo salva come dataframe

print(dataset) # printa il dataframe

mean1 = dataset.iloc[:,0].mean() # calcola la media dei valori della colonna 1
mean2 = dataset.iloc[:,1].mean() # calcola la media dei valori della colonna 2

std1 = dataset.iloc[:,0].std() # calcola la deviazione standard dei valori della colonna 1
std2 = dataset.iloc[:,1].std() # calcola la deviazione standard dei valori della colonna 2


t_stat, p_value = stats.ttest_ind(dataset.iloc[:,0], dataset.iloc[:,1]) # calcola il t-statistico e il p-value

#printa i risultati a terminale
print(std1, std2)
print(mean1, mean2)
print(t_stat, p_value)