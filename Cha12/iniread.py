import configparser #处理ini文件

iniFileName = 'iniFileName.ini'

cred = 0
config = configparser.ConfigParser()
config.read(iniFileName, encoding='utf-8')
sectionName = 'config'
list = config.sections()    # 获取到配置文件中所有分组名称
if sectionName in list: # 如果分组存在
    cred = config.getfloat(sectionName, "Credits")
print(cred)