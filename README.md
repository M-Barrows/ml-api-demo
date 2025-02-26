# ML-API-DEMO
This FastAPI-based application is designed to demonstrate the core principles behind the deployment of a machine learning model as an API. This project showcases how to create an API that allows users to interact with a pre-trained machine learning model, making it accessible for various applications and users.

Key Features:
* FastAPI to enable Asynchronous requests, Data Validaton, and API documentation OOB
* UV package management for simple and fast dependency management and tracking
* Tagged versions allow you to see how a project like this progresses from hello world to hello insights
* Clear Documentation 


# Getting Started

## Docker 
```sh
docker build -t ml-demo . && docker build run -d -p 8000:8000 ml-demo
```

## Local Testing
1. Install UV (Package Manager)
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Update PATH
    ```bash
    source $HOME/.local/bin/env
    ```

3. Create and activate a virtual environment
    ```bash
    uv venv
    source .venv/bin/activate
    ```

4. Install dependencies
    ```bash
    uv pip install -r pyproject.toml
    ```

5. Run Application
    ```bash
    uvicorn run:app --reload
    ```

6. View Docs at http://127.0.0.1:8000/docs

7. Send a test request to http://127.0.0.1:8000/

8. Send a test request to http://127.0.0.1:8000/conditional-return?n1=10&?n2=15

# Main File Structure: 

```
flask_project/
│
├── app/            
│   ├── __init__.py     Needed to import routes.py as a module
│   ├── utils.py        Holds extra functions/objects used in other places
│   ├── routes.py       This is where all the API endpoints go
│
├── instance/
│   └── config.py       Sets instance specific config
│
├── config.py           Sets global config
├── run.py              Entrypoint file. This is what runs your application
├── pyproject.toml      Project Metadata
├── uv.lock             Metadata for UV to use for dependency managment
```

# Model Training

This project is not meant to teach you the art of training a model. There are a million resources out on the interwebs for that. However, I will [link you to the documentation](https://github.com/uc-python/advanced-python-datasci/blob/master/notebooks/Case%20Study%20Solutions.ipynb) for the modelling technique I will be utilizing. This is documentation from a course I took years ago at the University of Cincinnati and was very helpful in putting the ML Model Lifecycle into context for me back then. 

