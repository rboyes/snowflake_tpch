select
    *
from
    {{ ref('fct_orders') }}
where
    gross_item_discounted_amount < 0.0
    
