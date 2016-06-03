################################################################
# Analysis post MSMBuilder                                     #   
# Author: Saurabh Shukla <sshukla4@illinois.edu>               #
# Orginally built for ShuklaGroup@illinois  <shuklagroup.org>  #
################################################################


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import numpy as np
from matplotlib import pyplot as plt





#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
def free_energy_plot(data1,data2,eqm_prob):
  """Plotting weighted free energy landscape.
  
  Args:
    data1(list of arrays): First metric for landscape
    data2 (list of arrays): Second metric for landscape
    eqm_probability (array): array corresponding to equilibrium probability of each state
  """
  
  
