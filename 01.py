'''
捲積由兩長度相同的向量透過滑動到不同位置並相乘後相加得到的結果
DFT:離散傅立葉轉換;dc係數和0點組成
fft2 = 矩陣傅立葉轉換(DFT)
ifft2 = 反DFT;逆時針方向旋轉
fftshift = 平移轉換;對角互換
AB  DC
CD  BA
dc係數:矩陣所有值的總和集中於dft影像(0,0)位置，比其他值大，其餘為0
'''
import skiamge.io as io
from numpy import ones, int16, zeros, log, meshgrid
from numpy.fft import fft2, fftshift, ifft2
from matplotlib.pyplot import figure
def fftshow(im, type='log'):
  if type == 'log':
    #dft轉換結果
    fl = log(1+abs(im))
    fm = fl.max()
    #figure(),io.imshow(fl)#彩色
    figure(),io.imshow(fl/fm, cmap= 'gray')
  elif type == 'abs':
    fa = abs(im)
    fm = fa.max()
    io.imshow(fa/fm, cmap='gray')
   else:
    print("Error:type must be abs or log")

#二維陣列，4(前)個[1,1,1,1](後)
a1 = ones((4, 4))
#矩陣的DFT，轉乘16位整數
#[[16,0,0...]] 15個0，int16:傅立葉轉換會是複數
A1 = int16(fft2(a1))

#二維陣列， 256個[0,0,0..]
a = zeros((256, 256))
a[77:177, 77:177] = 1
#平移傅立葉轉換，將DC係數至於中心
#中間白正方形
af = fftshift(fft2(a))
figure(), fftshow(a)
figure(), fftshow(af)


cm = io.imread(r'/content/drive/MyDrive/cameraman.png')
cf = fftshift(fft2(cm))
#沒平移轉換
#低通濾波器
#傅立葉轉換矩陣F，平移後DC係數在中心

d = 15 #截頻點:將此頻率點以上的過濾掉，越小越模糊
ar = range(-128, 128)
x, y= meshgrid(ar, ar) 
'''
meshgrid =    7             1 7   2 7
            y 6         ->  1 6   2 6
              5             1 5   2 5
                1 2 3 4
                    x
x = [[-128, -127,.....]*128-(-128)]
y = [[-128,-128,....],
      [-127,-127,...]...]
'''
c = (x**2 + y**2 < d**2) *1.0 #低通:< 高通:>
cfL = cf * c #dft影像*濾波器
figure(), fftshow(fft2(cm))
figure(), fftshow(cfL)
figure(), fftshow(cfL, 'abs')
#呈現波紋狀，經fft2運算，取相近數字


             
