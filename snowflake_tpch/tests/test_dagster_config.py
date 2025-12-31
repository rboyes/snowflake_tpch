from dagster import DefaultScheduleStatus
from snowflake_tpch.assets import CustomDagsterDbtTranslator, snowflake_tpch_dbt_assets
from snowflake_tpch.definitions import defs
from snowflake_tpch.project import repo_project_dir, snowflake_tpch_project
from snowflake_tpch.schedules import schedules


def test_translator_group_name():
    assert CustomDagsterDbtTranslator().get_group_name({}) == "snowflake_tpch"


def test_project_dir_prefers_repo_when_present():
    assert repo_project_dir.exists()
    assert snowflake_tpch_project.project_dir == repo_project_dir


def test_schedule_config():
    schedule = schedules[0]
    assert schedule.cron_schedule == "25 14 * * *"
    assert schedule.default_status == DefaultScheduleStatus.RUNNING


def test_definitions_wire_assets_and_resources():
    asset_graph = defs.resolve_asset_graph()
    asset_groups = {a.group_name for a in asset_graph.asset_nodes}
    assert "snowflake_tpch" in asset_groups
    asset_key_names = {a.key.path[-1] for a in asset_graph.asset_nodes}
    assert "fct_orders" in asset_key_names
