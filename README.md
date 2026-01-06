## Dagster/DBT TPCH Snowflake ❄️ Project 

[![Serverless Prod Deployment](https://github.com/rboyes/snowflake_tpch/actions/workflows/deploy.yml/badge.svg)](https://github.com/rboyes/snowflake_tpch/actions/workflows/deploy.yml)

Basic project to ingest tpch data from snowflake and create a data mart using Dagster & DBT. See: https://github.com/rboyes/snowflake_tpch 


### Pre-requisites

- A working snowflake instance with admin access to do the following:
  ```sql
  use role accountadmin;
  create warehouse if not exists dbt_wh with warehouse_size='x-small';
  create database if not exists dbt_db;
  create role if not exists dbt_role;
  grant usage on warehouse dbt_wh to role dbt_role;
  create user if not exists dbt_user
    rsa_public_key = 'REPLACE_WITH_RSA_PUBLIC_KEY'
    default_role = dbt_role
    default_warehouse = dbt_wh;
  grant role dbt_role to user dbt_user;
  grant all on database dbt_db to role dbt_role;
  ```
- Install uv using their [official documentation](https://docs.astral.sh/uv/getting-started/installation/)
- Synchronise the virtual environment: 
  ```bash
  uv sync --extra dev
  ```
- Use the virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Create the following environment variables:
  ```bash
  export SNOWFLAKE_ACCOUNT=XXXXXX-YYYYYY
  export SNOWFLAKE_USER=dbt_user
  export SNOWFLAKE_PRIVATE_KEY=$(cat /path/to/rsa_key.private)
  ```

### Running Dagster locally

- Scaffold the project:
  ```bash
  dagster-dbt project prepare-and-package --file src/snowflake_tpch/project.py
  ```
- Run the webserver:
  ```bash
  dagster dev -m snowflake_tpch.definitions
  ```

### Running the unit tests

- Synchronise the virtual environment: 
  ```bash
  uv sync --extra dev
  ```
- Use the virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Run the unit tests:
  ```bash
  pytest tests
  ```

### Dagster Cloud

See github actions under https://github.com/rboyes/snowflake_tpch/actions for deployment to Dagster cloud, also see [deploy.yml](.github/workflows/deploy.yml).


### Running DBT Locally

You may wish to run DBT locally, which will execute the DAG on Snowflake directly:
```bash
uv sync --extra dev
source ./.venv/bin/activate
cd ./dbt
dbt deps
dbt build
```
