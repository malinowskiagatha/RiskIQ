#----------------------------------------
#
# Main program
#
#----------------------------------------

#----------------------------------------
#
# Load Dependencies
#
#----------------------------------------

import EquityIQ

#----------------------------------------
#	Initialize data for MSFT stock
#----------------------------------------
msft = EquityIQ.stock('MSFT')  # Create the msft variable type class stock
msft.CalcGreek()      # Calculate greeks by calling CalcGreeks method
msft.GetGreek()       # Send Calculated greeks to terminal 


spy = EquityIQ.stock('spy')
spy.CalcGreek()
spy.GetGreek()

EquityIQ.CalcLinearRegression(msft,spy)  # Calculate linearregression and send results to the terminal 

EquityIQ.DisplayHist(msft,spy)  # Plot histogram for two stocks and send the results to the terminal 

#------------------
# End
#------------------