## Contents
- [Euclidean and Network distance Thiessen Buffer](#Thiessen-buffer)
- [Travel Time Exponential decay coefficient](#Travel-Time-Exponential-decay-coefficient)

<br><br>

### Euclidean and Network distance Thiessen Buffer
In the majority of analyses concerning bike share demand, researchers employ a Euclidean buffer to examine the attractions surrounding bike stations. However, this method may lead to biased results, despite the apparent similarity in coverage produced by both Euclidean and network distances. The advantage of creating buffers by integrating Thiessen polygons is that every attraction within the buffer is located closer to the corresponding bike station. The following images illustrate the differences between Thiessen buffers using Euclidean and network distances.
<br><br>

| Euclidean distance | Network distance |
|:-:|:-:|
|![First Image](../images/ArcGIS%20Pro%20ModelBuilder/EuclideanBuffer_300m.png)|![Second Image](../images/ArcGIS%20Pro%20ModelBuilder/NetworkBuffer_300m.png)|

<br><br>
The following workflow delineates the steps involved in creating a Network Distance Thiessen Buffer.
<div style="text-align: center;">
  <strong>ArcGIS ModelBuilder Workflow</strong>
  <br>
  <img src="../images/LA Metro/Model.png" alt="ArcGIS ModelBuilder Workflow" style="width: 100%; height: auto;">
</div>

<br><br>

### Travel Time Exponential decay coefficient

[dd](../miscellaneous/Time%20decay%20coefficient%20for%20gravity-based%20job%20accessibility%20index.ipynb)
