from PIL import Image
import numpy as np

# 创建300*400的图像,3个颜色通道
array = np.zeros([300, 400, 3], dtype=np.uint8)
print(array)
# rgb色彩模式
array[:, :200] = [255, 0, 0]
array[:, 200:] = [255, 255, 0]
img = Image.fromarray(array)
img.show()
img.save('C:/Users/tank/Desktop/数组生成图像.png')



# 图像转化为ndarry数组
im = Image.open('C:/Users/tank/Desktop/大熊猫.png')
im2 = np.array(im)
print(im2)

# # 将数组转化为图像
# arr_img = Image.fromarray(im2)
# arr_img.show()