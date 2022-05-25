import PIL
from PIL import Image

# 打开图片文件
im = Image.open(r"C:\Users\tank\Desktop\aodi.jpeg")
# 显示图片
# im.show()


"""
使用 Image 类提供的 new() 方法可以创建一个新的 Image 对象，语法格式如下:
im = Image.new(mode,size,color)
参数说明如下：
mode：图像模式，字符串参数，比如 RGB（真彩图像）、L（灰度图像）、CMYK（色彩图打印模式）等；
size：图像大小，元组参数（width, height）代表图像的像素大小；
color：图片颜色，默认值为 0 表示黑色，参数值支持（R,G,B）三元组数字格式、颜色的十六进制值以及颜色英文单词。
"""
im = Image.new(mode='RGB', size=(260, 100), color='#ff0000')
im.show()
