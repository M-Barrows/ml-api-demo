from fastapi import APIRouter, Query, Request, Body
from .utils import my_imported_add_function
from typing import List, Dict
import pandas as pd

basic = APIRouter()

def my_add_function(l: list):
    """
    Add a list of numbers
    >>> my_add_function([1,2,3])
    6
    >>> my_add_function([-1,0,1])
    0
    """
    return sum(l)

@basic.get("/")
def index():
    return {"message": "Welcome to the API!"}

@basic.get("/add-numbers") 
def add_numbers(n1: int = Query(...), n2: int = Query(...)): 
    result = n1 + n2
    return {"result": result}

@basic.get("/add-with-function")
def add_with_function(n1: int = Query(...), n2: int = Query(...)):
    result = my_add_function([ n1, n2])
    return {"result": result}

@basic.get("/add-with-imported-function")
def add_with_function(n1: int = Query(...), n2: int = Query(...)):
    result = my_imported_add_function([ n1, n2])
    return {"result": result}

@basic.get("/conditional-return")
def is_even(n: int = Query(...)):
    if n%2==0:
        return {"result": True}
    else: 
        return {"result": False}

@basic.get("conditional-add")
def is_even(n1: int = Query(...), n2: int = Query(...)):
    if n1%2==0:
        return {"result": my_imported_add_function([n1,n2])}
    else: 
        return {"result": "The first number is not even."}
    
@basic.post("/add-list")
def add_list(numbers: List[float]):
    return sum(numbers)

@basic.post("/add-list-any")
def add_list_any(numbers: Dict):
    return sum(numbers)


model_router = APIRouter(prefix="/model")

@model_router.get("/details")
def get_model_details(request: Request):
    model_dict = {
        'steps': [name for name in request.state.model.named_steps],
        'features': request.state.model.n_features_in_
    }
    return model_dict

@model_router.post("/predict")
async def predict(request: Request, input_data: list = Body(...)):
    model = request.state.model
    input_data = pd.DataFrame(input_data)
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}