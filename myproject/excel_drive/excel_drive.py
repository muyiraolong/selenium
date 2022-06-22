import openpyxl
import sys

sys.path.append("..")
from web_key.key import Key


def parse_excel(value):
    if not value:
        return None
    data = {}
    tem_str = value.split(";")
    for tem in tem_str:
        str = tem.split(":", 1)
        data[str[0]] = str[1]
    return data


excel = openpyxl.load_workbook('../excel_data/drive_info.xlsx')
for name in excel.sheetnames:
    print(f"是表{name}")
    sheet = excel[name]
    for values in sheet.values:
        if not isinstance(values[0], int):
            continue
        print(f"正在执行{values[0]}:{values[3]}")
        data = parse_excel(values[2])
        if values[1] == 'open_browser':
            Key = Key(**data)
        else:
            if data:
                getattr(Key, values[1])(**data)
            else:
                getattr(Key, values[1])()
