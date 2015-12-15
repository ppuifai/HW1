flag=inp=0
while flag==0:
    print 'Enter input :'
    inp=raw_input()
    inp=map(int,(inp.split()))
    if max(inp)<=1000 and len(inp)<=100:
        flag=1
tab=[' ']*50
for i in range(0,len(inp)):
    tab[(int(inp[i])%50)]+=str(inp[i])+'  '
for j in range(0,50):
    print j,':',tab[j]
