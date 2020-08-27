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


    def price(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.type =='Call' or self.type =="C":
            call=st.norm.cdf(d1,0,1)*self.underlying - self.discount_factor*self.strike*st.norm.cdf(d2,0,1)
            return call
        else:
            put=st.norm.cdf(-d2,0,1)*self.strike*self.discount_factor-st.norm.cdf(-d1,0,1)*self.underlying
            return put

    def delta(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        if self.type =="Call" or self.type == "C":
            deltaBS=st.norm.cdf(d1,0,1)
            return (deltaBS)
        else:
            deltaBS=st.norm.cdf(-d1,0,1)
            return(deltaBS)

    def vega(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        vega_value=self.underlying*st.norm.cdf(d1,0,1)*m.sqrt(self.T)
        return vega_value

    def implied_vol(self,option_mkt_price,vol_est):
        print((self.price(vol_est),self.delta(vol_est),self.vega(vol_est)))
        i=1
        while(i<=100):
            vol_est=vol_est-((self.price(vol_est)-option_mkt_price)/self.vega(vol_est))
            if abs(self.price(vol_est)-option_mkt_price) <= 0.0001:
                print("Numbers of attemps:",i)
                print("Implied_Vol:",vol_est)
                return vol_est
            else:
                i=i+1

    def volga(self,vol):
        Vega=self.vega(vol)
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                    vol * m.sqrt(self.T))
        d2 = d1 - (vol) * m.sqrt(self.T)
        volga=Vega*(d1*d2)/vol
        return(volga)


    def vanna(self,vol):
        d1 = (m.log(self.underlying / self.strike) + (self.rate + 0.5 * vol ** 2) * self.T) / (
                vol * m.sqrt(self.T))
        dNorm=m.exp(-0.5*d1**2)*(1/2*m.pi)
        vanna=m.sqrt(self.T)*dNorm*(1-d1)
        return(vanna)









