## Dagster/DBT TPCH Snowflake Project

Basic project to ingest tpch data from snowflake and create a data mart using Dagster & DBT. See: https://github.com/rboyes/snowflake_tpch

Pre-requisites:
- A working snowflake instance with admin access with the following:
  ```sql
  use role accountadmin;
  create warehouse if not exists dbt_wh with warehouse_size='x-small';
  create database if not exists dbt_db;
  create role if not exists dbt_role;
  grant usage on warehouse dbt_wh to role dbt_role;
  grant role dbt_role to user rich;
  grant all on database dbt_db to role dbt_role;
  use role dbt_role;
  ```
- Install uv using their [official documentation](https://docs.astral.sh/uv/getting-started/installation/)

Assumes you already have a snowflake instance.

To run locally, do the following in the project root:

- Create a virtual environment: `uv venv`
- Use the virtual environment: `source .venv/bin/activate`
- Install dependencies: `uv pip install -e "snowflake_tpch[dev]"`
- Create the following environment variables:
  ```bash
  export DBT_PROJECT_DIR=./dbt
  export DBT_PROFILES_DIR=./dbt
  export SNOWFLAKE_ACCOUNT=XXXXXX-YYYYYY
  export SNOWFLAKE_USER=rich
  export SNOWFLAKE_PASSWORD=XXXX
  ```
- Scaffold the project:
  ```bash
  dagster-dbt project prepare-and-package --file snowflake_tpch/snowflake_tpch/project.py
  ```
- Run the webserver: `dagster dev -m snowflake_tpch.definitions`

### Dagster Cloud

See github actions under https://github.com/rboyes/snowflake_tpch for deployment to Dagster cloud.