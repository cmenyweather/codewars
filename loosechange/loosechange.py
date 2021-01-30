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

    # dictionary that will be returned
    change_dict = {}

    # conditional to validate cents is an int or float
    if isinstance(cents, (float,int)) != True:
        raise ValueError('Integer or float expected error')
    else:
        # set all coin quantities to 0
        nickels_qty = pennies_qty = dimes_qty = quarters_qty = 0
        # if cents is a positive int or float start calculation
        if cents > 0:
            # if cents is a float > 0, round cents down to nearest integer
            if isinstance(cents, float) == True:
                cents = floor(cents)
            # use built-in divmod function to calculate quotient and remainder
            # calculate with QUARTERS
            div_quarters = divmod(cents, QUARTERS)
            # print(div_quarters)
            # calculate with DIMES
            if div_quarters[1] > 0:
                div_dimes = divmod(div_quarters[1], DIMES)
                # print(div_dimes)
                # calculate with NICKELS
                if div_dimes[1] > 0:
                    div_nickels = divmod(div_dimes[1], NICKELS)
                    # print(div_nickels)
                    # calculate with PENNIES
                    if div_nickels[1] > 0:
                        div_pennies= divmod(div_nickels[1], PENNIES)
                        # print(div_nickels)
                        # confirm no remainder left
                        if div_pennies[1] > 0:
                            raise Exception('Should be no remainder now')
                        else:
                            """least amount of coins is by using quarters and
                            dimes and nickels and pennies"""
                            nickels_qty = div_nickels[0]
                            pennies_qty = div_pennies[0]
                            dimes_qty = div_dimes[0]
                            quarters_qty = div_quarters[0]
                    else:
                        """least amount of coins is by using quarters and dimes
                        and nickels"""
                        nickels_qty = div_nickels[0]
                        dimes_qty = div_dimes[0]
                        quarters_qty = div_quarters[0]
                else:
                    # least amount of coins is by using quarters and dimes
                    dimes_qty = div_dimes[0]
                    quarters_qty = div_quarters[0]
            else:
                # least amount of coins is by using quarters only
                quarters_qty = div_quarters[0]
        # coin quantities finalised so let's update the dictionary
        change_dict = {
                      'Nickels': nickels_qty,
                      'Pennies': pennies_qty,
                      'Dimes': dimes_qty,
                      'Quarters': quarters_qty
                      }
        # function complete, return the dictionary
        return change_dict
