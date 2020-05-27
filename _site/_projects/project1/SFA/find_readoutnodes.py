def main():

    res=open('attractor_10A.txt').read().split('\n')
    sen=open('attractor_231.txt').read().split('\n')

    resd = {}
    send={}
    for line in res:
        #print(line)
        (key, val) = line.split()
        resd[key] = float(val)

    for line in sen:
        (key, val)=line.split()
        send[key]=float(val)

    for key,val1 in resd.items():
        val2=send.get(key)
        if val1<0 and val2>0:
            print (key+'\t'+str(val1)+'\t'+str(val2))
        if val1>0 and val2<0:
            print (key+'\t'+str(val1)+'\t'+str(val2))
main()
            
