from PIL import Image

im_path = r'./Cha12/valve.jpg'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)
im.show()

cropedIm = im.crop((0, 0, width//2, height//2)) #//整除
cropedIm.show()



