import pandas as pd
from pandas import read_csv

df = pd.read_csv('/home/cit/Major Project/turbo/CMAPSSData/train_FD001.txt',sep='\s+',names=['unit number','time, in cycles','operational setting 1','operational setting 2','operational setting 3','sensor measurement  1','sensor measurement  2','sensor measurement  3','sensor measurement  4','sensor measurement  5','sensor measurement  6','sensor measurement  7','sensor measurement  8','sensor measurement  9','sensor measurement  10','sensor measurement  11','sensor measurement  12','sensor measurement  13','sensor measurement  14','sensor measurement  15','sensor measurement  16','sensor measurement  17','sensor measurement  18','sensor measurement  19','sensor measurement  20','sensor measurement  21'])
df.to_csv('data_out1.csv')



