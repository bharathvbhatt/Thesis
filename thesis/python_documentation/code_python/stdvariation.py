#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:48:45 2021

@author: bharathvbhatt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tikzplotlib import save as tikz_save
freq = np.arange(1,41)*50e3

# std_ppm = [
#       3.33,
#       3.4,
#       3.43,
#       4.62,  
#       2.542,
#       2.43,
#       2.6,
#       3.039,
#       1.59,
#       2.28,
#       1.66,
#       3.404,
#       3.26,
#       5.04,
#       2.722,
#       2.72,
#       2.177,
#       2.22,
#       1.649,
#       1.17     ]
# plt.plot(freq,std_ppm)
# plt.title("Excitation frequency vs STD")
# plt.xlabel('Excitation frequency in KHz')
# plt.ylabel("TD in ppm")


#freq = [800e3,850e3,900e3,950e3,1000e3,1050e3,1100e3,1150e3,1200e3,1250e3,1300e3,1350e3,1400e3,1450e3,1500e3,1550e3,1600e3,1650e3,1700e3,1750e3,1800e3,1850e3,1900e3,1950e3,2000e3]
# std= [
#          3.33,
#       3.4,
#       3.43,
#       4.62,
#       2.542,
#       2.43,
#       2.6,
#       3.039,
#       1.59,
#       2.28,
#       1.66,
#       3.404,
#       3.26,
#       5.04,
#       2.722,
#     3.315140,
#   2.329862,
#   2.674610,
#   1.638155,
#   2.000745,
#   1.630120,
#   1.067485,
#   3.285560,
#   2.733242,
#   3.085755,
#   3.435753,
#   3.149836,
#   2.139301,
#   1.397987,
#   1.951400,
#   2.820142,
#   3.077280,
#   1.584293,
#   3.601018,
#   3.885632,
#   2.796365,
#   3.438695,
#   2.239638,
#   3.399156,
#   4.276776
 
#   ]
# plt.scatter(freq,std)
# plt.plot(freq,std)
# plt.title("Excitation frequency vs STD")
# plt.xlabel('Excitation frequency in KHz')
# plt.ylabel("TD in ppm")


# freq = np.arange(1,31)*100e3
# value = [
#     2.4188,
#     2.4192,
#     2.41970,
#     2.4195565,
#     2.41919,
#     2.4192141,
#     2.41931,
#     2.41921,
#     2.41922,
#     2.41923,
#     2.41926,
#     2.41938,
#     2.41945,
#     2.41933,
#     2.41934,
#     2.41929,
#     2.4194,
#     2.4196,
#     2.41944,
#     2.41945,
#     2.41936,
#     2.4194,
#     2.41939,
#     2.41940,
#     2.42168,
#     2.42168,
#     2.42168,
#     2.42164,
#     2.42168,
#     2.42169
#     ]
# plt.plot(freq,value)



frequency = [
    2.4171,
    2.4172,
    2.4173,
    2.4174,
    2.4175,
    2.4176,
    2.4177,
    2.4178,
    2.4179,
    2.418,
    2.4181,
    2.4182,
    2.4183,
    2.4184,
    2.4185,
    2.4186,
    2.4187,
    2.4188,
    2.4189,
    2.419,
    2.4191,
    2.4192,
    2.4193,
    2.4194,
    2.4195,
    2.4196,
    2.4197,
    2.4198,
    2.4199,
    2.42,
    2.4201,
    2.4202,
    2.4203,
    2.4204,
    2.4205,
    2.4206,
    2.4207,
    2.4208,
    2.4209,
    2.4210
    ]


value=[2.42290289,
2.41916106666667,
2.41915502,
2.41908628888889,
2.41911836,
2.41919355,
2.41904704,
2.41915785,
2.41912766,
2.41915564444444,
2.419155,
2.41919395,
2.41919143,
2.41915498888889,
2.41918862,
2.4192139,
2.41935816,
2.41922096,
2.41921663,
2.41923843,
2.41918842,
2.41931378888889,
2.41934165,
2.41934667,
2.41935014,
2.41927003333333,
2.41946754444444,
2.41933231,
2.41947432222222,
2.41945401,
2.41926818888889,
2.41940154,
2.4194745,
2.42162527,
2.42166799,
2.41936903333333,
2.41937028888889,
2.42015852,
2.42169352222222,
2.42170162222222]

std=[
     44.149493,
18.450184,
20.593443,
20.472483,
8.443263,
7.27055,
28.531279,
22.022961,
9.164373,
4.576087,
5.3364214,
6.080092,
3.215309,
9.604131,
2.877351,
2.398806,
9.219562,
5.525729,
5.511611,
1.484901,
1.499888,
3.562961,
3.239117,
1.966445,
0.513118,
0.23526,
2.398313,
7.979189,
8.693511,
3.789987,
15.940724,
20.61539,
13.843596,
12.566704,
2.800009,
3.062252,
2.997057,
10,
8.906469,
1.896559

     
     ]


# plt.plot(frequency,value)
# plt.title("Exciatation frequency VS Estimated frequency : Actual frq is 2.4192GHz")
# plt.xlabel("Excitation frequency in GHz")
# plt.ylabel("Estimated frequency in ppm")
plt.plot(frequency,std)
plt.title("Exciatation frequency VS std in ppm : Actual frq is 2.4192GHz")
plt.xlabel("Excitation frequency in GHz")
plt.ylabel("STD in ppm")

