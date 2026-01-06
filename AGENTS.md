# Agent Notes

Basic guidance for assistants working in this repository.

## Project Snapshot

- Purpose: Dagster + dbt pipeline for TPCH data in Snowflake.
- Key dirs: `src/` (python package), `dbt/` (dbt project).
- Entry points: `src/snowflake_tpch/definitions.py`, `src/snowflake_tpch/project.py`.

## Local Development

- Sync venv: `uv sync --extra dev`
- Activate: `source .venv/bin/activate`
- Set env vars:
  - `DBT_PROJECT_DIR=./dbt`
  - `DBT_PROFILES_DIR=./dbt`
  - `SNOWFLAKE_ACCOUNT=XXXXXX-YYYYYY`
  - `SNOWFLAKE_USER=rich`
  - `SNOWFLAKE_PASSWORD=XXXX`
- Scaffold Dagster/dbt project:
  - `dagster-dbt project prepare-and-package --file src/snowflake_tpch/project.py`
- Run Dagster:
  - `dagster dev -m snowflake_tpch.definitions`

## Tests

- `pytest tests`

## Notes

- Deployment uses GitHub Actions workflow at `.github/workflows/deploy.yml`.
