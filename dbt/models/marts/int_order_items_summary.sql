select
    order_key,
    sum(extended_price) as gross_item_sales_amount,
    sum(discounted_price) as gross_item_discounted_amount
from {{ ref('int_order_items') }}
group by order_key