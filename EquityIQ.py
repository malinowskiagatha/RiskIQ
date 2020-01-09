#-------------------------------------------------------
#	Load all dependencies
#-------------------------------------------------------	
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import statsmodels.api as sm


class stock:


#---------------------------------------------------------------------------------------------
#	Initialiaze the stock class and load data from predefined CSV file
#   Path defining location of the data files can be adjusted using path vatiable.
#    Default path is the location of the PY file. 
#---------------------------------------------------------------------------------------------
	def __init__(self, symbol):
		path = ""
		self.symbol = symbol.upper()
		if self.symbol == 'MSFT':
			self.hdt = pd.read_csv(path + "msft.csv", sep=',')
		elif self.symbol == 'SPY':
			self.hdt = pd.read_csv(path + "spy.csv", sep=',')
		else: 
			print ('Incorrect security. EXITING')
	
#-------------------------------------------------------
#	Create a daliy return based on the Adjusted Close
#-------------------------------------------------------
	def CalcDailyReturns(self):
		self.dailyreturn = self.hdt['Adj Close'].pct_change()
		
#-------------------------------------------------------
#	Calculate mean based on daily return
#-------------------------------------------------------		
	def CalcMean(self):
		self.mean = self.dailyreturn.mean()

#-------------------------------------------------------
#	Calculate standard deviation based on daily return
#-------------------------------------------------------		
	def CalcStDev(self):
		self.stdev = self.dailyreturn.std()
		
#-------------------------------------------------------
#	Calculate Sharpe Ratio based on daily return
#-------------------------------------------------------
	def CalcSharpeRatio(self):
		self.sharperatio = self.mean / self.stdev

#-------------------------------------------------------
#	Calculate Kurtosis based on daily return
#-------------------------------------------------------
	def CalcKurtosis(self):
		self.kurtosis = self.dailyreturn.kurtosis()

#-------------------------------------------------------
#	Calculate Skewness based on daily return
#-------------------------------------------------------
	def CalcSkwness(self):
		self.skewness = self.dailyreturn.skew()

#-------------------------------------------------------
#	Calculate variance based on daily return
#-------------------------------------------------------		
	def CalcVariance(self):
		self.variance = self.dailyreturn.var()

#-------------------------------------------------------
#	Calculate 95% variance based on daily return
#-------------------------------------------------------		
	def CalcVaR95(self):
		self.var95 = self.dailyreturn.quantile(0.05)
	
#-------------------------------------------------------
#	Calculate Greeks defined in the stock class
#-------------------------------------------------------
	def CalcGreek(self):
		self.CalcDailyReturns()
		self.CalcMean()
		self.CalcStDev()
		self.CalcSharpeRatio()
		self.CalcKurtosis()
		self.CalcSkwness()
		self.CalcVariance()
		self.CalcVaR95()


#----------------------------------------------------------------
#	Dispalys available Greeks calculated for by CalcGreek method
#----------------------------------------------------------------		
	def GetGreek(self):
		print(self.symbol)
		print('--------------------------------------')
		print('Mean:         ',self.mean)
		print('StDev:        ',self.stdev)
		print('Sharpe Ratio: ',self.sharperatio)
		print('Kurtosis:     ',self.kurtosis)
		print('Skewness:     ',self.skewness)
		print('Variance:     ',self.variance)
		print('VaR 95%:      ',self.var95)
		print('--------------------------------------')
		print('')
		print('')
			

#--------------------------------------------------------------------
#	Calculate and diplay Linear Regression for two stocks st1 and st2
#--------------------------------------------------------------------
def CalcLinearRegression(st1, st2):
	x = np.array(st1.dailyreturn[1:])
	y = np.array(st2.dailyreturn[1:])

	mod = sm.OLS(y, x)
	res = mod.fit()
	print(res.summary())
		
#-----------------------------------------------------------
#	Create and display histogram for two stocks st1 and st2 
#-----------------------------------------------------------
		
def DisplayHist(st1, st2):
	fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True)
	
	st1.dailyreturn.plot.hist(ax = axes[0], grid=True, bins=10, rwidth=0.95,color='#607c8e')
	st2.dailyreturn.plot.hist(ax = axes[1], grid=True, bins=10, rwidth=0.95,color='#607c8e')
	axes[0].set_title(st1.symbol.upper())
	axes[0].set_xlabel('Daily Return')
	axes[1].set_title(st2.symbol.upper())
	axes[1].set_xlabel('Daily Return')
	plt.show()