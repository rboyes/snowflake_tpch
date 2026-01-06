from pathlib import Path

from dagster_dbt import DbtProject

repo_project_dir = Path(__file__).joinpath("..", "..", "..", "dbt").resolve()
packaged_project_dir = Path(__file__).joinpath("..", "dbt-project").resolve()

snowflake_tpch_project = DbtProject(
    project_dir=repo_project_dir,
    packaged_project_dir=packaged_project_dir,
)
snowflake_tpch_project.prepare_if_dev()
