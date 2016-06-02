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
  """Merging two independent clusters made by MSMBuilder
    
  Args:
    cl1: cluster object obtained from MSMBuilder
    cl2:cluster object obtained from MSMBuilder
    
  Attributes:
    n_states (int): number of states in merged cluster assignment
    labels_ (list of arrays): cluster labels in new cluster assignment; each array corresponds to each trajectory
    cluster_center1 (array): first new cluster centers
    cluster_center2 (array): Second new cluster centers
  """


  def __init__(self,cl1,cl2):
    self.cl1=cl1
    self.cl2=cl2


  def merger_function(self):
    l1_input=self.cl1.labels_
    l2_input=self.cl2.labels_
    centers1=self.cl1.cluster_centers_
    centers2=self.cl2.cluster_centers_
    n=self.cl1.n_clusters
    size=[len(a) for a in l1_input]
    
    if isinstance(l1, list) is list:  #Checks if the labels are list of arrays.
      l1=np.array([item for sublist in l1_input for item in sublist])
    else
      l1=l1_input
    if isinstance(l2, list) is list:
      l2=np.array([item for sublist in l2_input for item in sublist])
    else
      l2=l2_input
    
    new_cl=np.zeros(len(l1))
    new_centers1=[]
    new_centers2=[]
    
    s=0
    for i in range(0,n):
      index=np.where(l1==i)   #traj index of frames belonging to same cluster on rmsd
      temp_l2=l2[index]           #Distance based cluster indices for the cluster
      for j in set(temp_l2):
        traj_index=index[0][np.where(temp_l2==j)]  #Traj index of frames with same rmsd and dist 
        new_cl[traj_index]=s                       #Assigning new cl labels
        new_centers1.append(centers1[i])
        new_centers2.append(centers2[j])
        s=s+1
    
    n_clusters=np.array(new_cl).max() +1
    n_clusters=int(n_clusters)
    new_centers1=new_centers1[0:n_clusters]
    new_centers2=new_centers2[0:n_clusters]
    
    final_labels=[]
    p=q=0
    for i in size:
      q=p+i
      final_labels.append(new_cl[p:q])
      p=p+i

    return final_labels, n_clusters, new_centers1, new_centers2 
  
  
  @property
  def labels_(self):
    l,n_clusters,c1,c2=self.merger_function()
    return l
  
  
  @property
  def n_clusters(self):
    l,n,c1,c2=self.merger_function()
    return n

  @property
  def cluster_center1(self):
    l,n,c1,c2=self.merger_function()
    return c1

  @property
  def cluster_center2(self):
    l,n,c1,c2=self.merger_function()
    return c2
