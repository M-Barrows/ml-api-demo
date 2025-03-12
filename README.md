# ML-API-DEMO
This FastAPI-based application is designed to demonstrate the core principles behind the deployment of a machine learning model as an API. This project showcases how to create an API that allows users to interact with a pre-trained machine learning model, making it accessible for various applications and users.

Key Features:
* FastAPI to enable Asynchronous requests, Data Validaton, and API documentation OOB
* UV package management for simple and fast dependency management and tracking
* Tagged versions allow you to see how a project like this progresses from hello world to hello insights
* Clear Documentation 


# Getting Started

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

9. Send a test request to http://127.0.0.1:8000/model/predict
    ```sh
    curl -X POST http://localhost:8000/model/predict -H "Content-Type: application/json" -d @model/data/X_test.json
    ```

# Main File Structure: 

```
ml-api-demo/
│
├── app/            
│   ├── __init__.py         Needed to import routes.py as a module
│   ├── utils.py            Holds extra functions/objects used in other places
│   ├── routes.py           This is where all the API endpoints go
│
├── instance/
│   └── config.py           Sets instance specific config
│
├── model/
│   └── data
│   │   ├── ames.csv        Data used to train inference model
│   │   └── X_test.json     Test data used to validate the `/model/prediction` endpoint
│   ├── train_model.ipynb   Notebook used to train the inference model 
│   └── model.joblib        model used for inference
│
├── Dockerfile              Instructions for building the docker container
├── config.py               Sets global config
├── run.py                  Entrypoint file. This is what runs your application
├── pyproject.toml          Project Metadata
├── uv.lock                 Metadata for UV to use for dependency managment
```