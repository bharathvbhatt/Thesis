#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:42:23 2021

@author: bharathvbhatt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tikzplotlib
import matplotlib
from sklearn.metrics import mean_squared_error

# matplotlib.use("pgf")

# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })

strain = np.arange(40)*2
DFE_wired_fft = [
    2.418931,
    2.418978,
    2.419037,
    2.419069,
    2.419088,
    2.41913,
    2.419175,
    2.4192,
    2.419241,
    2.419282,
    2.419329,
    2.419381,
    2.419426,
    2.419457,
    2.419539,
    2.419545,
    2.419583,
    2.419624,
    2.41969,
    2.419734,
    2.419761,
    2.419814,
    2.419842,
    2.419886,
    2.419934,
    2.419971,
    2.420024,
    2.420062,
    2.420087,
    2.420135,
    2.420197,
    2.420212,
    2.42025,
    2.4203,
    2.420327,
    2.420392,
    2.420444,
    2.420449,
    2.420494,
    2.42052
]

DFE_wireless_farfiled = [
    2.418983,
    2.419024,
    2.419058,
    2.419076,
    2.419138,
    2.419183,
    2.419207,
    2.419238,
    2.419296,
    2.419331,
    2.419384,
    2.419402,
    2.419459,
    2.419504,
    2.419555,
    2.419561,
    2.419591,
    2.419685,
    2.419769,
    2.419721,
    2.419847,
    2.419855,
    2.419974,
    2.419994,
    2.420054,
    2.42008,
    2.420138,
    2.420164,
    2.420141,
    2.420166,
    2.420211,
    2.420328,
    2.420376,
    2.420378,
    2.420465,
    2.420504,
    2.420584,
    2.42059,
    2.420632,
    2.420739

]
# plt.rc('pgf', texsystem='pdflatex')
# plt.style.use('seaborn')
# plt.scatter(strain, DFE_wired_fft,c='orange')
# model1 = np.polyfit(strain, DFE_wired_fft, 1)
# predict1 = np.poly1d(model1)
# x1 = strain
# y1 = predict1(x1)
# plt.plot(x1, y1, 'orange', label='Wired')
# #plt.title("DFE Far-field Vs. Wired Data")
# plt.xlabel("Strain in 0.01mm")
# plt.ylabel("Measured Frequency in GHz") 
# #plt.savefig('farfield_wired.pgf')
# error1 = mean_squared_error(DFE_wired_fft,y1)
# print(error1)
# plt.text(0,2.4199,"MSE_wired = $1.836\\times10^{-10}$")

# plt.scatter(strain, DFE_wireless_farfiled,c='b')
# model2 = np.polyfit(strain, DFE_wireless_farfiled, 1)
# predict2 = np.poly1d(model2)
# x2 = strain
# y2 = predict2(x2)
# plt.plot(x2, y2, 'b', label='Farfield')
# plt.legend()
# plt.grid(linestyle='--')
# error2 = mean_squared_error(DFE_wireless_farfiled,y2)
# print(error2)
# plt.text(0,2.420,'MSE_far-field = $1.11\\times10^{-9}$')

# error3 = mean_squared_error(DFE_wireless_farfiled,y1)
# print("Error from wireld line:"+str(error3))

#tikzplotlib.save("farfield_wired.tex")
DFE_16cm = [
    2.418948,
    2.418971,
    2.419027,
    2.419069,
    2.419099,
    2.419135,
    2.419175,
    2.419224,
    2.419256,
    2.41931,
    2.419349,
    2.419387,
    2.419425,
    2.419469,
    2.419511,
    2.419542,
    2.419594,
    2.419628,
    2.419672,
    2.419718,
    2.419747,
    2.41978,
    2.419839,
    2.419863,
    2.419895,
    2.41995,
    2.419996,
    2.420014,
    2.420053,
    2.42011,
    2.420161,
    2.420205,
    2.420251,
    2.42031,
    2.42034,
    2.420372,
    2.420386,
    2.420452,
    2.420505,
    2.420556

]
DFE_8cm = [
    2.41888,
    2.418931,
    2.418953,
    2.419018,
    2.419065,
    2.419111,
    2.419147,
    2.419182,
    2.41922,
    2.419259,
    2.4193,
    2.41935,
    2.419379,
    2.419435,
    2.41946,
    2.41951,
    2.419558,
    2.419588,
    2.419641,
    2.419664,
    2.419713,
    2.41975,
    2.419789,
    2.419824,
    2.419868,
    2.419902,
    2.41999,
    2.42001,
    2.42003,
    2.420065,
    2.420103,
    2.42015,
    2.420189,
    2.42023,
    2.42027,
    2.4203,
    2.420347,
    2.420398,
    2.420438,
    2.420473
]

# plt.rcParams["figure.figsize"] = (7,4.30)
# plt.scatter(strain, DFE_8cm,c='r')
# model1 = np.polyfit(strain,DFE_8cm,1)
# predict1 = np.poly1d(model1)
# x1 = strain
# y1 = predict1(x1)
# plt.text(0,2.420,'MSE_8cm = $1.101\\times10^{-10}$')
# plt.plot(x1,y1,'r',label='8cm')
# #plt.title("Effects of distance")
# plt.xlabel("Strain in 0.01mm")
# plt.ylabel("Measured Frequency in GHz") 
# error1 = mean_squared_error(DFE_8cm,y1)
# print(error1)

# plt.scatter(strain, DFE_16cm,c='b')
# model2 = np.polyfit(strain,DFE_16cm,1)
# predict2 = np.poly1d(model2)
# x2 = strain
# y2 = predict2(x2)
# plt.plot(x2,y2,'b',label='16cm')
# plt.text(0,2.4199,'MSE_16cm = $1.370\\times10^{-10}$')
# plt.legend()
# plt.grid(linestyle='--')
# error2 = mean_squared_error(DFE_16cm,y2)
# print(error2)

# distance = np.abs(model1[1]-model2[1])/np.sqrt((model1[0]**2)+1)
# print(distance*1e9)
# tikzplotlib.save("8-6cm.tex")


strain_neg =np.arange(52)*2
DFE_opposite_corrected =[
  2.4188376530612246,
  2.4188069696969694,
  2.4187690625,
  2.4187370103092785,
  2.418710210526316,
  2.418683402061856,
  2.4186512631578947,
  2.4186386597938148,
  2.418594255319149,
  2.418548469387755,
  2.418504285714286,
  2.418476907216495,
  2.4184351020408164,
  2.4184191666666663,
  2.4183882291666663,
  2.4183448453608247,
  2.4183136842105264,
  2.4182727368421055,
  2.4181187755102043,
  2.4181020408163265,
  2.4180869696969696,
  2.4180716161616163,
  2.4180546315789475,
  2.418031212121212,
  2.417987741935484,
  2.417958762886598,
  2.4179215217391303,
  2.417884226804124,
  2.417908585858586,
  2.417877741935484,
  2.4178392708333334,
  2.4177942268041237,
  2.417753548387097,
  2.4177105208333334,
  2.41765625,
  2.4176140206185566,
  2.4174840206185566,
  2.417456734693878,
  2.417425858585859,
  2.417384375,
  2.4173789361702127,
  2.417181030927835,
  2.4171415306122452,
  2.4170997959183675,
  2.41705898989899,
  2.4170211224489795,
  2.416977731958763,
  2.4169420408163265,
  2.4169076,
  2.4168679166666664,
  2.4168353535353537,
  2.4167982795698926
  ]
# DFE_opposite_corrected_step=[
#     2.418959797979798,
#     2.418905306122449,
#     2.4188928125,
#     2.4188589583333333,
#     2.4188329896907215,
#     2.418816907216495,
#     2.418778260869565,
#     2.4186928865979382,
#     2.418671122448979,
#     2.4185580208333337,
#     2.4184929591836735,
#     2.4184865,
#     2.4184588659793818,
#     2.4184175789473685,
#     2.4183864583333334,
#     2.4183688421052634,
#     2.4183610869565215,
#     2.418261111111111,
#     2.4182540206185563,
#     2.41822,
#     2.4181880808080805,
#     2.418223894736842,
#     2.4182613131313135,
#     2.418004949494949,
#     2.417994842105263,
#     2.417950625,
#     2.417907857142857,
#     2.417889175257732,
#     2.417864742268041,
#     2.417860206185567,
#     2.4178435353535352,
#     2.4178226262626263,
#     2.4176806382978726,
#     2.4176324731182794,
#     2.4174980412371134,
#     2.4175125510204083,
#     2.4174867368421054,
#     2.417457857142857,
#     2.4174155102040817,
#     2.4173892708333335,
#     2.4173801030927833,
#     2.417347311827957,
#     2.417296262626263,
#     2.4172494845360823,
#     2.417229052631579,
#     2.417186464646465,
#     2.4170273,
#     2.41700206185567,
#     2.416968152173913,
#     2.4169347872340428,
#     2.4168923958333335,
#     2.416857525773196
#     ]




# plt.plot(strain_neg, DFE_opposite_corrected_step,c='b')
# model1 = np.polyfit(strain_neg,DFE_opposite_corrected_step,1)
# predict1 = np.poly1d(model1)
# x1 = strain_neg
# y1 = predict1(x1)
# plt.text(0,2.417,'MSE_Opposite = $4.730\\times10^{-09}$')
# plt.plot(x1,y1,'r',label='8cm')
# plt.title("Secondary resonance effect removed")
# plt.xlabel("Strain in 0.01mm")
# plt.ylabel("Measured Frequency in GHz") 
# error1 = mean_squared_error(DFE_opposite_corrected_step,y1)
# print(error1)


plt.scatter(strain_neg, DFE_opposite_corrected,c='b')
model2 = np.polyfit(strain_neg,DFE_opposite_corrected,1)
predict2 = np.poly1d(model2)
x2 = strain_neg
y2 = predict2(x2)
plt.text(0,2.417,'MSE_Opposite = $4.730\\times10^{-09}$')
plt.plot(x2,y2,'r',label='8cm')
#plt.title("Secondary resonance effect removed")
plt.xlabel("Strain in 0.01mm")
plt.ylabel("Measured Frequency in GHz") 
error2 = mean_squared_error(DFE_opposite_corrected,y2)
print(error2)



