Basic project to ingest tpch data from snowflake and create a data mart.

You will need a working dbt command line with snowflake. I set that up in a virtual environment in python:

```bash
python -m venv .venv --prompt dbt
source .venv/bin/activate
pip install -r requirements.txt

Create a profile called snowflake_tpch in `~/.dbt/profiles.yml` that grants you access to snowflake.

Run the following commands to test it out:
- dbt deps
- dbt compile
- dbt debug
- dbt run
- dbt test
- dbt build
- dbt source freshness
