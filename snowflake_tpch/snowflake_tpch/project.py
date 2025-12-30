from pathlib import Path

from dagster_dbt import DbtProject

snowflake_tpch_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
snowflake_tpch_project.prepare_if_dev()

