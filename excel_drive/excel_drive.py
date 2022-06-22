import openpyxl
# 获取excel
excel=openpyxl.load_workbook('../data/demo.xlsx')
# 指定sheet页
sheet=excel['Sheet1']
#获取单元格与内容
# 每一行作为一个元组
# for values in sheet.values:
#     print(values)

# 如果我要一列

for values in sheet.values:
    print(values[0])