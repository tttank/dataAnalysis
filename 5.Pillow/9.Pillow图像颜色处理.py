from PIL import Image, ImageColor

# getrgb()方法 该函数用来得到颜色的 RGB 值
color1 = ImageColor.getrgb('blue')
print(color1)

color2 = ImageColor.getrgb('#DCDCDC')
print(color2)

color3 = ImageColor.getrgb('HSL(0, 100%, 50%)')
print(color3)

# 通过new()方法 新建图像 im = Image.new(mode,size,color)
im = Image.new('RGB', (200, 200), ImageColor.getrgb('blue'))
im.show()


# getcolor()获取颜色值，PIL.ImageColor.getcolor(color, mode)
color4 = ImageColor.getcolor('#EEA9B8', 'L')
print(color4)

color5 = ImageColor.getcolor('yellow', 'RGBA')
print(color5)
