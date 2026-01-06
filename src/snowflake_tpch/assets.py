from typing import Any, Mapping
from dagster import AssetExecutionContext
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, DbtProject, dbt_assets

from .project import snowflake_tpch_project

dbt_project = DbtProject(snowflake_tpch_project.project_dir)


class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> str | None:
        return "snowflake_tpch"


@dbt_assets(
    manifest=snowflake_tpch_project.manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(),
)
def snowflake_tpch_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
