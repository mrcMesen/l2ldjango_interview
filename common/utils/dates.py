from datetime import datetime

IS0_FORMAT = "%Y-%m-%dT%H:%M:%S"

PRINT_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_format_date(input_date: datetime) -> str:
    return input_date.strftime(PRINT_FORMAT)
