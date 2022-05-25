from PIL import Image

# crop(box=None) 以矩形区域的方式对原图像进行裁剪
im = Image.open("C:/Users/tank/Desktop/20.png")
# box = (0, 0, 200, 100)
# im_crop = im.crop(box)
# im_crop.show()


# 拷贝和粘贴 copy()和 paste(image, box=None, mask=None)
"""
image：指被粘贴的图片；
box：指定图片被粘贴的位置或者区域，其参数值是长度为 2 或者 4 的元组序列，长度为 2 时，表示具体的某一点 (x,y)；长度为 4 则表示图片粘贴的区域，此时区域的大小必须要和被粘贴的图像大小保持一致。
mask：可选参数，为图片添加蒙版效果。
"""
# 复制一张图片副本
im_copy = im.copy()
# 对副本进行剪裁
im_crop = im_copy.crop((0, 0, 200, 100))
# 创建一个新的图片作为蒙版,L模式,单颜色值
image_new = Image.new('L', (200, 100), 200)
# 粘贴
im_copy.paste(im_crop, (100, 100, 300, 200), mask=image_new)
im_copy.show()
