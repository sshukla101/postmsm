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
# Calculations on Inactive trajectories
run_address='/home/sshukla4/pyl10/apo_holo_analysis/'
os.chdir(run_address)
f=open('pyl10_inactive_cpptraj.in','wb')
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
run_address='/home/sshukla4/pyl10/apo_holo_analysis/'
os.chdir(run_address)
f=open('pyl10_active_cpptraj.in','wb')
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


#-----------------------------------------------------------------------------
# Calculations of solvated inactive trajectories
import numpy as np
import os
import os.path

rounds=9
parallel_traj=[20,50,20,16,16,100,16,100,200]
seq_traj=[6,3,1,1,1,5,1,3,2]
address='/home/sshukla4/pyl10/'


f=open('solvation_inactive_pyl10.in','wb')

f.write(' parm /home/sshukla4/pyl10/round1/apo_aba.top'+ '\n')
for i in range(0,2):
  for j in range(0,parallel_traj[i]):
    for k in range(0,seq_traj[i]):
      if os.path.isfile(address+'round'+str(i+1)+'/traj_files/par'+str(j+1)+'_sim'+str(k+1)+'.mdcrd')== True:
        f.write('trajin '+address+'round'+str(i+1)+'/traj_files/par'+str(j+1)+'_sim'+str(k+1)+'.mdcrd 1 last 6'+'\n')
      else:
        pass
f.write('watershell :A8S watershell_pyl10_inactive.dat W1 lower 3.0 upper 5.0'+ '\n')
f.close()

#round 3 is run is shadowfax; needs different kind of processing for wirting files.
i=3
par=20
f=open('solvation_inactive_pyl10_2.in','wb')
for j in range(0,par):
  f.write('trajin '+address+'round'+str(i)+'/traj_files/par'+str(j+1)+'.mdcrd 1 last 6'+'\n')
f.close()



# Calculations of solvated inactive trajectories
import numpy as np
import os
import os.path

rounds=[9,10]
parallel_traj=[20,20]
seq_traj=[5,3]
address='/home/sshukla4/pyl10/'


f=open('solvation_active_pyl10.in','wb')
f.write(' parm /home/sshukla4/pyl10/round1/apo_aba.top'+ '\n')
for i in range(0,len(rounds)):
  for j in range(0,parallel_traj[i]):
    for k in range(0,seq_traj[i]):
      if os.path.isfile(address+'round'+str(rounds[i]+1)+'/traj_files/par'+str(j+1)+'_sim'+str(k+1)+'.mdcrd')== True:
        f.write('trajin '+address+'round'+str(rounds[i]+1)+'/traj_files/par'+str(j+1)+'_sim'+str(k+1)+'.mdcrd 1 last 6'+'\n')
      else:
        pass
f.write('watershell :A8S watershell_pyl10_active.dat W1 lower 3.0 upper 5.0'+ '\n')

f.close()


#-----------------------------------------------------------------------------------
# Calculations of Lys and ser distance from ABA in inactive and active trajectories.
from msmbuilder.utils import io
#in shadowfax
lys=io.load('/home/sshukla4/pyl10/msm/rmsd_dist/dist_data/aba_lys_dist.pkl')
ser=io.load('/home/sshukla4/pyl10/msm/rmsd_dist/dist_data/cl2_ser_aba.pkl')

inactive_lys=lys[0:90]
active_lys=lys[536:576]
inactive_ser=ser[0:90]
active_ser=ser[536:576]

#In lab mac
os.chdir('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Papers/ABA_binding/figures/active_inactive/pyl10')

inactive_lys=io.load('inactive_lys_aba_pyl10.pkl')
active_lys=io.load('active_lys_aba_pyl10.pkl')
inactive_ser=io.load('inactive_ser_aba_pyl10.pkl')
active_ser=io.load('active_ser_aba_pyl10.pkl')



for i in range(0,len(inactive_lys)):
  plt.figure()
  plt.style.use('seaborn-ticks')
  plt.plot(inactive_lys[i],label='lys-aba')
  plt.plot(inactive_ser[i],label='ser-aba')
  plt.legend()
  plt.savefig(str(i)+'inactive.png')
  
for i in range(0,len(active_lys)):
  plt.figure()
  plt.style.use('seaborn-ticks')
  plt.plot(active_lys[i],label='lys-aba')
  plt.plot(active_ser[i],label='ser-aba')
  plt.legend()
  plt.savefig(str(i)+'active.png')
