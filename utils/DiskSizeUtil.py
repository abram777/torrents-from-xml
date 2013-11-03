import math

convert_bytes_to_kilobytes = lambda bts: float(bts) / 1024
convert_bytes_to_megabytes = lambda bts: convert_bytes_to_kilobytes(bts) / 1024
convert_bytes_to_gigabytes = lambda bts: convert_bytes_to_megabytes(bts) / 1024


format_kilobytes = lambda bts: str(math.floor(float(bts)))[0:4]
format_megabytes = lambda bts: str(convert_bytes_to_megabytes(bts))[0:6]
format_gigabytes = lambda bts: str(convert_bytes_to_gigabytes(bts))[0:4]


def get_storage_type(bts):
    bts = int(bts)
    if bts < 1024:
        return {"long_name": "bts", "abbr": "b"}
    elif bts < (1024 * 1024):
        return {"long_name": "Kilobytes", "abbr": "kb"}
    elif bts < (1024 * 1024 * 1024):
        return {"long_name": "Megabytes", "abbr": "mb"}
    elif bts < (1024 * 1024 * 1024 * 1024):
        return {"long_name": "Gigabytes", "abbr": "gb"}
    else:
        return {"long_name": "", "abbr": ""}


def format_bytes(bts):
    storage_type = get_storage_type(bts)
    return {
        "b": bts,
        "kb": format_kilobytes(bts),
        "mb": format_megabytes(bts),
        "gb": format_gigabytes(bts)
    }.get(storage_type["abbr"], 0)