import pandas as pd
import numpy as np
def main():

    nodes=["a20","apoptosis","bclxl","bid","caspase",
           "ceramide","creb","ctla4","cytoskeletonsignaling",
           "disc","erk","fas","fasl","fast","flip","fyn","gap",
           "gpcr","grb2","gzmb","iap","ifng","ifngt","il2","il2ra",
           "il2rat","il2rb","il2rbt","jak","lck","mcl1","mek","nfat",
           "nfkb","p2","p27","pdgfr","pi3k","plcg1","proliferation",
           "rantes","ras","s1p","sfas","smad","socs","sphk1","stat3",
           "tbet","tcr","tnf","tpl2","tradd","zap70","il15","stimuli",
           "cd45","stimuli2","pdgf","tax"]
    temp=np.random.choice(a=[0,1],size=[100000,60])
    l1=[]
    for i in range(0,100000):
        l1.append('is_' + str(i+1).rjust(6, '0'))
    df1=pd.DataFrame(temp,index=l1,columns=nodes)
    
    df1.to_csv('initial_states.txt',sep=' ')

main()

        
