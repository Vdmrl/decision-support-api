# Decision support api

## Description

The Decision Support API module is designed for a startup acceleration platform, assisting in ranking help measures for the current project using sBERT embeddings and cosine distance.

### Main features:
+ Asynchronous API with swagger documentation 
+ Interaction with the database using SQLalchemy and async driver aiomysql
+ Migrations using Alembic
+ Module for converting data from a database into text with ORM
+ Module for text preprocessing
+ Module for text ranking using sBERT embedding and cosine distance
+ Autotests for API and database with pytest
+ Fully containerized application

## Preparing environment and docker

+ Change .env data to your development database configuration

+ Change .env.prod data to your production database configuration

+ Replace docker-compose db service with a real database

## Running server

### Using Docker compose

+ Run services

    ```shell
    docker-compose up
    ```

+ Bring services down

    ```shell
    docker-compose down
    ```

go to the local host address: http://127.0.0.1:8000/

### Using python virtual machine

1. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it.

3. Go to the folder with main.py

    ```shell
    cd backend
    ```

3. Install requirements:

    ```shell
    python3 -m pip install --user -r requirements.txt
    ```

4. Run server using gunicorn:

    ```shell
    python uvicorn main:app --reload
    ```

go to the local host address: http://127.0.0.1:8000/
