################################################################
# Analysis post MSMBuilder                                     #   
# Author: Saurabh Shukla <sshukla4@illinois.edu>               #
# Orginally built for ShuklaGroup@illinois  <shuklagroup.org>  #
################################################################


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import numpy as np





#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
class merge_cluster(object):
  """
  Merging two independent clusters made by MSMBuilder
    
  Parameters
  ----------
  cl1: 
    cluster object obtained from MSMBuilder
  cl2:
    cluster object obtained from MSMBuilder
    
  Attributes
  ----------
  n_states: int
    number of states in merged cluster assignment
  labels_: list of arrays
    cluster labels in new cluster assignment; each array corresponds to each trajectory
  cluster_center:
    new cluster centers
  """


  def __init__(self,cl1,cl2):
    self.cl1=cl1
    self.cl2=cl2


  def labels_(self):
    l1_input=self.cl1.labels_
    l2_input=self.cl2.labels_
    n=self.cl1.n_clusters
    size=[len(a) for a in l1_input]
    l1=np.array([item for sublist in l1_input for item in sublist])
    l2=np.array([item for sublist in l2_input for item in sublist])
    
    new_cl=np.zeros(len(l1))
    s=0
    for i in range(0,n):
      index=np.where(l1==i)   #traj index of frames belonging to same cluster on rmsd
      temp_l2=l2[index]           #Distance based cluster indices for the cluster
      for j in set(temp_l2):
        traj_index=index[0][np.where(temp_l2==j)]  #Traj index of frames with same rmsd and dist 
        new_cl[traj_index]=s                       #Assigning new cl labels
        s=s+1
    
    final_labels=[]
    p=q=0
    for i in size:
      q=p+i
      final_labels.append(new_cl[p:q])
      p=p+i
    
    return final_labels

