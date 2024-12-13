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

# Main File Structure: 

```
flask_project/
│
├── app/            
│   ├── __init__.py     Needed to import routes.py as a module
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