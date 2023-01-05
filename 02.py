'''
import skimage.io as io
import skimage.util.noise as noise
import numpy as np
from matplotlib.pyplot import figure
import scipy.ndimage as ndi
from numpy.fft import fft2, ifft2
import skimage.exposure as ex
#影像模糊化
cr = io.imread(r'/content/drive/MyDrive/Untitled Folder/car.png')
m = np.ones((1, 7)) / 7
cm = ndi.correlate(cr, m)
print(cr.shape)
#濾波器傅立葉
m2 = np.zeros_like(cr)*1.0
m2[1,0:7] = m
mf = fft2(m2)
mf[np.where(abs(mf)<0.01)] = 1
#影像傅立葉除以濾波器傅立葉
bmi = abs(ifft2(fft2(cm)/mf))
io.imshow(bmi/bmi.max(), vmax= 0.2, vmin=0)
io.show()

'''
import skimage.io as io
import skimage.util.noise as noise
import numpy as np
from matplotlib.pyplot import figure
import scipy.ndimage as ndi
from numpy.fft import fft2, ifft2
g =  io.imread(r'/content/drive/MyDrive/gull_gray.png')
#圖片的列行平面數
x, y = g.shape
t = np.zeros((x,y,10))

#鹽和胡椒雜訊7%
#gaussian:高斯雜訊，白雜訊的理想化形式，頻道沒調好的電視
#t=10張進行高斯雜訊的g，每張都不一樣
for i in range(10):
  t[:,:,i] = noise.random_noise(g, 'gaussian', var = 0.07)
#去除高斯雜訊，計算平均值，將10張圖相加/10
#2=二維
# mean()函数功能：求取均值
ta = np.mean(t, 2)
figure(), io.imshow(ta)

cr = io.imread(r'/content/drive/MyDrive/car.png')
#動態濾波器:10*1 element=0.1陣列
#進行捲積，圖片模糊
'''
>>> s = (2,2)
>>> np.ones(s)
array([[1.,  1.],
       [1.,  1.]])
'''
m = np.ones((10,1))/10
#增加動態模糊
cm = ndi.correlate(cr,m)
#zeros_like m*n elements=0
m2 = np.zeros_like(cr) * 1.0
m2[0:10, 0:1] = m
mf2 = fft2(m2)

d = 0.02
#d越大白色越多
mf2[np.where(abs(mf2)<d)] = 1
#去除模糊影像
#影像傅立葉除以濾波器傅立葉
bmi2 = abs(ifft2(fft2(cm)/mf2))
figure(),io.imshow(cm)
figure(),io.imshow(bmi2/bmi2.max(), vmax=0.2, vmin=0)
io.show()
