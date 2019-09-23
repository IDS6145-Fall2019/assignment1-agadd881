import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('Turnstile_NYC_59st_2017.csv')
df.sort_values(by=['Date','Time'], inplace=True)
group = df.groupby(['Date']).mean()
col = group.iloc[:,0] # first column of grouped info- by date
#group.plot(x,y='Entries', kind='scatter')
col.plot(kind='bar')
axes.set_title('NYC Turnstile Uses by Date in 2017 at 59 St')
axes.set_ylabel('Average Number of People Through Turnstile')
axes.set_ylabel('Date')
plt.show()
print(group)