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
import numpy as np
from random import randint
import pytraj as pt
import glob


#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

#PYL10 round 1,2,3 are inactive
# PYL210 round 10,11 are ABA bound
# We need to assess the properties of active vs inactive PYLs. 

#-----------------------------------------------------------------------------
def traj_list_maker(address,extension):     #Function for making list of "trajectory addresses"
  import re
  numbers = re.compile(r'(\d+)')
  def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
  T=[]
  for traj in sorted(glob.glob(address+'*.'+extension),key=numericalSort):
    T.append(traj)
  return T

#-----------------------------------------------------------------------------
traj_list=traj_list_maker('/home/sshukla4/pyl10/msm/trajs/','mdcrd')
top_address='/home/sshukla4/pyl10/msm/trajs/stripped.apo_aba.top'

inactive_traj=traj_list[0:90]
active_traj=traj_list[536:576]


#-----------------------------------------------------------------------------
os.chdir(run_address)
f=open('pyl10_inactive_rmsd.in','wb')
f.write('parm '+top_address+'\n')

for i in range(0,n):
  f.write('trajin '+address+str(i)+'cluster.mdcrd'+'\n')

f.write('reference ref_inactive.rst'+'\n')
f.write('rmsd :1-171@CA,C,O,N reference'+'\n')
f.write('rmsd :69-78&!@H= reference nofit out pyl10_holo_rmsd.dat'+'\n')
