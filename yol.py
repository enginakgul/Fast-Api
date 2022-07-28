

from fastapi import FastAPI, Path,Query


app = FastAPI()

@app.get("/items/{items_id}")
async def read_items_defination(q : str, item_id: int = Path(...,title= "Engin have paths"),):
    results = {"item_id":item_id }
    if q:
        results.update({"q": q})
    return results
    
    
    