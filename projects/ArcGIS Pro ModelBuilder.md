## Contents
- [Euclidean and Network distance Thiessen Buffer](#Euclidean-and-Network-distance-Thiessen-Buffer)
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
<div style="text-align: center;">
  <img src="../images/LA Metro/Model.png" alt="ArcGIS ModelBuilder Workflow" style="width: 100%; height: auto;">
</div>
<br>
  
- First, construct buffer from points <br>
- Second, create Thiessen polygon from points <br>
- Third, extract Thiessen polygon line by using Polygon to Line tool <br>
- Fourth, use Intersect tool for the results from the first and third steps <br>
- Fifth, extract buffer boundary by usingi Polygon to Line again on the buffer, then dissolve! <br>
- Sixth, use Feature to Polygon on the results from Fourth and Fifth steps. <br>

<br><br>

### Gravity-based job accessibility index

First, I aggregate total number of low-paying jobs and workers (less than $1,250/month) at census tract, respectively. The trick is that [LEHD LODES]([https://lehd.ces.census.gov/](https://lehd.ces.census.gov/data/)) is linked employer-household data. Aggregating low-paying Origin-Destination (OD) trips at Residence Census Block Code is equivalent to obtaining the number of low-paying workers at census block. The same applies to aggregating low-paying OD trips at Work Census Block Code, which is tantamount to obtaining the number of jobs at census block. However, I aggregate them at census tract for calculating job accessibility index (steps can be found [here](../miscellaneous/low_paying_worker_job.ipynb)), as it is the most commonly used geographic unit found in existing literature.

Secondly, I export them as csv files then bring them into ArcGIS Pro. I use export table tool on them before joining them into census tract.
