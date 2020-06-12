import pandas as pd
import numpy as np
from numpy import loadtxt,savetxt

sis=loadtxt('dedu.csv',delimiter=',')
mom=loadtxt('mom.csv',delimiter=',')
me=loadtxt('bunny.csv',delimiter=',')
dad=loadtxt('dad.csv',delimiter=',')
obama=loadtxt('obama-2.csv',delimiter=',')

embedding_df=pd.DataFrame({"Bharadwaj":me,"sis":dedu,"mom":mom,"dad":dad,"Obama":obama})
embedding_df.to_csv("embeddings.csv",index=False)

print(embedding_df.columns)
print(embedding_df.columns[[0,1]])
