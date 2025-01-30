from fastapi import APIRouter, Query
from .utils import my_imported_add_function
from typing import List, Dict

router = APIRouter()

def my_add_function(l: list):
    """
    Add a list of numbers
    >>> my_add_function([1,2,3])
    6
    >>> my_add_function([-1,0,1])
    0
    """
    return sum(l)

@router.get("/")
def index():
    return {"message": "Welcome to the API!"}

@router.get("/add-numbers") 
def add_numbers(n1: int = Query(...), n2: int = Query(...)): 
    result = n1 + n2
    return {"result": result}

@router.get("/add-with-function")
def add_with_function(n1: int = Query(...), n2: int = Query(...)):
    result = my_add_function([ n1, n2])
    return {"result": result}

@router.get("/add-with-imported-function")
def add_with_function(n1: int = Query(...), n2: int = Query(...)):
    result = my_imported_add_function([ n1, n2])
    return {"result": result}

@router.get("/conditional-return")
def is_even(n: int = Query(...)):
    if n%2==0:
        return {"result": True}
    else: 
        return {"result": False}

@router.get("conditional-add")
def is_even(n1: int = Query(...), n2: int = Query(...)):
    if n1%2==0:
        return {"result": my_imported_add_function([n1,n2])}
    else: 
        return {"result": "The first number is not even."}
    
@router.post("/add-list")
def add_list(numbers: List[float]):
    return sum(numbers)

@router.post("/add-list-any")
def add_list_any(numbers: Dict):
    return sum(numbers)