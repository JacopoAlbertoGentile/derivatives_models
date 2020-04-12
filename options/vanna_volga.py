import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy.stats as st
from BlackScholes import *
import matplotlib.pyplot as plt


#set the strike and ivols in other words create the Ivol_surface
b1=(0.30,150,75)
b2=(0.25,200,70)
b3=(0.27,250,73)

#Implement the Vol-Vega model
Call1=BlackScholes(150,200,0.02, "2019-12-18", "Call")
Call2=BlackScholes(200,200,0.02,"2019-12-18",'Call')
Call3=BlackScholes(300,200,0.02,"2019-12-18","Call")

Bs_Iv=0.25

PriceCall1=Call1.Price(Bs_Iv)
PriceCall2=Call2.Price(Bs_Iv)
PriceCall3=Call3.Price(Bs_Iv)

print([PriceCall1,PriceCall2,PriceCall3])
#Calculating Weights in Vanna-Volga framework

weight1=(Call2.Vega(Bs_Iv)/Call1.Vega(Bs_Iv))*((math.log(b2[1]/b2[1])*math.log(b3[1]/b2[1]))/(math.log(b2[1]/b1[1])*math.log(b3[1]/b1[1])))
weight2=(Call2.Vega(Bs_Iv)/Call2.Vega(Bs_Iv))*((math.log(b2[1]/b1[1])*math.log(b3[1]/b2[1]))/(math.log(b2[1]/b1[1])*math.log(b3[1]/b2[1])))
weight3=(Call2.Vega(Bs_Iv)/Call3.Vega(Bs_Iv))*((math.log(b2[1]/b1[1])*math.log(b2[1]/b2[1]))/(math.log(b3[1]/b1[1])*math.log(b3[1]/b2[1])))

print([weight1,weight2,weight3])
print(PriceCall2)


OptionsBS=BlackScholes(200,200,0.02,"2019-12-18",'Call')
print(OptionsBS.Price(Bs_Iv))
Option=OptionsBS.Price(Bs_Iv)+weight2*(b2[2]-PriceCall2)


class Vanna_Volga(BlackScholes):
    def __init__(self,strike, underlying, rate, T, type, vol=None):
        BlackScholes.__init__(self,strike ,underlying ,rate , T , type ,vol=None)



    def BSPrices(self,vol,strikes):
        initial_strike=self.strike
        Options={}
        for i in strikes:
            self.strike=i

            Options[i]=self.Price(vol)
        self.strike=initial_strike
        return(Options)

    #def Weights(self,target_strike,vol):




if __name__=="__main__":
    A=Vanna_Volga(12,10,0.02,"2019-12-20",'Call')
    print(A.BSPrices(0.25,[9,10,11]))
    print(A.strike)
    B=BlackScholes(12,10,0.02,"2019-12-20",'Call')
    print(B.Price(0.25))

