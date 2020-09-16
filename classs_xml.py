#7类
import xml.etree.ElementTree as ET
import os

xmlfilepath = 'new_xml/'
# xmlfilepath = 'data/test'
# xmlfilepath = 'data/Annotations'

total_xml = os.listdir(xmlfilepath)
lists = []  
haozao = 0
aoxian = 0
heiban = 0
liekou = 0
niaozhuo = 0
gantiao = 0
lanzao = 0
shuzao = 0
for i in total_xml:
    i = 'new_xml/' + i
    tree = ET.parse(i)
    root = tree.getroot()
    for names in root.findall("object"):
        name = names.find('name').text
        if name == "4":
            haozao += 1
        elif name == "1":
            heiban += 1
        elif name == "5":
            niaozhuo += 1
        elif name == "0":
            aoxian += 1
        elif name == "2":
            gantiao += 1
        elif name == "6":
            lanzao += 1
        elif name == "7":
            shuzao += 1
        else:
            liekou += 1
zs = haozao + gantiao + heiban + liekou + aoxian + niaozhuo + lanzao + shuzao
print("统计数据集各类数量如下：好枣-%s-,干条-%s-,黑斑-%s-,裂口-%s-,凹陷-%s-,鸟琢-%s-,烂枣-%s-,竖枣-%s-,总数-%s-" % (haozao, gantiao, heiban, liekou, aoxian, niaozhuo, lanzao, shuzao, zs))

# 统计数据集各类数量如下：好枣-26371-,干条-12817-,黑斑-17415-,裂口-15823-,凹陷-11100-,鸟琢-9789-,烂枣-8470-,竖枣-2483-,总数-104268-
# 统计数据集各类数量如下：好枣-2924-,干条-1336-,黑斑-1718-,裂口-1674-,凹陷-1095-,鸟琢-728-,烂枣-738-,竖枣-222-,总数-10435-

# 6类
# import xml.etree.ElementTree as ET
# import os
#
# xmlfilepath = 'new_xml/'
# total_xml = os.listdir(xmlfilepath)
# lists = []
# haozao = 0
# aoxian = 0
# heiban = 0
# liekou = 0
# niaozhuo = 0
# gantiao = 0
# for i in total_xml:
#     i = 'new_xml/' + i
#     tree = ET.parse(i)
#     root = tree.getroot()
#     for names in root.findall("object"):
#         name = names.find('name').text
#         if name == "HaoZao":
#             haozao += 1
#         elif name == "HeiBan":
#             heiban += 1
#         elif name == "NiaoZhuo":
#             niaozhuo += 1
#         elif name == "AoXian":
#             aoxian += 1
#         elif name == "GanTiao":
#             gantiao += 1
#         else:
#             liekou += 1
# zs = haozao+ gantiao+ heiban+ liekou+ aoxian+ niaozhuo
# print("统计数据集各类数量如下：好枣-%s-,干条-%s-,黑斑-%s-,裂口-%s-,凹陷-%s-,鸟琢-%s-,总数-%s-" % (haozao, gantiao, heiban, liekou, aoxian, niaozhuo, zs))