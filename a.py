
from fastapi import FastAPI, Query
from typing import Union



app = FastAPI()
@app.get("/items")
async def read_items(q : Union[str,None] = Query (None ,min_length= 3,max_length = 10,title= "This is a sample query string",alias= 'Item-query')):
    results = {"items":[{"item_id": "Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results
    
@app.get("/items_hidden")
async def read_itemas_hidden(hidden_query: Union[str, None] = Query (None, include_in_schema=True)):
    results1 = {"items":[{"Hidden_query":"goo"},{"hidden_query": "foo"}] }  
    if hidden_query :
        results1.update({"hiddden_query": hidden_query})
    return {"hidden_query":"Not Found"}