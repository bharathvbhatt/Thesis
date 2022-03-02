#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:32:19 2021

@author: bharathvbhatt
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:10:24 2021

@author: bharathvbhatt
"""
# d = [2,5,8,12,16,20,25,30]
# gain =[10,20,30,40,50,60]


# def get_mean(arr):
#     mean = sum(arr)/len(arr)
#     return mean

# def get_variance(arr):
#     var = np.var(arr)
#     std = np.std(arr)
#     return var,std


# f_10db = [2.421541,2.421871,2.4217268,2.4217665,2.4218148,2.4218173,2.4203567,2.415]
# f_20db = [2.4211213,2.4216922,2.4218451,2.421735,2.4217089,2.4214156,2.421661,2.4222882]
# f_30db = [2.4212717,2.4212144,2.4220579,2.4213612,2.4217972,2.4179683,2.4212544,2.421504]
# f_40db = [2.4219026,2.4217741,2.4217768,2.4213263,2.421605,2.4213407,2.421503,2.4213925]
# f_50db = [2.4212716,2.4219134,2.4218201,2.4217145,2.421973,2.4218233,2.4218329,2.4218145]
# f_60db = [2.4218209,2.4218803,2.4218301,2.4218789,2.4218235,2.421798,2.4218607,2.4213169]

# d_6  = [2.4217731,2.4217842,2.4218083,2.4218039,2.4219076,2.4218618]
# d_14 = [2.4213248,2.4214134,2.421686,2.4217044,2.4217876,2.4218238]
# d_25 = [2.415,2.415,2.4150124,2.4217868,2.4218053,2.4217636]
# d_30 = [2.415,2.415,2.415,2.415,2.4217555,2.4218247]

# print(get_variance(f_30db))
# plt.plot(d,f_10db,color='red',label='10dB')
# plt.plot(d,f_20db,color='green',label='20dB')
# plt.plot(d,f_30db,color='blue',label='30dB')
# plt.plot(d,f_40db,color='yellow',label='40dB')
# plt.plot(d,f_50db,color='pink',label='50dB')
# plt.plot(d,f_60db,color='brown',label='60dB')
# plt.xlabel('Distance in cm')
# plt.ylabel('Frequency in GHz')
# plt.title('Fixed Gain, with varying distance')

# plt.plot(gain,d_6,color = 'red',label='6cm')
# plt.plot(gain,d_14,color ='blue',label='14cm')
# plt.plot(gain,d_25,color = 'orange',label='25cm')
# plt.plot(gain,d_30,color='yellow',label='30cm')
# plt.xlabel('Gain in dB')
# plt.ylabel('Frequency in GHz')
# plt.title('Fixed distance, with varying gain')
# plt.legend()
# plt.show()


#######################strain VS Frequency#####################################
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression# true_value = 2.421791
import tikzplotlib

strain = np.arange(40)*2

FMCW_wired = [2.4188552,
              2.41889093,
              2.41894531,
              2.41898608,
              2.41901831,
              2.41906116,
              2.41911286,
              2.41914366,
              2.41919032,
              2.41923463,
              2.41927247,
              2.4193137,
              2.41935373,
              2.41939897,
              2.41943752,
              2.41947975,
              2.41952161,
              2.41956651,
              2.41961,
              2.41964998,
              2.41968833,
              2.41973159,
              2.4197755,
              2.41981344,
              2.41986106,
              2.41989746,
              2.41993801,
              2.41997929,
              2.42001783,
              2.42005374,
              2.42009943,
              2.42013936,
              2.42018051,
              2.42022343,
              2.42026797,
              2.42030767,
              2.4203472,
              2.42038353,
              2.42042697,
              2.42046967
              ]

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
# strain_neg = np.arange(20)*5
# DFE_wired_neg=[
#      2.418971,
#      2.4188753,
#      2.4187238,
#      2.4186211,
#      2.41858,
#      2.4184101,
#      2.4183042,
#      2.4182662,
#      2.4180921,
#      2.4181061,
#      2.4179392,
#      2.4178356,
#      2.4178417,
#      2.4176768,
#      2.4175899,
#      2.4196444,
#      2.4195517,
#      2.4189957,
#      2.4193413,
#      2.4192692
#     ]
strain_neg =np.arange(52)*2
DFE_wired_neg=[
    2.4189558,
    2.4189394,
    2.4188499,
    2.418823,
    2.4188005,
    2.4187345,
    2.4186999,
    2.4186817,
    2.41866,
    2.418565,
    2.4185277,
    2.4185077,
    2.4184499,
    2.41842,
    2.4183691,
    2.4183798,
    2.41835,
    2.4182336,
    2.4181892,
    2.4181302,
    2.4183318,
    2.4181598,
    2.4181409,
    2.4179938,
    2.4180677,
    2.4179633,
    2.4179329,
    2.4178939,
    2.4178251,
    2.4178663,
    2.4177483,
    2.4178158,
    2.4177095,
    2.4177241,
    2.4176305,
    2.4176305,
    2.4176505,
    2.4176147,
    2.417516,
    2.418175,
    2.4195823,
    2.4175121,
    2.417481,
    2.4181272,
    2.4194548,
    2.419411,
    2.4193699,
    2.4193662,
    2.4192581,
    2.4192795,
    2.4192214,
    2.419165
    ]
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

DFE_opposite_corrected_step=[
    2.418959797979798,
    2.418905306122449,
    2.4188928125,
    2.4188589583333333,
    2.4188329896907215,
    2.418816907216495,
    2.418778260869565,
    2.4186928865979382,
    2.418671122448979,
    2.4185580208333337,
    2.4184929591836735,
    2.4184865,
    2.4184588659793818,
    2.4184175789473685,
    2.4183864583333334,
    2.4183688421052634,
    2.4183610869565215,
    2.418261111111111,
    2.4182540206185563,
    2.41822,
    2.4181880808080805,
    2.418223894736842,
    2.4182613131313135,
    2.418004949494949,
    2.417994842105263,
    2.417950625,
    2.417907857142857,
    2.417889175257732,
    2.417864742268041,
    2.417860206185567,
    2.4178435353535352,
    2.4178226262626263,
    2.4176806382978726,
    2.4176324731182794,
    2.4174980412371134,
    2.4175125510204083,
    2.4174867368421054,
    2.417457857142857,
    2.4174155102040817,
    2.4173892708333335,
    2.4173801030927833,
    2.417347311827957,
    2.417296262626263,
    2.4172494845360823,
    2.417229052631579,
    2.417186464646465,
    2.4170273,
    2.41700206185567,
    2.416968152173913,
    2.4169347872340428,
    2.4168923958333335,
    2.416857525773196
    ]


DFE_wired_timeavg = [
    2.41894,
    2.41898,
    2.41904,
    2.41907,
    2.41905,
    2.41913,
    2.41917,
    2.4192,
    2.41924,
    2.41933,
    2.41942,
    2.41945,
    2.41948,
    2.41951,
    2.41954,
    2.41955,
    2.41958,
    2.41962,
    2.41969,
    2.41973,
    2.41976,
    2.4198,
    2.41983,
    2.41988,
    2.41993,
    2.41996,
    2.41998,
    2.42005,
    2.42008,
    2.42013,
    2.42019,
    2.42021,
    2.42025,
    2.42029,
    2.42033,
    2.42042,
    2.42045,
    2.42048,
    2.4205,
    2.42053
]
DFE_wired_timeavg2=[
    2.41891,
    2.41895,
    2.41899,
    2.41902,
    2.41906,
    2.41911,
    2.41914,
    2.41918,
    2.41922,
    2.41926,
    2.41929,
    2.41933,
    2.41936,
    2.41942,
    2.41944,
    2.41951,
    2.41955,
    2.41959,
    2.41959,
    2.41963,
    2.41969,
    2.41971,
    2.41977,
    2.41982,
    2.41983,
    2.41988,
    2.41989,
    2.41993,
    2.42,
    2.42002,
    2.42009,
    2.42012,
    2.42016,
    2.42025,
    2.42029,
    2.42031,
    2.42035,
    2.42042,
    2.42042,
    2.4205
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
DFE_wireless_12 = [
    2.418909,
    2.418958,
    2.418999,
    2.419037,
    2.419079,
    2.419126,
    2.419166,
    2.419202,
    2.419239,
    2.419278,
    2.419323,
    2.419361,
    2.419409,
    2.419469,
    2.419499,
    2.419569,
    2.419602,
    2.419628,
    2.419691,
    2.419735,
    2.419789,
    2.41981,
    2.41984,
    2.41989,
    2.419933,
    2.419956,
    2.419995,
    2.420022,
    2.420075,
    2.420092,
    2.420127,
    2.420161,
    2.420201,
    2.420254,
    2.4203,
    2.420336,
    2.420364,
    2.420387,
    2.42044,
    2.420464
]
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
plt.style.use('seaborn')
plt.rc('pgf', texsystem='pdflatex')
#plt.plot(strain,FMCW_wired)


#plt.plot(strain_neg,DFE_wired_neg)
#plt.title("Strain VS Measured frequency, secondary resonance effect")
#plt.xlabel("Strain in 0.01mm")
#plt.ylabel("Estimated frequency in GHz")

#plt.plot(strain_neg,DFE_opposite_corrected_step)



n_meas = [10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
time = [0.13,0.20,0.24,0.29,0.35,0.39,0.45,0.50,0.55,0.60,1.15,1.70,2.24,2.80,3.34,3.89,4.43,4.97,5.54]
time_vect=[0.12,0.16,0.20,0.23,0.27,0.29,0.34,0.38,0.42,0.48,0.87,1.28,1.66,2.80,2.49,2.89,3.30,3.69,4.10]
time_radix2=[0.13,0.17,0.21,0.25,0.29,0.34,0.38,0.43,0.48,0.50,0.96,1.40,1.84,2.30,2.73,3.18,3.62,4.08,4.55]
time_Vecradix2=[0.12,0.20,0.26,0.34,0.42,0.48,0.55,0.62,0.69,0.78,1.47,2.20,1.37,1.72,2.04,2.36,2.71,3.30,3.39]
plt.rcParams["figure.figsize"] = (5.86,4.30)
# plt.semilogx(n_meas, time,c='r',label='no vectorization,non-radix2 points')
# plt.semilogx(n_meas, time_vect,c='b',label='vectorization,non-radix2 points')
# plt.semilogx(n_meas, time_radix2,c='g',label='radix2 points')
# plt.semilogx(n_meas, time_Vecradix2,c='brown',label='vectorization and radix2 points')
plt.plot(n_meas,time,label='no vectorization,non-radix2 points')
plt.plot(n_meas,time_vect,label='vectorization,non-radix2 points')
plt.plot(n_meas,time_Vecradix2,label='vectorization and radix2 points')
plt.plot(n_meas,time_radix2,label='radix2 points')
plt.xlabel("Number of measurements")
plt.ylabel("Time in s")

#plt.plot(strain,DFE_wired_timeavg2)
# plt.xlabel("Number of measurements")
# plt.ylabel("Time in s")
# plt.title(" Computation time Vs measurements")
#tikzplotlib.save("FMCW.tex")
#plt.savefig("FMCW_wired.pgf")

#plt.plot(strain,DFE_wired_fft,'r',label='FFT based averaging')
#plt.plot(strain,DFE_wired_timeavg,'b',label='Time based averaging')
#plt.plot(strain,DFE_wireless_farfiled,'b',label='Far field')
#plt.plot(strain,DFE_16cm,'orange',label='16cm')
#plt.plot(strain,DFE_wireless_12,'purple',label='12cm')
#plt.plot(strain,DFE_8cm,'green',label='8cm')




# # plt.plot(strain,freq_wireless_withoutfilt,'r',label='Wireless_with_outliers')
# # plt.plot(strain,freq_wireless_filtered_300,'b',label='Wireless_without_outliers')
# # plt.plot(strain,freq_wired_filt,color='orange',label='Wired_without_outliers')
# # plt.plot(strain,freq_wired_withoutfilt,color='purple',label='Wireless_with_outliers')
# # # plt.plot(strain,freq_wireless_filtered_300,'b',label='Wireless_filtered_10cm')
# # # plt.plot(strain,freq_wireless_filtered_300_18cm,'r',label='Wireless_filtered_18cm')
# # plt.plot(strain,freq_wireless_farfield,'b',label='Wireless_unfiltered_farfield')
# # plt.plot(strain,freq_unfilt_farfield,'r',label='Wired_unfiltred')


#plt.xlabel("Strain in 0.01mm")
#plt.ylabel("Frequency in GHz")
#plt.title("FMCW-Wired Analysis : Strain vs. Frequency")
# plt.text(1.0, 1.0,'42dB RX Gain,10cm Distance')
plt.legend()
plt.show()
plt.grid(linestyle='--')
###############################################################################


# fft_bin = np.fromfile('fft_val.txt')
# #fft_bin = np.fromfile("fmcw_bin.txt")
# noise = np.array([])
# array = np.array(fft_bin)
# avg = sum(array)/len(array)
# print(avg)
# for i in range(len(array)):
#     if array[i]>2*avg:
#         array[i]=array[i-1]
# for i in range(len(array)):
#     if array[i]<(avg-80):
#         array[i]=array[i-1]
# for i in range(len(array)):
#     if (array[i]<2*avg and array[i]>avg):
#         noise = np.append(noise,array[i])


# freq=(array)*10e3 + 2.41e9
# est_freq = sum(freq)/len(freq)
# print(est_freq/1.0e9)
# freq_ppm = freq *1e6/2.42e9
# mean = sum(freq_ppm)/len(freq_ppm)
# freq_ppm = freq_ppm-mean
# N = 100
# Range = max(freq_ppm)-min(freq_ppm)
# Interval = math.sqrt(N)
# width = Range/Interval
# N_bins = int(Range//width)
# std = np.std(freq_ppm)
# print("%2f,%2f" %(mean,std))



# plt.hist(freq_ppm,bins='auto')
# #plt.text(-599,77,'$\mu$='+ str(mean))
# plt.text(-28,600,'$\sigma$='+str("{:.2f}".format(std)))
# plt.xlabel('$\Delta$fppm',fontweight='bold')
# plt.ylabel('Counts')
# plt.title('Histogram plot of 1000 measurements,30dB-10cm')
# plt.show()


# # freq = f_20db

# # N = len(freq)
# # Range = max(freq)-min(freq)
# # Interval = math.sqrt(N)
# # width = Range/Interval
# # mean = sum(freq)/len(freq)
# # std = np.std(freq)
# # print(mean,std)
# # plt.hist(fft_bin,bins=1)
# # plt.xlabel('Frequency x10e3 Hz')
# # plt.ylabel('Counts')
# # plt.title('Histogram plot of 100 measurements')
# # plt.show()
