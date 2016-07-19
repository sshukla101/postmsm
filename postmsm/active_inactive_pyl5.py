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

#PYL5 aorund 1 except 7th parallel round are inactive 
# Round 2 is ABA bound (We take only 25 out of the 50 parallel rounds to equalize the simulation time)

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
traj_list=traj_list_maker('/home/sshukla4/pyl5/apo_aba/prod/msm/trajs/','mdcrd')
top_address='/home/sshukla4/pyl5/apo_aba/prod/msm/trajs/stripped.apo_aba.top'

inactive_traj=traj_list[0:49]
del inactive_traj[6]
active_traj=traj_list[49:73]


#-----------------------------------------------------------------------------
# Calculations on Inactive trajectories
run_address='/home/sshukla4/pyl5/apo_aba/prod/apo_holo_analysis'
os.chdir(run_address)
f=open('pyl5_inactive_cpptraj.in','wb')
f.write('parm '+top_address+'\n')

n=len(inactive_traj)
for i in range(0,n):
  f.write('trajin '+inactive_traj[i]+'\n')

f.write('reference ref_inactive.rst'+'\n')
f.write('rmsd :1-68,79-171@CA,C,O,N reference'+'\n')
f.write('rmsd :69-78&!@H= reference nofit out rmsd_cl2_inactive_pyl10.dat'+'\n')
f.write('average avg_inactive.pdb pdb'+'\n')
f.write('atomicfluct out rmsf_pyl10_inactive.dat :1-171 byres'+'\n')
f.write('radgyr out gyr_all_pyl10_inactive.dat :1-171 mass nomax'+'\n')
f.write('radgyr out gyr_binding_pocket_pyl10_inactive.dat :43,46,47-50,66,68-71,74-79,81,95,97,100-104,107,109,111,128,130,132,146-148,150,151,154,155 mass nomax'+'\n')
f.write('strip :A8S'+'\n')
f.write('surf out surf_pyl10_inactive.dat'+'\n')
f.close()



#-----------------------------------------------------------------------------
# Calculations on active trajectories
run_address='/home/sshukla4/pyl5/apo_aba/prod/apo_holo_analysis'
os.chdir(run_address)
f=open('pyl5_active_cpptraj.in','wb')
f.write('parm '+top_address+'\n')


n=len(active_traj)
for i in range(0,n):
  f.write('trajin '+active_traj[i]+'\n')

f.write('reference ref_active.rst'+'\n')
f.write('rmsd :1-68,79-171@CA,C,O,N reference'+'\n')
f.write('rmsd :69-78&!@H= reference nofit out rmsd_cl2_active_pyl10.dat'+'\n')
f.write('average avg_active.pdb pdb'+'\n')
f.write('atomicfluct out rmsf_pyl10_active.dat :1-171 byres'+'\n')
f.write('radgyr out gyr_all_pyl10_active.dat :1-171 mass nomax'+'\n')
f.write('radgyr out gyr_binding_pocket_pyl10_active.dat :43,46,47-50,66,68-71,74-79,81,95,97,100-104,107,109,111,128,130,132,146-148,150,151,154,155 mass nomax'+'\n')
f.write('strip :A8S'+'\n')
f.write('surf out surf_pyl10_active.dat'+'\n')
f.close()
