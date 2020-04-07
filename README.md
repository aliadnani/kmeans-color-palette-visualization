# K-Means Color Palette Visualization
### Color palette generation using K-means clustering; further 3D RGB space visualization. 

![](colorpalette_rot2.png)

## How it works

1. Reads image into numpy array using OpenCV2
2. Resizes image to 420px short edge to make computation faster
3. Reshapes array to get one dimensional series of pixel RGB values
4. Fits K-Means clustering model to pixel series
5. Visualisation with plot.ly

## Examples:

#### Image to generate color palette for

![](DSC_4439.jpg)

#### Visualization of image's pixels in 3D RGB space

![](overall_pixel_plot.PNG)

#### Generated colors from K-Means model

![](colorpalette_rot2.png)

#### Visualization of generated colors in 3D RGB space
![](kmeans.PNG)

