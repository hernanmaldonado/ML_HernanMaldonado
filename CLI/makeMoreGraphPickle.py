import torch
import networkx as nx
import sys
import pickle
from nameGen import * 


 
def main():
    try:
        fpath="./auxiliary/"
        cnt=input_capture()
        words=load_data(fpath+'names.txt')
        size=len(max(words,key=len))+1
        allchrs=getallchars(words)
        new_words=padding(words,size)
        #DG=bigramgraph(new_words,size)
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