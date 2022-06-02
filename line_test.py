import re
import json

# 驗證key有沒有缺1
def is_valid(data):
    # check type of data
    if not isinstance(data, dict):
        return False

    # check key
    valid_keys = ["ad_network", "date", "app_name", "unit_id", "request", "revenue", "imp"]
    data_keys = [key for key in data]
    
    if valid_keys != data_keys:
        return False

    # check value type
    valid_value_type = {key: str for key in valid_keys}
    for key, value in data.items():
        if not isinstance(value, valid_value_type[key]):
            return False

    # check value format
    # ad_network
    valid_value_format = {
        "ad_network": r"^[A-Z]+$",
        "date": r"^(202[0-2]|20[01]\d|1[\d]{3})-(0[1-9]|1[0-2])-([0][1-9]|[12][\d]|3[01])$",
        "app_name": r"^LINETV$",
        "unit_id": r"^[\d]+$",
        "request": r"^[1-5][\d]{2}$",
        "revenue": r"^-?\d+.\d+$|^-?\d+$",
        "imp": r"^\d+$"
    }
    for key, value in data.items():
        p = re.compile(valid_value_format[key])
        if not p.match(value):
            print(key)
            return False

    return True