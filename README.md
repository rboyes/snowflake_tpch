Basic project to ingest tpch data from snowflake and create a data mart using Dagster & DBT. See: https://github.com/rboyes/snowflake_tpch

Assumes you already have a snowflake instance.

To run locally, do the following in the project root:

- Install uv using their [official documentation](https://docs.astral.sh/uv/getting-started/installation/)
- Create a virtual environment:
  - `uv venv`
- Use the virtual environment:
  - `source .venv/bin/activate`
- Install dependencies:
  - `uv pip install -e "snowflake_tpch[dev]"`
- Create the following environment variables:
  - `export DBT_PROJECT_DIR=./dbt`
  - `export DBT_PROFILES_DIR=./dbt`
  - `export SNOWFLAKE_ACCOUNT=XXXXXX-YYYYYY`
  - `export SNOWFLAKE_USER=rich`
  - `export SNOWFLAKE_PASSWORD=XXXX`
- Scaffold the project:
  - `dagster-dbt project prepare-and-package --file snowflake_tpch/snowflake_tpch/project.py`
- Run the webserver:
  - `dagster dev -m snowflake_tpch.definitions`