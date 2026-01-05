# Agent Notes

Basic guidance for assistants working in this repository.

## Project Snapshot

- Purpose: Dagster + dbt pipeline for TPCH data in Snowflake.
- Key dirs: `snowflake_tpch/` (python package), `dbt/` (dbt project).
- Entry points: `snowflake_tpch/definitions.py`, `snowflake_tpch/snowflake_tpch/project.py`.

## Local Development

- Sync venv: `uv sync --project snowflake_tpch --extra dev`
- Activate: `source snowflake_tpch/.venv/bin/activate`
- Set env vars:
  - `DBT_PROJECT_DIR=./dbt`
  - `DBT_PROFILES_DIR=./dbt`
  - `SNOWFLAKE_ACCOUNT=XXXXXX-YYYYYY`
  - `SNOWFLAKE_USER=rich`
  - `SNOWFLAKE_PASSWORD=XXXX`
- Scaffold Dagster/dbt project:
  - `dagster-dbt project prepare-and-package --file snowflake_tpch/snowflake_tpch/project.py`
- Run Dagster:
  - `dagster dev -m snowflake_tpch.definitions`

## Tests

- `pytest snowflake_tpch/tests`

## Notes

- Deployment uses GitHub Actions workflow at `.github/workflows/deploy.yml`.
