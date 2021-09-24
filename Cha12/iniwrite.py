import configparser #处理ini文件
iniFileName = 'iniFileName.ini'
config = configparser.ConfigParser()
config.read(iniFileName, encoding='utf-8')
list = config.sections()    # 获取到配置文件中所有分组名称
sectionName = 'config'
if  sectionName not in list: # 如果分组不存在
    config.add_section(sectionName)   # 增加section
config.set(sectionName,"Credits",str(90))
with open(iniFileName, "w+") as f:
    config.write(f)
    f.close()
