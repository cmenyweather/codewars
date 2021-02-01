"""import the floor method from math so we can round a float down to the
nearest integer"""
from math import floor

def loose_change(cents):
    '''Take an amount of US currency in cents and return a dictionary
    which shows the least amount of coins to make up that amount'''
    # set constant variables - coins for calcuation
    QUARTERS = 25
    DIMES = 10
    NICKELS = 5
    PENNIES = 1

    # set all coin quantities to 0
    nickels_qty = pennies_qty = dimes_qty = quarters_qty = 0

    # conditional to validate cents is an int or float
    if isinstance(cents, (float,int)) != True:
        raise ValueError('Integer or float expected error')
    else:
        # if cents is a positive int or float start calculation
        if cents > 0:
            # if cents is a float > 0, round cents down to nearest integer
            if isinstance(cents, float) == True:
                cents = floor(cents)
            # use built-in divmod function to calculate quotient and remainder
            # calculate with QUARTERS
            div_quarters = divmod(cents, QUARTERS)
            # set qaurters quantity
            quarters_qty = div_quarters[0]
            # calculate with DIMES
            div_dimes = divmod(div_quarters[1], DIMES)
            # set dimes quantity
            dimes_qty = div_dimes[0]
            # calculate with NICKELS
            div_nickels = divmod(div_dimes[1], NICKELS)
            # set nickels quantity
            nickels_qty = div_nickels[0]
            # calculate with PENNIES
            div_pennies= divmod(div_nickels[1], PENNIES)
            # set pennies quantity
            pennies_qty = div_pennies[0]
            # confirm no remainder left
            if div_pennies[1] > 0:
                raise Exception('Should be no remainder now')

    # coin quantities finalised so update the dictionary
    change_dict = {
                  'Nickels': nickels_qty,
                  'Pennies': pennies_qty,
                  'Dimes': dimes_qty,
                  'Quarters': quarters_qty
                  }
    # function complete, return the dictionary
    return change_dict
