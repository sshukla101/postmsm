################################################################
# Analysis post MSMBuilder                                     #   
# Author: Saurabh Shukla <sshukla4@illinois.edu>               #
# Orginally built for ShuklaGroup@illinois  <shuklagroup.org>  #
################################################################


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from msmbuilder.msm import MarkovStateModel
from msmbuilder.cluster import KMeans
import os
import scipy.sparse, scipy.io
import numpy as np


#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------


################################################################################
# Making clusters with different number of states along with MSM's with 
# different lag times. Saves cluster object; MSM object and timescales pkl files
################################################################################  
def cluster_msm(sequences,n_states, lag_times):
  for n in n_states:
    states = KMeans(n_clusters=n)
    states.fit(sequences)
    io.dump(states,str(n)+'n_cl.pkl')
    ts=np.zeros(5)
    for lag_time in lag_times:
        msm = MarkovStateModel(lag_time=lag_time, verbose=False,n_timescales=5)
        msm.fit(states.labels_)
        ts1=msm.timescales_
        ts=np.vstack((ts,ts1))
        io.dump(msm,str(n)+'n_'+str(lag_time)+'lt_msm.pkl')
    ts=np.delete(ts, (0), axis=0)
    io.dump(ts,str(n)+'n_timescales.pkl')
  
