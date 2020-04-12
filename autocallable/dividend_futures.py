import numpy as np
import pandas as pd
""" Get the data"""

call_put_historical_data=pd.read_csv('OptionHistoricalData.csv')

class DividendFutures(object):
    """Class to handle all the dividend futures calculation, to initiate the Dividend Futures object
        need historical data such as price,date"""

    def __init__(self,historical_data=None):
        """

        :param historical_data: pd.DataFrame
        """

        self.historical_data=historical_data


    def get_synthetic_implied_forward(self,call_put_historical_data,interest_rate):
        """ Method to calculate synthetic forward from call put parity. to perform the calculation
        needed the call historical price, put historical price, and spot historical price

        :param call_put_historical_data: pd.DataFrame
        :param interest_rate: float
        :return: synthetic_forward: pd.DataFrame
        """
        if self.historical_data != None:
            call_put_historical_data=call_put_historical_data[call_put_historical_data['DATE'].isin(self.historical_data['DATE'])]

        else:
            call_put_historical_data["ImpliedForward"] = ((call_put_historical_data['Call']-call_put_historical_data['Put'])*np.exp(interest_rate*call_put_historical_data["TimeToExpiry"]) + call_put_historical_data['Strike'])

        return call_put_historical_data

    def get_syntethic_implied_forward_term_structure(self,call_put_historical_data,interest_rate,date):
        """Method to compute the historical synthetic implied forward term structure """

        df = self.get_synthetic_implied_forward(call_put_historical_data,interest_rate)

        df = df[df["DATE"]==date]

        return df








if __name__=="__main__":
    DivFut=DividendFutures()
    print(DivFut.get_synthetic_implied_forward(call_put_historical_data,0.02))
