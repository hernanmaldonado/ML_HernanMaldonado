import torch
import networkx as nx
import sys
import networkx as nx
import pickle



def load_data(path:str)->list:
    return open(path).read().splitlines()
     
def padding(words:list)->list:
    new_words=list()
    for word in words:
        endpadding=15-len(word)
        new_words.append("*"+word+"~"*endpadding)
    return new_words

def getallchars(words:list)->set:
    allchrs=set()
    for word in words:
        for i in list(word):
            allchrs.add(i)
    allchrs.add('*')
    allchrs.add('~')
    return sorted(allchrs)

def trackfunc(new_words):
    tracking=dict()
    for word in new_words:
        for i,j in list(zip(range(16), range(1,16))):
            poschri=str(i)+word[i]
            poschrj=str(j)+word[j]
            if not poschri in tracking:
                tracking[poschri]=dict()
            if poschrj in tracking[poschri]:
                tracking[poschri][poschrj]+=1
            else:
                tracking[poschri][poschrj]=1
    return tracking

def graphbuilder(tracking:dict)->nx.DiGraph:
    DG = nx.DiGraph()
    for k,v in tracking.items():
        total=0
        for x,y in v.items():
            total+=y
        for x,y in v.items():
            p=round(y/total,2)
            DG.add_edge(k,x,weight=p)
    return DG


def bigramgraph(new_words:list)->nx.DiGraph:
    DG=graphbuilder(trackfunc(new_words))
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
  
def main():
    try:
        fpath="./auxiliary/"
        cnt=input_capture()
        words=load_data(fpath+'names.txt')
        allchrs=getallchars(words)
        new_words=padding(words)
        #DG=bigramgraph(new_words)
        with open(fpath+'DG.gpickle', 'rb') as f:
            DG = pickle.load(f)
        g = torch.Generator().manual_seed(torch.randint(0, 10000000000, (1,)).item())
        while cnt>0:
            for i in range(cnt):
                print(makemore(allchrs,g, DG))
            cnt=input_capture()
        exit()
    except KeyboardInterrupt:
        print('Aborted manually.', file=sys.stderr)
        return 1

    except Exception as err:
        return 1

    return 0  # success

if __name__ == '__main__':
    main()