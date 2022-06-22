'''
    Excel读取
'''

import openpyxl
import sys

sys.path.append('..')
from Key.web_keys import Key
# 获取单元格信息


def mess_Unit(value):
    data = {}
    str_Temp = value.split(';')
    for tmp in str_Temp:
        str = tmp.split('=', 1)
        data[str[0]] = str[1]
    return data


excel = openpyxl.load_workbook('../data/demo.xlsx')
# sheet=excel['Sheet2']
for name in excel.sheetnames:
    sheet = excel[name]
    for values in sheet.values:
        if type(values[0]) is not int:
            continue
        print(f'正在执行操作步骤{values[0]}:{values[1]}:{values[3]}')
        if values[2] != None:
            data = mess_Unit(values[2])
        if values[1] == 'open_browser':
            key = Key(**data)
        elif 'assert' in values[1]:  #因为不同断言有不同断言方法，所以用in
            status = getattr(key, values[1])(**data)
            if status:
                pass
            else:
                pass
        else:
            if data is not None:
                getattr(key, values[1])(**data)
            else:
                getattr(key, excel[1])()
