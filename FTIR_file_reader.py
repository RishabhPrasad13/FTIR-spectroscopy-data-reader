
import pandas as pd
import os


#naming convention of FTIR spectroscopy data files must be 'BX_bin_30' or 'BX_bin_50' depending on resolution. X corresponds to biofuel number
#Place .py file in same directory as ASP file folder

files= sorted(os.listdir("Replace with name of folder containing ASP files"),key=len) #otherwise not in order


names=[x.split('.')[0] for x in files]


Data=[]
for fhand in files:
    path=r'Replace with directory of folder containing ASP files'+fhand
    file=open( path,'r')
    lines=file.readlines()
    lines=[line.rstrip() for line in lines]
    Data.append(lines)

#Data is a list of lists, where each individual list is a particular FTIR spectrum
dict = {}
keys = names
values = Data

n=0
for i in keys:
        dict[i] = values[n]
        n+=1
#if we make the dataframe from dictionary , we set rows rather than column

#Next the data is split by resolution
data_30={k: v for k, v in dict.items() if '30' in k}
data_50={k: v for k, v in dict.items() if '50' in k}


df_30=pd.DataFrame(data_30)
df_50=pd.DataFrame(data_50)



df_30.to_csv('Sun_bin_30.csv')
df_50.to_csv('Sun_bin_50.csv')


nums=([int(x.split('_')[0].split('B')[1]) for x in names ])[::2]  #step because numbers repeated twice
print(nums)   #list of blend numbers , useful for matlab
