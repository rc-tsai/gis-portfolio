## Contents
- ModelBuilder Example I: [Euclidean and Network distance Thiessen Buffer](#Euclidean-and-Network-distance-Thiessen-Buffer)
- ModelBuilder Example II: [Travel Time Exponential decay coefficient](#Travel-Time-Exponential-decay-coefficient)

<br><br>

## Euclidean and Network distance Thiessen Buffer
In the majority of analyses concerning bike share demand, researchers employ a Euclidean buffer to examine the attractions surrounding bike stations. However, this method may lead to biased results, despite the apparent similarity in coverage produced by both Euclidean and network distances. The advantage of creating buffers by integrating Thiessen polygons is that every attraction within the buffer is located closer to the corresponding bike station. The following images illustrate the differences between Thiessen buffers using Euclidean and network distances.
<br><br>

| Euclidean distance | Network distance |
|:-:|:-:|
|![First Image](../images/ArcGIS%20Pro%20ModelBuilder/EuclideanBuffer_300m.png)|![Second Image](../images/ArcGIS%20Pro%20ModelBuilder/NetworkBuffer_300m.png)|

<br><br>

Below is a demonstration of creating a Network Distance Thiessen Buffer using 300-meter buffer as an example

https://github.com/rc-tsai/gis-portfolio/assets/139235338/81fc279a-0cfa-41cf-81b0-c083649acfcb

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

## Gravity-based job accessibility index

<br>
<p align="center">
  $A_{i} = \displaystyle\sum_{j} [\frac{E_{j} \cdot f(d_{ij})}{\displaystyle\sum_{k} P_{k} \cdot f(d_{jk})}]$
</p>
<br>

$`A_{i}`$ = job accessibility in census tract 𝑖 (measured census tract)

$`E_{j}`$ = number of jobs in census tract 𝑗

$`P_{k}`$ = number of jobseekers (job competitors) in census tract 𝑘

$`f(d_{ij} = e^{-\beta(k) \cdot t}`$ (time decay funtion, $`b`$ = non-negative time decay coefficient, $`t`$ = travel time in minute, $`k`$ = area type)

_Note. Area type is categorized as Metropolitan area, Small town, or Rural area based on [USDA Rural-Urban Commuting Area Codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/)_

#### _Pre-processing data_
First, I aggregate total number of low-paying jobs and workers (less than $1,250/month) at census tract, respectively. The trick is that [LEHD LODES]([https://lehd.ces.census.gov/](https://lehd.ces.census.gov/data/)) is linked employer-household data. Aggregating low-paying Origin-Destination (OD) trips at Residence Census Block Code is equivalent to obtaining the number of low-paying workers at census block. The same applies to aggregating low-paying OD trips at Work Census Block Code, which is tantamount to obtaining the number of jobs at census block. However, I aggregate them at census tract for calculating job accessibility index (steps can be found [here](../miscellaneous/low_paying_worker_job.ipynb)), as it is the most commonly used geographic unit found in existing literature.

Secondly, I export them as csv files then bring them into ArcGIS Pro. I use export table tool on them before joining them into census tract. I generate census tract centroid, then add two fields 'low_job' and 'low_worker' both as DOUBLE data type. Then calculate 'low_job' after the first join, then remove join. Do it the same for 'low_worker.'

<br>

#### _Classify rural-urban census tract_
I classify census tracts into three categories: Metropolitan, Small town, and Rural based on the classification provided by [USDA Rural-Urban Commuting Area Codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/). However, 2020 classification would be released no earlier than Fall 2024, so I use the classification of 2010 on census tracts 2020 with some modification as follows:
- I add 2010 census tract from ArcGIS Online then use copy feature tool (cannot edit the layer import from ArcGIS Online).
- Filter out records regarding Georgia then export to csv file. Then export to table in ArcGIS Pro.
- Join the table to 2010 census tract (I add a census tract text field in the export table unlike GEOID_NUM as DOUBLE data type when join low-paying workers and jobs)
- Add a text field 'Area_Type' and use the following classification to calculate 'Area_Type'
```python
Area_Type = area_type(!RUCA!)

def area_type(x):
    if 1 <= x <= 6:
        return "Metropolitan"
    elif 7 <= x <= 9:
        return "Small town"
    else:
        return "Rural"
```
- Use feature to point to generate 2020 census tract centroid
- Perform spatial join using 2020 census tract centroid as target feature and 2010 census tract polygon as join feature
- Now we classify 2020 census tract into three categories

<br>

#### _Assign time decay coefficient to the corresponding census tract_
We estimate travel time decay coefficient [here](../miscellaneous/Time-decay-coefficient-for-gravity-based-job-accessibility-index.ipynb). The time decay coefficients can be thought as penalizing the desirability of jobs that are further away than the closer jobs, meaning that the desirability of job and distance from job seeker's residential location is inverse relationship. To assign the corresponding coefficient:
- I add a text field 'TimeDecay_Beta' in the result of spatial join done in previous step
- Calculate the field by using:
```python
TimeDecay_Beta = beta(!Area_Type!)

def beta(x):
    if x == 'Metropolitan':
        return 0.0278
    elif x == 'Small town':
        return 0.0292
    else:
        return 0.0259
```
<br>

To derive the job accessibility index, I first normalize the total low-paying jobs at census tract by the total number of low-paying workers that can reach those jobs in that census tract. By doing so, the index accounts for job competition among job seekers. I calculate the job access index in two steps:

1. Normalize jobs at census tract
2. Calculate reachable normalized jobs from each census tract

<br>

This is the job access equation:
<p align="center">
  $A_{i} = \displaystyle\sum_{j} [\frac{E_{j} \cdot f(d_{ij})}{\displaystyle\sum_{k} P_{k} \cdot f(d_{jk})}]$
</p>


This is normalized jobs at ceneus tract:
<p align="center" style="font-size: larger;">
  $$\frac{E_{j}}{\displaystyle\sum_{k} P_{k} \cdot f(d_{jk})}$$
</p>
<br>

### _Normalize jobs at census tract_
First, add a text field 'CTID_lowjob' to concatenate census tract GEOID and 'low_job'
```python
CTID_lowjob = !GEOID! + "-" +str(int(!low_job!))
```
<br>
Secondly, add another text field 'Worker_Beta' to ocncatenate total worker in each census tract and time decay coefficient
```python
Worker_Beta = str(int(!low_worker!)) + "-" +str(!TimeDecay_Beta!)
```
