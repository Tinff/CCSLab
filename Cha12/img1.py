from PIL import Image

im_path = r'F:\OneDrive\1-教学\自动化17级《计算机控制系统》\计算机控制系统实验指导书\CCSlab\Lab8\valve.jpg'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

im.save(r'C:\Users\ZYoffice\Desktop\valve2.jpg')
im.show()


