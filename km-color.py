import cv2
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import colorsys

def read_image(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  # Resize image to fit model faster
  resize_factor = (420 / min(img.shape[0],img.shape[1]))
  new_height = int(img.shape[0] * resize_factor)
  new_width = int(img.shape[1] * resize_factor)
  img = cv2.resize(img,(new_width, new_height))

  print(f'Old dimensions: {img.shape[1]} x {img.shape[0]}')
  print(f'New dimensions: {new_width} x {new_height}')

  # Convert to one dimensional pixel array
  pixel_list = img.reshape( ( img.shape[0] * img.shape[1]), 3 )
  return pixel_list

def get_dominant_colors(pixel_list, n_clusters=5):

  # Make kmeans model & fit
  kmeans = KMeans(n_clusters=n_clusters)
  kmeans.fit(pixel_list)

  # Return cluster
  dominant_colors = (kmeans.cluster_centers_)
  dominant_colors = dominant_colors.astype(int)

  return dominant_colors

# Function to plot pixels in 3D RGB space
def plot_all_pixels(pixel_list,size):
  trace=dict(type='scatter3d',
    x= pixel_list[:,0],
    y= pixel_list[:,1],
    z= pixel_list[:,2],
    mode='markers',
    marker=dict(color=[f'rgb({pixel_list[:,0][i]}, {pixel_list[:,1][i]}, {pixel_list[:,2][i]})' for i in range(len(pixel_list))],size=28,symbol='diamond'))
  
  data = [trace]
  fig = go.Figure(data=data)
  fig.show()


  # fig = go.Figure(data=go.scatter3d())

colors_series = read_image('DSC_4439.jpg')
plot_all_pixels(pixel_list=colors_series,size=2)
dom_colors = get_dominant_colors(colors_series)
plot_all_pixels(pixel_list=dom_colors,size=28)


