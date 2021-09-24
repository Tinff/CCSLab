from PIL import Image,ImageFilter

im_path = r'./Cha12/valve.jpg'
im = Image.open(im_path)
im.show()
# 高斯模糊
im1 = im.filter(ImageFilter.GaussianBlur)
im1.show()
# 普通模糊
im2 = im.filter(ImageFilter.BLUR)
im2.show()
# 边缘增强
im3 = im.filter(ImageFilter.EDGE_ENHANCE)
im3.show()
# 找到边缘
im4 = im.filter(ImageFilter.FIND_EDGES)
im4.show()
# 浮雕
im5 =im.filter(ImageFilter.EMBOSS)
im5.show()
# 轮廓
im6 =im.filter(ImageFilter.CONTOUR)
im6.show()
# 锐化
im7 =im.filter(ImageFilter.SHARPEN)
im7.show()
# 平滑
im8 =im.filter(ImageFilter.SMOOTH)
im8.show()
# 细节
im9 =im.filter(ImageFilter.DETAIL)
im9.show()


