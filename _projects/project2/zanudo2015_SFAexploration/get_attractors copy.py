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
    
    df1=pd.DataFrame(columns=cols)

    with open('basins_of_boolean/temp.txt','r') as f,open('basins_of_boolean/result_temp.txt','w') as fout:
        copy = False
        ls = []
        for line in f:
            if line.strip() == "|--<-----------------------------------------------------------|":
                copy = True
                continue
            elif line.strip() == "|-->-----------------------------------------------------------|":
                copy = False
                continue
            elif copy:
                if line.strip() != 'V                                                              |':
                    fout.write(','.join(line.strip().split(' ')[0]))
                

main()
