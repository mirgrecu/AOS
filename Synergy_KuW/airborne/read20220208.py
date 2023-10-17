fname='Subsets/IMPACTS2022_20220208_14200_17000.nc'
import netCDF4 as nc4
with nc4.Dataset(fname) as f:
    zKa=f['zKa'][:]
    zKu=f['zKu'][:]
    zW=f['zW'][:]
    vDopKu=f['vDopKu'][:]
    height=f['height'][:]
    timeL=f['timeL'][:]

import matplotlib.pyplot as plt
import numpy as np
nx2=zKa.shape[0]//2
b=np.nonzero((height>2000)&(height<3000))
hL=[]
hLKa=[]
dZ=[]
for i in range(0,nx2):
    zKu1=zKu[i,::-1]
    ind=np.argmax(zKu1[b])
    hL.append(height[b[0][0]+ind])
    dZ.append(zKu1[b[0][0]+ind]-zKu1[b[0][0]])
    ind=np.argmax(zKa[i,:][b])
    hLKa.append(height[b[0][0]+ind])
from scipy.ndimage import gaussian_filter1d
hL_filtered=gaussian_filter1d(hL, sigma=15)