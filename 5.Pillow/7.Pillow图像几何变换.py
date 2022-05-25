from PIL import Image

"""
翻转操作: Image.transpose(method)
Image.FLIP_LEFT_RIGHT：左右水平翻转；
Image.FLIP_TOP_BOTTOM：上下垂直翻转；
Image.ROTATE_90：图像旋转 90 度；
Image.ROTATE_180：图像旋转 180 度；
Image.ROTATE_270：图像旋转 270 度；
Image.TRANSPOSE：图像转置；
Image.TRANSVERSE：图像横向翻转
"""
im = Image.open("C:/Users/tank/Desktop/07.放大.jpg")
# im_out = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_out.show()
# im_out.save("C:/Users/tank/Desktop/07.水平翻转.jpg")


"""
任意角度旋转:
Image.rotate(angle, resample=PIL.Image.NEAREST, expand=None, center=None, translate=None, fillcolor=None)
angle：表示任意旋转的角度；
resample：重采样滤波器，默认为 PIL.Image.NEAREST 最近邻插值方法；
expand：可选参数，表示是否对图像进行扩展，如果参数值为 True 则扩大输出图像，如果为 False 或者省略，则表示按原图像大小输出；
center：可选参数，指定旋转中心，参数值是长度为 2 的元组，默认以图像中心进行旋转；
translate：参数值为二元组，表示对旋转后的图像进行平移，以左上角为原点；
fillcolor：可选参数，填充颜色，图像旋转后，对图像之外的区域进行填充
"""
# im_out = im.rotate(45, translate=(0, -25), fillcolor='green')
# im_out.show()
# im_out.save("C:/Users/tank/Desktop/07.旋转图像.jpg")


"""
图像变换: Image.transform(size, method, data=None, resample=0) 
size：指定新图片的大小；
method：指定图片的变化方式，比如 Image.EXTENT 表示矩形变换；
data：该参数用来给变换方式提供所需数据；
resample：图像重采样滤波器，默认参数值为 PIL.Image.NEAREST
"""
im_out = im.transform((250,250), Image.EXTENT, data=[0,0,30 + im.width//4,im.height//3])
im_out.show()
im_out.save("C:/Users/tank/Desktop/07.变换.jpg")