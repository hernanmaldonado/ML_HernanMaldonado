from fastapi import FastAPI, Request
from pydantic import BaseModel
from NameGen import *
import pickle

class Item(BaseModel):
    name: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello world"}

@app.get("/items/{item_id}")
def read_item(item_id:int):
    cnt=item_id
    words=load_data('names.txt')
    allchrs=getallchars(words)
    new_words=padding(words)
    #DG=bigramgraph(allchrs,new_words)
    with open('DG.gpickle', 'rb') as f:
        DG = pickle.load(f)
    g = torch.Generator().manual_seed(torch.randint(0, 10000000000, (1,)).item())
    outlist=list()
    while cnt>0:
        for i in range(cnt):
            outlist.append(makemore(allchrs,g, DG))
        cnt=0
    return {"item_id":outlist}
