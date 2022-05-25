from PIL import Image, ImageDraw, ImageFont

"""
draw = ImageDraw.Draw(im)
text:在图像上绘制文字,需结合imageFont模块一起使用
line:绘制直线,线段
eclipse:绘制椭圆形
rectangle:绘制矩形
polygon:绘制多边形
"""

# 绘制矩形 draw.rectangle(xy, fill=None, outline=None)
# 创建Image对象,当做背景图
# im = Image.new('RGB', (200, 200), color='gray')
# # 创建ImageDraw对象
# draw = ImageDraw.Draw(im)
# # 以左上角为原点,元祖坐标序列表示矩形的位置大小,fill设置填充色为红色,outline设置边框线为黑色
# draw.rectangle((50, 100, 100, 150), fill=(255, 0, 0), outline=(0, 0, 0))
# im.show()
# im.save("C:/Users/tank/Desktop/添加矩形图.png")


# 创建字体对象 font = ImageFont.truetype(font='字体文件路径', size=字体大小)
# 在图片上添加文本水印 d.text((x,y), "text", font, fill)
im = Image.open('C:/Users/tank/Desktop/大熊猫.png')
# # 创建画布对象
# draw = ImageDraw.Draw(im)
# # 加载计算机本地字体文件
font = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', size=30)
# # 在原图像上添加文本
# draw.text(xy=(80, 50), text='大熊猫的专属水印', fill=(255, 0, 0), font=font)
# im.show()
# im.save("C:/Users/tank/Desktop/水印图.png")


""" 添加图片水印设置透明度,颜色 """
# 转换图片格式,添加透明度
im_rgba = im.convert('RGBA')
im_text_canvas = Image.new('RGBA', im_rgba.size, (255, 255, 255, 0))
print(im_rgba.size[0])
# 创建画布对象
draw = ImageDraw.Draw(im_text_canvas)
# 设置文本字体大小
text = '大熊猫的水印'
text_x_width, text_y_height = draw.textsize(text, font=font)
print(text_x_width, text_y_height)
# 字体坐标
text_xy = (im_rgba.size[0] - text_x_width, im_rgba.size[1] - text_y_height)
print(text_xy)
# 设置文本颜色(绿色) 和透明度(半透明) 颜色元祖参数最后一个参数表示透明度
draw.text(text_xy, text, font=font, fill=(255, 0, 0, 130))
# im_text_canvas.show()
# 将原图与文字复合
im_text = Image.alpha_composite(im_rgba, im_text_canvas)
im_text.show()
im_text.save('C:/Users/tank/Desktop/半透明水印图.png')