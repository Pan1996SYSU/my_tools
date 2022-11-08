import pandas as pd
import xlwings as xw

file_path = r"D:\桌面\sth\公商福档案封面.xlsx"
output_path = r'D:\桌面\sth\封面.xlsx'

excel_data = pd.read_excel(file_path, sheet_name='Sheet3', header=0)
excel_keys = list(excel_data.keys())
number_list = list(excel_data['编号'])

excel = xw.App(visible=False, add_book=False)
workbook = excel.books.add()
sht = workbook.sheets[0]
const_num = 23

for i in range(len(number_list)):
    the_id = excel_data['编号'][i]
    name = excel_data['店名'][i]
    add = excel_data['地址'][i]
    phone = excel_data['电话'][i]
    time = excel_data['通气时间'][i]
    the_type = excel_data['性质'][i]
    num = excel_data['档案编号'][i]
    gas_type = excel_data['类别'][i]

    sht[i * const_num + 0, 0].value = '档案编号：'
    sht[i * const_num + 0, 2].value = num

    sht[i * const_num + 1, 0].value = '用户编号：'
    sht[i * const_num + 1, 2].value = the_id
    sht[i * const_num + 1, 4].value = '用气性质：'
    sht[i * const_num + 1, 5].value = the_type
    sht[i * const_num + 1, 7].value = '联系电话：'
    sht[i * const_num + 1, 8].value = phone

    sht[i * const_num + 2, 0].value = '用户名称：'
    sht[i * const_num + 2, 2].value = name
    sht[i * const_num + 2, 4].value = '地  址：'
    sht[i * const_num + 2, 5].value = add

    sht[i * const_num + 3, 0].value = '报装时间：'
    sht[i * const_num + 3, 4].value = '通气时间：'
    sht[i * const_num + 3, 5].value = time
    sht[i * const_num + 3, 7].value = gas_type

    sht[i * const_num + 4, 0].value = '序号'
    sht[i * const_num + 4, 2].value = '名称'
    sht[i * const_num + 4, 3].value = '归档√'
    sht[i * const_num + 4, 5].value = '序号'
    sht[i * const_num + 4, 7].value = '名称'
    sht[i * const_num + 4, 8].value = '归档√'
    sht[i * const_num + 5, 0].value = '1'
    sht[i * const_num + 5, 2].value = '用户基本信息'
    sht[i * const_num + 5, 5].value = '13'
    sht[i * const_num + 5, 6].value = '用气情况'
    sht[i * const_num + 5, 7].value = '日均用气量'
    sht[i * const_num + 6, 0].value = '2'
    sht[i * const_num + 6, 1].value = '工程建设资料'
    sht[i * const_num + 6, 2].value = '现场勘察图'
    sht[i * const_num + 6, 5].value = '14'
    sht[i * const_num + 6, 7].value = '用气压力'
    sht[i * const_num + 7, 0].value = '3'
    sht[i * const_num + 7, 2].value = '设计图'
    sht[i * const_num + 7, 5].value = '15'
    sht[i * const_num + 7, 7].value = '抄表情况'
    sht[i * const_num + 8, 0].value = '4'
    sht[i * const_num + 8, 2].value = '施工图'
    sht[i * const_num + 8, 5].value = '16'
    sht[i * const_num + 8, 6].value = '隐患情况'
    sht[i * const_num + 8, 7].value = '安检记录单'
    sht[i * const_num + 9, 0].value = '5'
    sht[i * const_num + 9, 2].value = '施工验收资料'
    sht[i * const_num + 9, 5].value = '17'
    sht[i * const_num + 9, 7].value = '隐患通知单'
    sht[i * const_num + 10, 0].value = '6'
    sht[i * const_num + 10, 1].value = '合同签订情况'
    sht[i * const_num + 10, 2].value = '报装合同'
    sht[i * const_num + 10, 5].value = '18'
    sht[i * const_num + 10, 7].value = '隐患整改跟进记录'
    sht[i * const_num + 11, 0].value = '7'
    sht[i * const_num + 11, 2].value = '用气协议'
    sht[i * const_num + 11, 5].value = '19'
    sht[i * const_num + 11, 7].value = '维修记录'
    sht[i * const_num + 12, 0].value = '8'
    sht[i * const_num + 12, 2].value = '相关补充协议'
    sht[i * const_num + 12, 5].value = '20'
    sht[i * const_num + 13, 0].value = '9'
    sht[i * const_num + 13, 2].value = '流量计型号'
    sht[i * const_num + 13, 5].value = '21'
    sht[i * const_num + 14, 0].value = '10'
    sht[i * const_num + 14, 2].value = '调压器型号'
    sht[i * const_num + 14, 5].value = '22'
    sht[i * const_num + 15, 0].value = '11'
    sht[i * const_num + 15, 2].value = '燃气燃烧设备情况'
    sht[i * const_num + 15, 5].value = '23'
    sht[i * const_num + 15, 0].value = '12'
    sht[i * const_num + 15, 2].value = '燃气燃烧设备情况'
    sht[i * const_num + 15, 5].value = '燃气泄漏报警装置'
    sht[i * const_num + 17, 0].value = '流量计型号：'
    sht[i * const_num + 19, 0].value = '燃气泄漏报警装置'

    # 边框
    col_dict = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I']
    for j in range(6, 19):
        for col in col_dict:
            for style in range(7, 11):
                sht.range(f'{col}{i * const_num + j}').api.Borders(
                    style).LineStyle = 1
                sht.range(f'{col}{i * const_num + j}').api.Borders(
                    style).Weight = 2
    col_dict = ['C', 'D', 'F', 'G', 'H', 'I']
    for j in range(2, 5):
        for col in col_dict:
            if j == 2 and col == 'H':
                continue
            sht.range(f'{col}{i * const_num + j}').api.Borders(9).LineStyle = 1
            sht.range(f'{col}{i * const_num + j}').api.Borders(9).Weight = 2

    # 字体
    sht.range(f'A{i * const_num + 1}').api.Font.Size = 12
    sht.range(f'A{i * const_num + 1}').api.Font.Bold = True
    col_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for j in range(2, 19):
        for col in col_dict:
            sht.range(f'{col}{i * const_num + j}').api.Font.Size = 10
    sht.range(f'A{i * const_num + 20}').api.Font.Size = 11
    sht.range(f'A{i * const_num + 20}').api.Font.Bold = True
    sht.range(f'A{i * const_num + 22}').api.Font.Size = 11
    sht.range(f'A{i * const_num + 222}').api.Font.Bold = True

    if i == 0:
        # 单元格宽
        col_dict = {
            'A': 5,
            'B': 4.88,
            'C': 16.75,
            'D': 12.38,
            'E': 10.5,
            'F': 5,
            'G': 4.88,
            'H': 16,
            'I': 12.38
        }
        for col in col_dict.keys():
            sht.range(f'{col}{i * const_num + 1}').column_width = col_dict[col]
    # 单元格高
    for j in range(1, 5):
        sht.range(f'A{i * const_num + j}').row_height = 27.75
    sht.range(f'A{i * const_num + 6}').row_height = 27
    for j in range(7, 19):
        sht.range(f'A{i * const_num + j}').row_height = 13.5

workbook.save(output_path)
workbook.close()
