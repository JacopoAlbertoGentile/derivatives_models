import numpy as np
import datetime as dt
import math as m
import scipy.stats as st


class BlackScholes(object):
    def __init__(self, strike ,underlying ,rate , T , type ,vol=None):
        self.strike=strike
        self.underlying=underlying
        self.vol = vol
        self.rate = rate
        self.type = type
        today=dt.datetime.today()
        T=dt.datetime.strptime(T,"%Y-%m-%d")
        T=(T-today).days/252
        self.T=T
        self.discount_factor=m.exp(-self.rate*self.T)
        self.d1=None
        self.d2=None


    def Price(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.type =='Call' or self.type =="C":
            call=st.norm.cdf(d1,0,1)*self.underlying - self.discount_factor*self.strike*st.norm.cdf(d2,0,1)
            return call
        else:
            put=st.norm.cdf(-d2,0,1)*self.strike*self.discount_factor-st.norm.cdf(-d1,0,1)*self.underlying
            return put

    def Delta(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.type =="Call" or self.type == "C":
            deltaBS=st.norm.cdf(d1,0,1)
            return (deltaBS)
        else:
            deltaBS=st.norm.cdf(-d1,0,1)
            return(deltaBS)

    def Vega(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        vega=self.underlying*st.norm.cdf(d1,0,1)*m.sqrt(self.T)
        return(vega)

    def ImpliedVol(self,Quote,vol_est):
        print((self.Price(vol_est),self.Delta(vol_est),self.Vega(vol_est)))
        i=1
        while(i<=100):
            vol_est=vol_est-((self.Price(vol_est)-Quote)/self.Vega(vol_est))
            if abs(self.Price(vol_est)-Quote) <= 0.0001:
                print("Numbers of attemps:",i)
                print("Implied_Vol:",vol_est)
                return vol_est
            else:
                i=i+1

    def Volga(self,vol):
        Vega=self.Vega(vol)
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        volga=Vega*(d1*d2)/vol
        return(volga)


    def Vanna(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        dNorm=m.exp(-0.5*d1**2)*(1/2*m.pi)
        vanna=m.sqrt(self.T)*dNorm*(1-d1)
        return(vanna)










#if __name__== "__main__":
    #A=BlackScholes(3,5,0.02, "2019-09-18", "Put")
    #print(A.Price(0.4136),A.Delta(0.4136),A.Vega(0.4136))
    #print(A.ImpliedVol(0.3,0.3))
    #print(A.Vanna(0.25))
    #print(A.Volga(0.25))
    #for i in range(10,100):
        #A.underlying=i
        #print(A.Vanna(0.25))



