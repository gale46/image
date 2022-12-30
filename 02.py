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
