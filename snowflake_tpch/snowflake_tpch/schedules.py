"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import snowflake_tpch_dbt_assets

schedules = [
     build_schedule_from_dbt_selection(
         [snowflake_tpch_dbt_assets],
         job_name="materialize_fct_orders",
         cron_schedule="0 13 * * *",
         dbt_select="+fct_orders",
     ),
]

