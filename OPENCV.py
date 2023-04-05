import cv2

# 读取图像或视频
img = cv2.imread('程浩.jpg')

# 执行图像处理操作
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示图像
cv2.imshow('image', gray)
cv2.waitKey(0)

# 保存处理后的图像
cv2.imwrite('gray.jpg', gray)
