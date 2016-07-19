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
f=open('pyl5_inactive_cpptraj1.in','wb')
f.write('parm '+top_address+'\n')

n=len(inactive_traj)
for i in range(0,n):
  f.write('trajin '+inactive_traj[i]+'\n')

f.write('reference pyl5_inactive.rst'+'\n')
f.write('rmsd :1-73,84-166@CA,C,O,N reference'+'\n')
f.write('rmsd :74-83&!@H= reference nofit out rmsd_cl2_inactive_from_inactive_pyl5.dat'+'\n')
f.write('atomicfluct out rmsf_pyl5_inactive_full_resid.dat :1-166 byres'+'\n')
f.write('atomicfluct out rmsf_pyl5_inactive_backbone.dat :1-166@CA,C,O,N byres'+'\n')
f.write('radgyr out gyr_all_pyl5_inactive.dat :1-166 mass nomax'+'\n')
f.write('radgyr out gyr_binding_pocket_pyl5_inactive.dat :47,50-54,71,73-84,86,100,102,105-110,112,114,116,130,132,134,148-149,152,155,157,158 mass nomax'+'\n')
f.write('strip :A8S'+'\n')
f.write('surf out surf_pyl5_inactive.dat'+'\n')
f.close()

#for rmsd from active
f=open('pyl5_inactive_cpptraj2.in','wb')
f.write('parm '+top_address+'\n')

n=len(inactive_traj)
for i in range(0,n):
  f.write('trajin '+inactive_traj[i]+'\n')

f.write('reference pyl5_active.rst'+'\n')
f.write('rmsd :1-73,84-166@CA,C,O,N reference'+'\n')
f.write('rmsd :74-83&!@H= reference nofit out rmsd_cl2_inactive_from_active_pyl5.dat'+'\n')
f.close()



#-----------------------------------------------------------------------------
# Calculations on active trajectories
run_address='/home/sshukla4/pyl5/apo_aba/prod/apo_holo_analysis'
os.chdir(run_address)
f=open('pyl5_active_cpptraj1.in','wb')
f.write('parm '+top_address+'\n')

n=len(active_traj)
for i in range(0,n):
  f.write('trajin '+active_traj[i]+'\n')

f.write('reference pyl5_inactive.rst'+'\n')
f.write('rmsd :1-73,84-166@CA,C,O,N reference'+'\n')
f.write('rmsd :74-83&!@H= reference nofit out rmsd_cl2_active_from_inactive_pyl5.dat'+'\n')
f.write('atomicfluct out rmsf_pyl5_active_full_resid.dat :1-166 byres'+'\n')
f.write('atomicfluct out rmsf_pyl5_active_backbone.dat :1-166@CA,C,O,N byres'+'\n')
f.write('radgyr out gyr_all_pyl5_active.dat :1-166 mass nomax'+'\n')
f.write('radgyr out gyr_binding_pocket_pyl5_active.dat :47,50-54,71,73-84,86,100,102,105-110,112,114,116,130,132,134,148-149,152,155,157,158 mass nomax'+'\n')
f.write('strip :A8S'+'\n')
f.write('surf out surf_pyl5_active.dat'+'\n')
f.close()

#for rmsd from active
f=open('pyl5_active_cpptraj2.in','wb')
f.write('parm '+top_address+'\n')

n=len(active_traj)
for i in range(0,n):
  f.write('trajin '+active_traj[i]+'\n')

f.write('reference pyl5_active.rst'+'\n')
f.write('rmsd :1-73,84-166@CA,C,O,N reference'+'\n')
f.write('rmsd :74-83&!@H= reference nofit out rmsd_cl2_active_from_active_pyl5.dat'+'\n')
f.close()
