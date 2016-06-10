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
def free_energy_data(data1,data2,cl,msm):
  """Plotting weighted free energy landscape.
  
  Args:
    data1(list of arrays): First metric for landscape
    data2 (list of arrays): Second metric for landscape
    eqm_probability (array): array corresponding to equilibrium probability of each state
  """
  from random import randint
  import numpy as np
  n=cl.n_clusters
  cl_labels=cl.labels_
  
  traj_number=[[i for i in range(0,0)] for j in range(0,n)]               #2d list initialization: mapping traj numbers
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]              #2d list initialization: mapping frame numbers
  [[traj_number[i].append(j[0]) for i in j[1]] for j in enumerate(cl_labels)];    
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in cl_labels];
  
  counts=np.array([len(frame_number[i]) for i in range(n)])    #Count numbers for each cluster
  
  data1_clustered=[[i for i in range(0,0)] for j in range(0,n)]
  data2_clustered=[[i for i in range(0,0)] for j in range(0,n)]
  
  for i in range(0,len(frame_number)):
    for j in range(0,len(frame_number[i])):
      data1_clustered[i].append(data1[traj_number[i][j]][frame_number[i][j]])
      data2_clustered[i].append(data2[traj_number[i][j]][frame_number[i][j]])
  
  map_=msm.mapping_
  inv_map_={v: k for k, v in map_.items()}
  
  dat1_final=[]
  dat2_final=[]
  dat1_array=[]
  dat2_array=[]
  counts_final=[]
  for key in inv_map_:
    dat1_array.append(np.array(data1_clustered[inv_map_[key]]))
    dat2_array.append(np.array(data1_clustered[inv_map_[key]]))
    dat1_final=dat1_final+data1_clustered[inv_map_[key]]
    dat2_final=dat2_final+data2_clustered[inv_map_[key]]
    counts_final.append(counts[inv_map_[key]])

  
  np.savetxt('dat1.dat',dat1_final,newline='\n')
  np.savetxt('dat2.dat',dat2_final,newline='\n')
  np.savetxt('count_mat.dat',counts_final,newline='\n')
  np.savetxt('msm_eq_pop.dat',msm.populations_,newline='\n')
  
  return np.array(counts_final), dat1_array, dat2_array
  
  
  
