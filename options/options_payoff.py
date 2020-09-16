def call_payoff(strike, premium,underlying_price):
    if premium > 0:
        payoff = (underlying_price - strike) - premium
        if payoff > 0:
            return payoff
        else:
            return 0
    else:
        payoff = - premium - (underlying_price - strike)
        if underlying_price > strike:
            return payoff
        else:
            return -payoff

def put_payoff(strike, premium, underlying_price):
    if premium > 0:
        payoff = (strike - underlying_price) - premium
        if payoff > 0:
            return payoff
        else:
            return 0
    else:
        payoff = -premium - (strike - underlying_price)
        if strike > underlying_price:
            return payoff
        else:
            return -premium


