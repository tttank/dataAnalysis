import PIL
from PIL import Image

im = Image.open(r"C:\Users\tank\Desktop\aodi.jpeg")

# 打印image对象
print(im)

# 1) size：查看图像的尺寸
print('宽是%s高是%s'%(im.width, im.height))
# 通过size查看尺寸大小
print('图像的大小尺寸:', im.size)

# 2) format：查看图片的格式
print('图像的格式:', im.format)

# 3) readonly：图片是否为只读   该属性的返回为 0 或者 1
print('图像是否为只读:', im.readonly)

# 4 ) info：查看图片相关信息
print('图像信息:', im.info)

# 5) mode：图像模式
print('图像模式信息:', im.mode)

