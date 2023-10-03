# -*- coding: utf-8 -*-
"""
@author: Shasa Foster
https://www.linkedin.com/in/shasafoster
"""

if __name__ == "__main__":
    import os
    import pathlib
    import sys
    
    os.chdir(pathlib.Path(__file__).parent.parent.parent.parent.resolve()) 
    sys.path.append(os.getcwd())
    print('__main__ - current working directory:', os.getcwd())


from frm.pricing_engine.heston import simulate_heston
from frm.pricing_engine.gbm import simulate_gbm

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt



# Sample use
#result = simGBM(1, 0.84, 0.02, np.sqrt(0.1), 1/100, np.random.normal(0, 1, 100), 1)

# Random Numbers from Matlab - 
rand_nbs = [[1.01324345095392,-0.142225283569095],
    [0.407344920643207,-0.151153289330984],
    [1.14314593040433,0.318719872913361],
    [-0.853448402446952,-1.11877736557267],
    [-1.13309912333958,0.483345180106232],
    [0.341397730575067,0.508989589576643],
    [0.0498175119356292,-0.854868829818002],
    [-0.951439318747714,0.0357402644626707],
    [-0.0672896257201675,-0.356285396191052],
    [-1.68511345286972,0.849046371733583],
    [0.676759291387555,0.135437683910847],
    [0.256137129570204,0.759927977382943],
    [0.664414127701385,-1.47841589097176],
    [1.17493644019628,0.219831847372367],
    [-0.661590129562252,-1.20538979497377],
    [-0.45175502708869,0.208091637876728],
    [-0.0980938536639713,-0.679038919867732],
    [0.686432233941189,0.636458630901011],
    [1.06463516603529,-0.808282650526677],
    [0.392008134801371,0.0811519196324566],
    [-0.0547560571351863,0.146932270725739],
    [1.15029196280438,-0.229011029944057],
    [-0.402510498759189,1.67881792773982],
    [1.42852448407727,1.23808893154354],
    [-1.18197317843088,-0.662686103970816],
    [-0.235361822006365,-1.99322251427358],
    [-0.401425133041613,-2.23845877545728],
    [-2.30914261567867,-0.860818001414857],
    [-0.754180911273729,-2.12717840498656],
    [-0.139636287156667,-0.245694813800602],
    [-0.462451250610224,0.650783000210527],
    [0.766265809397281,1.48273100479755],
    [-0.527690825871072,0.5689576702246],
    [0.639955180431011,-0.672287960736216],
    [-0.417233981097452,-1.37665909765066],
    [-1.09947730581632,1.22047960886136],
    [1.12202028403938,-0.171468619698071],
    [0.395820934298721,2.81046621555568],
    [-1.01405034998498,-0.0646086198599094],
    [0.258564108227897,-0.571518288520795],
    [-0.0346640460292493,-0.537699007513607],
    [-0.3992497079824,1.43882655065703],
    [-0.60924932586135,-0.690012226637994],
    [0.509389576682374,0.318715070502666],
    [1.02381723196008,2.33602455645169],
    [-0.350474064102046,0.598985751890907],
    [1.41404403584175,0.241508552260953],
    [0.321473516734551,1.19821872203099],
    [1.02052831200169,0.910920022350408],
    [-0.527588016113858,-0.16371200200994],
    [0.54449721756301,0.445351927077147],
    [-1.80482988371221,-0.225746797552568],
    [2.19512788032745,-0.0787849382078636],
    [-0.207959821278037,-0.818672828429031],
    [0.714554753711663,-0.142687092383126],
    [1.25351682614961,-0.210809008352346],
    [0.773500861269606,0.808903722025248],
    [-1.11925058689156,-0.189081009190524],
    [-0.27183872353785,-0.0463393453088817],
    [-0.288876395923868,1.38239118044999],
    [0.384386222202134,0.969852614732045],
    [0.155190310066371,-1.06218180916389],
    [0.0804386563612439,2.40162029078653],
    [1.95740584233107,1.64707486395158],
    [1.95979278879262,-1.03901759257765],
    [2.24328958181418,0.198349066597986],
    [1.13843129392206,0.448170486265491],
    [-0.888835852132315,0.0876338232010184],
    [-1.74920621532156,0.398644808205792],
    [-0.760661674377894,-0.675765712870144],
    [0.707542949204636,0.492586749794515],
    [-0.0649033962224585,-0.0397569610959917],
    [-0.0790601757661689,0.721367071231378],
    [-0.163978074165912,0.948906041915486],
    [1.27171694764777,0.377075931877217],
    [1.02575225809093,0.167857676562958],
    [-0.117641875671809,1.5415572025322],
    [0.522076514442483,0.299562523387065],
    [1.55451111362411,0.150994359739978],
    [-0.220156364751855,-0.0845102140559424],
    [-2.86391118170739,1.49122135530833],
    [1.06650084722725,-0.51971530636786],
    [-3.04614375545796,0.315528559789131],
    [0.185652270058855,1.28583337713792],
    [-0.0832543036536954,-1.47577502381802],
    [-0.311791454070877,-0.997167926287072],
    [-0.673659400121962,0.519440818571086],
    [0.603345759008325,0.635619259407623],
    [1.27688012834029,0.101970476724232],
    [0.559122693322207,0.552007838919491],
    [0.43436725759261,-1.54226471033052],
    [-0.149302239543807,-0.424030281209169],
    [0.991991473021708,-0.99615119018846],
    [0.577261285265419,-0.712566273553651],
    [-2.14033315580991,-1.67488894772361],
    [0.352145450551827,0.262131493990169],
    [0.485832349620454,-0.298310201117196],
    [-0.48766076758097,0.643137681407291],
    [-0.0609415845690305,-1.72661202597394],
    [-0.665612917361851,-0.895132048958458]]
rand_nbs = np.array(rand_nbs)

#%%

# Sample input
spot = 4
mu = 0.02
kappa = 2
v0 = 0.04
theta = 0.04
vv = 0.3
rho = -0.05
T = 1

days = 100
time = np.linspace(0, days, days) / 365

# Set random seed for reproducibility
#np.random.seed(42)

# Normally distributed random numbers for GBM and Heston processes
#rand_nbs = np.random.normal(0, 1, (len(time), 2))


# GBM
y = simulate_gbm(x0=spot, mu=mu, σ=np.sqrt(theta), T=T, dt=1/days, rand_nbs=rand_nbs[:, 0], method=0)

# Heston spot and volatility processes
x = simulate_heston(spot, mu, v0, vv, kappa, theta, rho, T, 1 / days, rand_nbs=rand_nbs, method='quadratic_exponential')

# Plotting
plt.figure(1)

plt.plot(time, y[1:], 'r--', label='GBM')
plt.plot(time, x[1:, 0], 'b', label='Heston')
plt.xlabel('Time [years]')
plt.ylabel('FX rate')
plt.ylim([3.5, 6])
plt.legend(loc=2)


#%%

# GBM vs. Heston volatility
plt.figure(1)
plt.plot(time, 100 * np.sqrt(x[1:, 1]), 'b', label='Heston Volatility')
plt.axhline(y=np.sqrt(theta) * 100, color='r', linestyle='--', label='GBM Volatility')
plt.xlabel('Time [years]')
plt.ylabel('Volatility [%]')
plt.ylim([5, 35])
plt.legend()

plt.show()

