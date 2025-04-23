import csv
fh = open("Employee.csv","w")
ewriter = csv.writer(fh)
empdata = [['name','salary'],['ajith',50000],['anu',20000]]
ewriter.writerows(empdata)
fh.close()


import math
num = 16
sqrt = math.sqrt(num)
print(sqrt)

import datetime
now = datetime.datetime.now()
print(now)

# chapter -5 data cleaning and plotting
# handling missing data
import numpy as np
import pandas as pd
data = pd.DataFrame({'name':['alice','bod',np.nan,'dave'],
                     'age':[24,np.nan,19,22],
                     'score':[90,85,np.nan,88]})
clean = data.replace(np.nan,"Unknown")
print(clean)
print(data.drop_duplicates())


import numpy as np
import pandas as pd
data = pd.DataFrame({'name':["ajit","ajit","police"],
                     'age':[84,84,52]})
print(data.drop_duplicates())

import pandas as pd
data = pd.DataFrame({
    'department' : ['hr','it','pm','it'],
    'salary' :[2000,5000,4000,6000]
})

avg = data.groupby('department')['salary'].mean()
print(avg)
