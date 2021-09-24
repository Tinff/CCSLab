from PIL import Image

im_path = r'./Cha12/valve.jpg'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)
im.show()

im1 = im.rotate(45) #逆时针
im1.show()

im2 = im.rotate(-45) #顺时针
im2.show()


