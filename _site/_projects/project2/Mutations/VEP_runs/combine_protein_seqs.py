import re
def main():
    ref=open('ref1.fa').read()
    mut=open('mut1.fa').read()
    mut=re.sub('..?:', ':', mut)
    ref1=ref.split('\n')
    mut1=mut.split('\n')
    complete=[]
    for lineref in ref1: 
        if '>' in lineref:
            seqref=ref1[ref1.index(lineref)+1]
            #print(lineref)
            for linemut in mut1:
                thing=linemut.split(':')
                ID=thing[0]
                #print('$$$$$')
                if '>' in linemut:
                    seqmut=mut1[mut1.index(linemut)+1]
                if lineref==ID:
                    #print(seqref!=seqmut)
                    if seqref!=seqmut:
                        #print(lineref+'\n')
                        #print(linemut+'\n')
                        #print(seqref+'\n')
                        #print(seqmut+'\n')
                        
                        complete.append(lineref+'_reference')
                        complete.append(seqref)
                        complete.append(linemut)
                        complete.append(seqmut)
    with open('complete.fa', 'w') as f:
        for item in complete:
            f.write("%s\n" % item)
main()
