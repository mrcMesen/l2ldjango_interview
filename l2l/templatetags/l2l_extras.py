from datetime import datetime

from django import template

from common.utils.dates import IS0_FORMAT, get_format_date

register = template.Library()


@register.filter(name="format_date_time")
def format_date_time(value: str | datetime) -> str:
    if not value:
        return "There is no date."

    if isinstance(value, (datetime)):
        return get_format_date(value)

    if isinstance(value, str):
        return get_format_date(datetime.strptime(value, IS0_FORMAT))

    return "Opps the format date is not valid."
