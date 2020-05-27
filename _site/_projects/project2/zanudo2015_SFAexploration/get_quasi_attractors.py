from re import *
import pandas as pd
import itertools
def main():
    cols=['a20','apoptosis','bclxl','bid','caspase',
          'ceramide','creb','ctla4','cytoskeletonsignaling',
          'disc','erk','fas','fasl','fast','flip','fyn','gap',
          'gpcr','grb2','gzmb','iap','ifng','ifngt','il2','il2ra',
          'il2rat','il2rb','il2rbt','jak','lck','mcl1','mek','nfat',
          'nfkb','p2','p27','pdgfr','pi3k','plcg1','proliferation',
          'rantes','ras','s1p','sfas','smad','socs','sphk1','stat3',
          'tbet','tcr','tnf','tpl2','tradd','zap70','il15','stimuli',
          'cd45','stimuli2','pdgf','tax']
    ind=['attr_'+str(n) for n in range(1,878)]
    df1=pd.DataFrame(index=ind,columns=cols)


    with open('basins_of_boolean/result_temp.txt','r') as f:
        att=f.read().split('\n\n')
        current=0
        for a in att:
            x=a.split('\n')
            if len(x)>1:
                clist=[list(elem)for elem in x]
                fa=[]
                for j in range(60):
                    h=[]
                    for i in range(len(clist)):
                        h.append(clist[i][j])
                    if len(set(h))>1:
                        fa.append('X')
                    else:
                        fa.append(h[0])
                df1.iloc[current,]=fa
                current+=1
            else:
                t=list(x[0])
                df1.iloc[current,]=t
                current+=1
    df1.index.name='name'
    df1.to_csv('basins_of_boolean/attr_temp.txt',sep=' ')

##    RONS = ["apoptosis","bid","caspase","ceramide","disc",
##            "fas","fasl","fast","gpcr","gzmb","iap","ifngt","nfkb","pdgfr","pi3k","s1p","sphk1","tpl2","tradd"]
##    df2 = df1[RONS]
##    df2.to_csv('boolnet_attractors_RONS.txt',sep=' ')
    
                    

main()
