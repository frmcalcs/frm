# -*- coding: utf-8 -*-
import os
if __name__ == "__main__":
    os.chdir(os.environ.get('PROJECT_DIR_FRM')) 

from frm.pricing_engine.garman_kohlhagen import gk_price, gk_solve_strike


def test_gk_price():

    epsilon = 0.0006 # 0.06% of notional
    
    ##### AUDUSD Tests, function results in USD per 1 AUD ######
    
    # 1Y AUDUSD Call, 30 June 2023, London 8am
    px_test = 0.00133006 # 1330.06 USD per A$1,000,000 notional
    S0=00.6629
    σ=0.098408
    r_d=0.05381
    r_f=0.0466
    tau=1.0
    cp=1
    K=0.7882
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']
    assert abs(px_test - px) < epsilon
    
    # 1Y AUDUSD Put, 30 June 2023, London 8am
    px_test = 0.11533070 # 115,330.7 USD per A$1,000,000 notional
    S0=0.662866
    σ=0.0984338
    r_d=0.05381
    r_f=0.0466
    tau=1.0
    cp=-1
    K=0.7882
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']
    assert abs(px_test - px) < epsilon
    
    # 1Y AUDUSD Call, 30 June 2023, London 8am
    px_test = 0.12284766 
    S0=0.662866
    σ=0.1354523
    r_d=0.05381
    r_f=0.0466
    tau=1.0
    cp=1
    K=0.5405
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']     
    assert abs(px_test - px) < epsilon  
          
    # 1Y AUDUSD Put, 30 June 2023, London 8am
    px_test = 0.00200167
    S0=0.662866
    σ=0.1354523
    r_d=0.05381
    r_f=0.0466
    tau=1.0
    cp=-1
    K=0.5405
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']           
    assert abs(px_test - px) < epsilon     
      
    
    ##### AUDUSD Tests, function results in AUD per 1 USD ######
    
    # 1Y USDAUD Put, 30 June 2023, London 8am
    px_test = 0.00133006
    S0=1/0.662866
    σ=0.0984338
    r_d=0.0466
    r_f=0.05381
    tau=1.0
    cp=-1
    K=1/0.7882
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']    
    px_in_AUD_per_1_AUD = px / S0 / K
    assert abs(px_test - px_in_AUD_per_1_AUD) < epsilon
    
    # 1Y USDAUD Call, 30 June 2023, London 8am
    px_test = 0.11533070 
    S0=1/0.662866
    σ=0.0984338
    r_d=0.0466
    r_f=0.05381
    tau=1.0
    cp=1
    K=1/0.7882
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']      
    px_in_AUD_per_1_AUD = px / S0 / K
    assert abs(px_test - px_in_AUD_per_1_AUD) < epsilon

    # 1Y USDAUD Put, 30 June 2023, London 8am
    px_test = 0.12284766
    S0=1/0.662866
    σ=0.1354523
    r_d=0.0466
    r_f=0.05381
    tau=1.0
    cp=-1
    K=1/0.5405
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']        
    px_in_AUD_per_1_AUD = px / S0 / K
    assert abs(px_test - px_in_AUD_per_1_AUD) < epsilon 

    # 1Y USDAUD Call, 30 June 2023, London 8am
    px_test = 0.00200167
    S0=1/0.662866
    σ=0.1354523
    r_d=0.0466
    r_f=0.05381
    tau=1.0
    cp=1
    K=1/0.5405
    px = gk_price(S0=S0,tau=tau,r_f=r_f,r_d=r_d,cp=cp,K=K,σ=σ)['option_value']    
    px_in_AUD_per_1_AUD = px / S0 / K
    assert abs(px_test - px_in_AUD_per_1_AUD) < epsilon


def test_gk_solve_strike():
    
    epsilon = 0.001 # 0.1 % 

    # AUDUSD 1Y 30 Δ Put, 30 June 2023 London 10pm 
    strike_test = 0.64100
    S0=0.6662
    σ=0.1064786
    r_f=0.04655
    r_d=0.05376
    tau=1.0
    Δ = -0.3
    Δ_convention = 'regular_spot_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon

    # AUDUSD 1Y 30 Δ Call, 30 June 2023 London 10pm 
    strike_test = 0.70690
    S0=0.6662
    σ=0.0963895
    r_f=0.04655
    r_d=0.05376
    tau=1.0
    Δ = 0.3
    Δ_convention = 'regular_spot_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon

    # AUDUSD 1Y 5 Δ Put, 30 June 2023 London 10pm 
    strike_test = 0.54280
    S0=0.6662
    σ=0.1359552
    r_f=0.04655
    r_d=0.05376
    tau=1.0
    Δ = -0.05
    Δ_convention = 'regular_spot_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon


    # AUDUSD 1Y 5 Δ Call, 30 June 2023 London 10pm 
    epsilon = 0.0015 # 0.15 % higher tolerance for this one 
    strike_test = 0.79300
    S0 = 0.6662
    σ = 0.0990869
    r_f = 0.04655
    r_d = 0.05376
    tau = 1.0
    Δ = 0.05
    Δ_convention = 'regular_spot_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon
    
    # AUDUSD 5Y 30 Δ Put, 30 June 2023 London 10pm 
    epsilon = 0.0034 # 0.34 % higher tolerance for this one 
    strike_test = 0.59180
    S0 = 0.6662
    σ = 0.1161961
    r_f = 0.04287
    r_d = 0.03902
    tau = 5.0
    Δ = -0.3
    Δ_convention = 'regular_forward_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon
    
    # AUDUSD 5Y 30 Δ Put, 30 June 2023 London 10pm 
    epsilon = 0.0036 # 0.36 % higher tolerance for this one 
    strike_test = 0.75820
    S0 = 0.6662
    σ = 0.1016627
    r_f = 0.04287
    r_d = 0.03902
    tau = 5.0
    Δ = 0.3
    Δ_convention = 'regular_forward_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon


    epsilon = 0.001
    
    # 2Y USDJPY call, (USD call, JPY Put), 30 June 2023, London 10pm data
    strike_test = 145.83
    S0 = 144.32 # 20 Δ Call
    σ = 0.0960777
    r_f = 0.04812
    r_d = -0.00509
    tau = 2.0
    F = 129.7958
    Δ = 0.2
    Δ_convention = 'premium_adjusted_forward_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention)
    assert abs(strike_test - strike) / strike_test < epsilon
    
    # 9M USDJPY call, (USD call, JPY Put), 30 June 2023, London 10pm data
    strike_test = 148.11
    S0 = 144.32 # 20 Δ Call
    σ = 0.0985008
    r_f = 0.05413
    r_d = -0.00528
    tau = 0.75
    F = 138.031
    Δ = 0.2
    Δ_convention = 'premium_adjusted_spot_Δ'
    strike = gk_solve_strike(S0=S0,tau=tau,r_f=r_f,r_d=r_d,σ=σ,Δ=Δ,Δ_convention=Δ_convention, F=F)
    assert abs(strike_test - strike) / strike_test < epsilon
        
        
def test_gk_price_greeks():
    
    # 1Y AUDUSD Call, data from 30 June 2023, London 8am
    S0=0.6629
    σ=9.84251/100
    r_f=0.0466
    r_d=0.05381
    tau=1.0
    cp=1
    K=0.7882
    F=0.667962
    result = gk_price(S0=S0, tau=tau, r_f=r_f, r_d=r_d, cp=cp, K=K, σ=σ, F=F, analytical_greeks_flag=True, numerical_greeks_flag=True)    
    #print('X:',X)
    #print('greeks_analytical:',greeks_analytical)   
    #print('greeks_numerical:',greeks_numerical)   


        
        

if __name__ == '__main__':
    test_gk_price()
    test_gk_solve_strike()
        
    S0=0.6629
    σ=0.0984688
    r_f=0.0466
    r_d=0.05381
    tau= 1.00957592339261
    cp=1
    K=0.7882
    F=0.667962
    result  = gk_price(S0=S0, tau=tau, r_f=r_f, r_d=r_d, cp=cp, K=K, σ=σ, F=F, analytical_greeks_flag=True, numerical_greeks_flag=True)    

    
    