{% macro discounted_price(extended_price, discount_percentage, scale=2) %}
    round({{ extended_price }} * (1 - {{ discount_percentage }}), {{ scale }})
{% endmacro %}