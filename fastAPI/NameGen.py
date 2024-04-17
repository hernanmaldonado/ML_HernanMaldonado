import torch
import networkx as nx
import sys

def load_data(path:str)->list:
    return open(path).read().splitlines()
     

def getallchars(words:list)->set:
    allchrs=set()
    for word in words:
        for i in list(word):
            allchrs.add(i)
    allchrs.add('*')
    allchrs.add('~')
    return sorted(allchrs)

def padding(words:list)->list:
    new_words=list()
    for word in words:
        endpadding=15-len(word)
        new_words.append("*"+word+"~"*endpadding)
    return new_words

def bigramgraph(allchrs:set,new_words:list)->nx.DiGraph:
    DG = nx.DiGraph()
    for i,j in list(zip(range(16), range(1,16))):
        for bchr in allchrs:
            for achr in allchrs:
                cnt=0
                cntb=0
                for word in new_words:
                    if word[i]==bchr:
                        cntb+=1
                        if word[j]==achr:
                            cnt+=1   
                start=str(i)+bchr
                end=str(j)+achr
                if cntb==0:
                    p=0
                else:
                    p=round(cnt/cntb,2)
                if p>0:
                    DG.add_edge(start,end,weight=p)
    return DG
    


def zerodict(mylist:list)->dict:
    mydict=dict()
    for key in mylist:
        mydict[key]=0.0
    return mydict

def makemore(allchrs,g, DG):
        start='0*'
        rnd=0
        name=""
        out=list()
        while not start[-1]=='~':   
            probdict=zerodict(allchrs)
            for s in list(DG.successors(start)):
                probdict[s[-1]]=DG.get_edge_data(start,s)['weight']
            #print(probdict)
            #print(list(probdict.values()))
            p=torch.tensor(list(probdict.values()),dtype=float)
            start='1~'
            ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
            rnd+=1
            start=str(rnd)+allchrs[ix]
            if not allchrs[ix]=='~':
                out.append(allchrs[ix])
        return ''.join(out)

def input_capture()->int:
    args = input("Enter the number of names you want to generate: ")
    if args is None:
        return 1
    elif args.isnumeric():
        cnt=int(args)
        return cnt
    else:
        return 0