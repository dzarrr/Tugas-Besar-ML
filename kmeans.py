import random

def get_euclidean_distance(p1, p2):
  squared_error = 0
  for atrib_p1, atrib_p2 in zip(p1, p2) :
    squared_error += (atrib_p1 - atrib_p2) ** 2

  return (squared_error ** (1/2))

def initialize_center_cluster(dataset):
  return random.randint(0, len(dataset) - 1)

def average_cluster(dataset):
  sum_of_data = []

  for i in range(0, len(dataset[0])):
    sum_of_data.append(0)

  for element in dataset :
    for i in range(0, len(element)) :
      sum_of_data [i] += element[i]

  for i in range(0, len(sum_of_data)) :
    sum_of_data[i] /= len(dataset)

  return sum_of_data


def get_label(dataset, cluster_center):
  label = []
  for data in dataset :
    max_dist = -1
    for i in range(0, len(cluster_center)) :
      dist = get_euclidean_distance(data, cluster_center[i])
      if (max_dist == -1) or (dist < max_dist) :
        max_dist = dist
        current_cluster = i
    label.append(current_cluster)

  return label

def update_center(cluster_center, dataset_, label_) :
  updated_center = []

  for i in range(0, len(cluster_center)) :
    current_cluster = []
    for dataset, label in zip(dataset_, label_) :
      if label == i :
        current_cluster.append(dataset)
    updated_center.append(average_cluster(current_cluster))

  return updated_center

        



def kmeans(k, dataset) : 
  cluster_changed = True
  cluster_center = []
  clusters_copy = []
  label = []

  for element in dataset :
    clusters_copy.append(element)

  for i in range (0, k) :
    index_center_cluster = initialize_center_cluster(clusters_copy)
    cluster_center.append(clusters_copy[index_center_cluster])
    del(clusters_copy[index_center_cluster])

  cluster_center = []
  cluster_center = [(1.0, 1.0), (5.0, 7.0)]

  prev_label = []
  while (cluster_changed) :
    label = get_label(dataset, cluster_center)
    cluster_center = update_center(cluster_center, dataset, label)

    if label == prev_label :
      cluster_changed = False
    prev_label = label

  return label

