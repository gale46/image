import skimage.io as io
import skimage.util.noise as noise
import numpy as np
from matplotlib.pyplot import figure
import scipy.ndimage as ndi
from numpy.fft import fft2, ifft2
import skimage.exposure as ex
from skimage.feature import canny
from skimage.exposure import equalize_hist
import skimage.color as co
from matplotlib import pyplot as plt
#不轉float會產生溢位
s = io.imread(r'/content/drive/MyDrive/Untitled Folder/color_sunset.png').astype('float64')
s2 = np.zeros_like(s)
ss = io.imread(r'/content/drive/MyDrive/Untitled Folder/color_sunset.png')

#加強對比
for i in range(3):
  s2[:,:,i] = equalize_hist(s[:,:,i])
'''
figure(), io.imshow(ss)
figure(), io.imshow(s2)
'''
#rgb轉乘hsv，rgb變成色調 飽和 明暗
shsv = co.rgb2hsv(s)
shsv[:,:,2] = equalize_hist(shsv[:,:,2])
s3 = co.hsv2rgb(shsv)
#hsv to rgb
x = io.imread(r'/content/drive/MyDrive/Untitled Folder/gull.png')
#轉成灰階
xgray = co.rgb2gray(x)
#亮度(3的位置數值0)和色彩資訊
xyiq = co.rgb2yiq(x)
#邊緣偵測，擷取亮度分輛，找到邊緣
#轉灰階
xe1 = canny(xgray)

#轉hsv
xhsv = co.rgb2hsv(x)


#plt.subplot(221), plt.imshow(xe1)
'''
plt.subplot(222), plt.imshow(xgray, cmap='gray')
plt.subplot(223), plt.imshow(xyiq)
plt.subplot(224), plt.imshow(xhsv)
'''

x2 = np.zeros_like(x)

for i in range(3):
  x2[:,:,i] = canny(np.float64(x[:,:,i]) / 255)
  #將RGB各分量
xe2 = (x2[:,:,0] + x2[:,:,1] + x2[:,:,2]) > 2
#邊緣後將各分量合併
#rgb擷取
#閥值越大雜訊越少
xe3 = canny(xyiq[:,:,0])
#yiq擷取亮度分布，找到邊緣

plt.subplot(131), plt.imshow(xe3)
plt.subplot(132), plt.imshow(xe2)
plt.subplot(133), plt.imshow(xe1)
#rgb 較為完整

plt.show()
io.show()
