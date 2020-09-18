import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime
import pandas as pd
import matplotlib.pyplot as plt

start_date = datetime.date(2019,1,1) 
end_date = datetime.date(2019,3,1)
Assets = ['EURUSD']

#import_ticks_method(Assets, start_date, end_date, 1, TimeFrame.TICK, ".", True)
tick_data = pd.read_csv('EURUSD-2019_01_01-2019_03_01.csv')
print(tick_data)


plt.plot(tick_data['ask'])
plt.plot(tick_data['bid'])
plt.show()