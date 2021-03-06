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
  




#-----------------------------------------------------------------------------
def cluster_counts(n,cl_labels):
  """
  Function: Counting the frames in each cluster
  Parameters:
    n: number of cluster centers
    cl_labels: labels obtained from the clustering. It should be a list of arrays

  Returns:
    counts: list of counts corresponding to each cluster
  """
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]              #Intialization of a 2d list; length == number of clusters
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in cl_labels];   #List maps the clusters to their trajectory numbers.  
  counts=[len(frame_number[i]) for i in range(n)]
  return counts


#-----------------------------------------------------------------------------
def parameter_clustering(n,cl_labels,metric):
  """Extracts index of trajectory and frame based on cluster labels
  Parameters:
    n: number of clusters
    cl_labels: labels obtained from the clustering. It should be a list of arrays

  Returns:
    index_tuple: Gives list of tuples of length==n; 
                 first and second element of tuple correspond to trajectory and frame number respectively.
  """
  from random import randint
  import numpy as np
  traj_number=[[i for i in range(0,0)] for j in range(0,n)]               #2d list initialization: mapping traj numbers
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]              #2d list initialization: mapping frame numbers
  [[traj_number[i].append(j[0]) for i in j[1]] for j in enumerate(cl_labels)];    
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in cl_labels];
  
  metric_cluster=[]
  
  for i in range(0,len(frame_number)):
    temp=[]
    for j in range(0,len(frame_number[i])):
      temp.append(metric[traj_number[i][j]][frame_number[i][j]])
    metric_cluster.append(np.array(temp))
  
  return metric_cluster






#-----------------------------------------------------------------------------
def extract_index(n,cl_labels):
  """Extracts index of trajectory and frame based on cluster labels
  Parameters:
    n: number of clusters
    cl_labels: labels obtained from the clustering. It should be a list of arrays

  Returns:
    index_tuple: Gives list of tuples of length==n; 
                 first and second element of tuple correspond to trajectory and frame number respectively.
  """
  from random import randint
  traj_number=[[i for i in range(0,0)] for j in range(0,n)]               #2d list initialization: mapping traj numbers
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]              #2d list initialization: mapping frame numbers
  [[traj_number[i].append(j[0]) for i in j[1]] for j in enumerate(cl_labels)];    
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in cl_labels];
  
  
  traj_extract=[]                     #List containing traj number 
  frame_extract=[]                    #List containing frame number
  for i in enumerate(traj_number):
    L=len(i[1])-1
    index=randint(0,L)
    traj_extract.append(traj_number[i[0]][index])
    frame_extract.append(frame_number[i[0]][index])
  
  index_tuple=zip(traj_extract,frame_extract)
  
  return index_tuple
  


#-----------------------------------------------------------------------------
def pdb_extract(index_tuple,traj_list, top_path):
  """Extracts frames from trajectories and saves them in pdb format
  Parameters:
    index_tuple: Gives list of tuples of length==n; 
                 first and second element of tuple correspond to trajectory and frame number respectively.
    traj_list: List of string; each string is address of each trajectory file
    top_path: String; path of topology file

  Returns:
    Creates pdb files
  """
  import pytraj as pt
  L=len(index_tuple)
  for i in range(0,L):
    traj=traj_list[index_tuple[i][0]]
    frame=index_tuple[i][1]
    traj=pt.iterload(traj,top_path,frame_slice=(frame, frame+1))
    pt.write_traj(str(i)+'.pdb', traj, overwrite=True)
  
  
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
def reshape_seq(s,shape_pkl):     #Function for transforming single array cluster labels to 'list of array' type
  traj_frames=io.load(shape_pkl)
  sequences=[]
  p=q=0
  for i in traj_frames:
    q=p+i
    sequences.append(s[p:q])
    p=p+i
  return sequences
