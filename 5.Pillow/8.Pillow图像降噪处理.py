from PIL import Image,ImageFilter

im = Image.open("C:/Users/tank/Desktop/大熊猫.png")

# 模糊处理
im_blur = im.filter(ImageFilter.BLUR)
im_blur.show()
im_blur.save("C:/Users/tank/Desktop/模糊.png")

# 轮廓图
im2 = im.filter(ImageFilter.CONTOUR)
im2.show()
im2.save("C:/Users/tank/Desktop/轮廓图.png")

# 边缘检测
im3 = im.filter(ImageFilter.FIND_EDGES)
im3.show()
im3.save("C:/Users/tank/Desktop/边缘检测.png")

# 浮雕图
im4 = im.filter(ImageFilter.EMBOSS)
im4.show()
im4.save("C:/Users/tank/Desktop/浮雕图.png")

# 平滑图像
im5 = im.filter(ImageFilter.SMOOTH)
im5.show()
im5.save("C:/Users/tank/Desktop/平滑图.png")

# 细节滤波
im6 = im.filter(ImageFilter.DETAIL)
im6.show()
im6.save("C:/Users/tank/Desktop/细节处理.png")