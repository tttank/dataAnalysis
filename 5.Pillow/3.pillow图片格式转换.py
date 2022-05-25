from PIL import Image

# save() 方法用于保存图像，当不指定文件格式时，它会以默认的图片格式来存储；
# 如果指定图片格式，则会以指定的格式存储图片 Image.save(fp, format=None)
# im = Image.open(r"C:\Users\tank\Desktop\aodi.jpeg")
# im.save("C:/Users/tank/Desktop/a.xiugai.bmp")


# convert()+save() 由于 PNG 和 JPG 图像模式不一致导致的。
# 其中 PNG 是四通道 RGBA 模式，即红色、绿色、蓝色、Alpha 透明色；
# JPG 是三通道 RGB 模式。因此要想实现图片格式的转换，
# 就要将 PNG 转变为三通道 RGB 模式。
im = Image.open(r"C:\Users\tank\Desktop\jie.png")
# 此时返回一个新的image对象,转换图片模式
image = im.convert('RGB')
# 调用save()保存
image.save("C:/Users/tank/Desktop/b.xiugai.jpg")