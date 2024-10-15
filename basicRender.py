import cv2
import matplotlib.pyplot as plt

img = cv2.imread('testimg.jpg')

#convert
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#showww
plt.imshow(img_rgb)
plt.title("Test Image")
plt.axis('off')  
plt.show()
