from PIL import Image
import os

"""
resize(size, resample=image.BICUBIC, box=None, reducing_gap=None)
size：元组参数 (width,height)，图片缩放后的尺寸；
resample：可选参数，指图像重采样滤波器，与 thumbnail() 的 resample 参数类似，默认为 Image.BICUBIC；
box：对指定图片区域进行缩放，box 的参数值是长度为 4 的像素坐标元组，即 (左,上,右,下)。注意，被指定的区域必须在原图的范围内，如果超出范围就会报错。当不传该参数时，默认对整个原图进行缩放；
reducing_gap：可选参数，浮点参数值，用于优化图片的缩放效果，常用参数值有 3.0 和 5.0。
"""

# im = Image.open(r"C:\Users\tank\Desktop\07.jpg")

""" 放大图片 """
# try:
#     # 放大图片
#     print('查看原始图片尺寸:', im.size)
#     image = im.resize((1500, 1400))
#     image.save("C:/Users/tank/Desktop/07.放大.jpg")
#     print('查看新图像尺寸:', image.size)
# except IOError:
#     print('放大图片失败')

""" 对图片局部放大 """
# try:
#     # 选择放大的局部位置,并徐哲图片重采样方式
#     # box四元组指的是像素坐标 (左,上,右,下)
#     # (0,0,120,180)，表示以原图的左上角为原点，选择宽和高分别是(120,180)的图像区域
#     image = im.resize((1600, 1500), box=(0, 0, 120, 180))
#     image.show()
#     image.save("C:/Users/tank/Desktop/07.放大2.jpg")
#     print('查看新图片的尺寸:', image.size)
# except IOError:
#     print('放大失败')

""" 
创建缩略图 
thumbnail(size,resample)
size：元组参数，指的是缩小后的图像大小；
resample：可选参数，指图像重采样滤波器，有四种过滤方式，分别是 Image.BICUBIC（双立方插值法）、PIL.Image.NEAREST（最近邻插值法）、PIL.Image.BILINEAR（双线性插值法）、PIL.Image.LANCZOS（下采样过滤插值法），默认为 Image.BICUBIC
"""
# im.thumbnail((150,50))
# print('缩略图尺寸', im.size)
# im.save('C:/Users/tank/Desktop/07.缩略图.jpg')

""" 批量修改图片尺寸 """
# 读取图片目录
fileName = os.listdir('C:/Users/tank/Desktop/image01')
print(fileName)
# 设定统一尺寸
width = 350
height = 350
# 如果目录不存在,则创建目录
if not os.path.exists('C:/Users/tank/Desktop/NewImage/'):
    os.mkdir('C:/Users/tank/Desktop/NewImage/')
# 循环读取每一张图片
for img in fileName:
    old_pic = Image.open('C:/Users/tank/Desktop/image01/' + img)
    new_image = old_pic.resize((width, height))
    print(new_image)
    new_image.save('C:/Users/tank/Desktop/NewImage/' + img)
