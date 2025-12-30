"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster import DefaultScheduleStatus

from dagster_dbt import build_schedule_from_dbt_selection

from .assets import snowflake_tpch_dbt_assets

schedules = [
     build_schedule_from_dbt_selection(
         [snowflake_tpch_dbt_assets],
         job_name="materialize_fct_orders",
         cron_schedule="15 13 * * *",
         default_status=DefaultScheduleStatus.RUNNING,
         dbt_select="+fct_orders",
     ),
]

