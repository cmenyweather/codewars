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

    # conditional to validate cents is an integer or float
    if isinstance(cents, (float,int)) != True:
        raise ValueError('Integer or float expected error')
    else:
        """if cents is a negative integer, return dictionary with all values
        set to 0"""
        if cents < 0:
            change_dict = {
                           'Nickels': 0,
                           'Pennies': 0,
                           'Dimes': 0,
                           'Quarters': 0
                          }
        else:
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
                            change_dict = {
                                           'Nickels': div_nickels[0],
                                           'Pennies': div_pennies[0],
                                           'Dimes': div_dimes[0],
                                           'Quarters': div_quarters[0]
                                          }
                    else:
                        """least amount of coins is by using quarters and dimes
                        and nickels"""
                        change_dict = {
                                       'Nickels': div_nickels[0],
                                       'Pennies': 0,
                                       'Dimes': div_dimes[0],
                                       'Quarters': div_quarters[0]
                                      }
                else:
                    # least amount of coins is by using quarters and dimes
                    change_dict = {
                                   'Nickels': 0,
                                   'Pennies': 0,
                                   'Dimes': div_dimes[0],
                                   'Quarters': div_quarters[0]
                                  }
            else:
                # least amount of coins is by using quarters only
                change_dict = {
                               'Nickels': 0,
                               'Pennies': 0,
                               'Dimes': 0,
                               'Quarters': div_quarters[0]
                              }
        # function complete, return the dictionary
        return change_dict
