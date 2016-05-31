################################################################
# Analysis post MSMBuilder                                     #   
# Author: Saurabh Shukla <sshukla4@illinois.edu>               #
# Orginially built for ShuklaGroup@illinois  <shuklagroup.org> #
################################################################

from msmbuilder.msm import MarkovStateModel
from msmbuilder.cluster import KMeans
import os
import numpy as np


def cluster_counts(n,cl_labels):
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in l];
  counts=[len(frame_number[i]) for i in range(n)]
  return counts

def rst_extraction(n,cl_labels,traj_list,top_address):
  traj_number=[[i for i in range(0,0)] for j in range(0,n)]
  frame_number=[[i for i in range(0,0)] for j in range(0,n)]
  [[traj_number[i].append(j[0]) for i in j[1]] for j in enumerate(l)];
  [[frame_number[i[1]].append(i[0]) for i in enumerate(j)] for j in l];
  
  
  
