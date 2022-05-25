from PIL import Image

# # split() 的使用方法比较简单，用来分离颜色通道
# im = Image.open("C:/Users/tank/Desktop/10.png")
# # 修改图像大小,以适应图像处理
# image = im.resize((450, 400))
# image.save("C:/Users/tank/Desktop/20.png")
# # 分离颜色通道,产生三个 Image对象
# r, g, b = image.split()
# r.show()
# g.show()
# b.show()
#
# # Image.merge(mode, bands) 图像的合并操作
# image_merge = Image.merge('RGB', (b, g, r))
# image_merge.show()
# image_merge.save("C:/Users/tank/Desktop/30.png")


# 两张图片合并  大小必须一致
im_1 = Image.open("C:/Users/tank/Desktop/20.png")
im_2 = Image.open("C:/Users/tank/Desktop/向日葵.png")
# 修改尺寸一致
image = im_2.resize(im_1.size)
# 颜色分离
r1, g1, b1 = im_1.split()
r2, g2, b2 = image.split()
# 合并图像
im_3 = Image.merge('RGB', [r2, g1, b2])
im_3.show()
im_3.save("C:/Users/tank/Desktop/合成.png")

# Image.blend(image1,image2, alpha)  混合 RGBA 模式的图片（PNG 格式）
# image1，image2：表示两个 Image 对象。
# alpha：表示透明度，取值范围为 0 到 1，当取值为 0 时，输出图像相当于 image1 的拷贝，而取值为 1 时，则是 image2 的拷贝，
# 只有当取值为 0.5 时，才为两个图像的中合。因此改值的大小决定了两个图像的混合程度。
""""
混合 rgba模式的图像
"""
im1 = Image.open("C:/Users/Administrator/Desktop/c-net.png")
image = Image.open("C:/Users/Administrator/Desktop/心形函数图像.png")
im2 = image.resize(im1.size)


def blend_im(im1, im2):
    # 设置 alpha 为 0.5
    Image.blend(im1, im2, 0.5).save("C:/Users/Administrator/Desktop/C语言中文网.png")


# 调用函数
blend_im(im1, im2)
