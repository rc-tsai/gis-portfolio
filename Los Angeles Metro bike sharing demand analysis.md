## Table of Content
- [Introduction](#Introduction)<br>
- [Bike sharing demand](#Bike-sharing-demand)<br>
- [Data source](#Data-source)<br>
- [Result](#Result)<br>
- [ArcGIS ModelBuilder workflow (construct Thiessen-Polygon from network distance)](#ArcGIS ModelBuilder workflow (construct Thiessen-Polygon from network distance))
<br><br><br>


## Introduction
This project combines Python, R, and ArcGIS Pro to conduct a bike sharing demand analysis. Using Python to deal with data and arcpy to do spatial analysis then constructing built environment-related variables for a further bike demand analysis which conducted in R. This project utilizes Python to create a user-friendly interface for users to access the information about weekly, monthly (both on weekday and weekend) shared-bike ridership by two steps: import bike sharing data (which is public accessible on LA Metro GIS data website), then enter the numeric number corresponding to that month. The dependent variable is the number of bike trips made to each bike station, the independent variables including zoning, number of restaurants, number of jobs, number of bus stops, and station capacity.

<br>

## Bike sharing demand
Bike sharing demand in urban environment is influenced by multiple factors including, land use and built environment, workday and weekend, supported cycling infrastructure, access to public transportation, socio-economic factor and weather condition. An intuitive way to understand bike-sharing demand is by referring to the number of bike trip, which is the dependent variable in this research. The factors mentioned above have various impact on bike-sharing either in the direction of encouraging or discouraging the usage of shared bikes. The way in which one can identify bike trip purpose is through bike-sharing origin-destination (OD) pairs. Land use and built environment and access to public transportation can have positive influence on cycling behavior, for example, businesses district might attract more bike work trips, district with recreational might attract more leisure bike trips. Nonetheless, identifying the bike OD pairs through different days and time of week on top of land use factor would provide us a better understanding in cycling behavior. Which is to say, it is intuitive to make the assumptions that recreational hubs where parks, shopping malls located might attract more leisure bike trips on the weekend as opposed to weekdays in the case of business district. Supported cycling infrastructure such as bike racks or different types of bike lanes (conventional/buffered/contra-flow/left-sided) has positive impact on cycling behavior as they are in service of providing a better biking experience and increase bike safety for cyclists. As for socio-economic factor, it could be referred to long-term and short-term subscriber in this case. Weather condition might be the dichotomous constraint for analyzing bike-sharing demand as its presence may exclude the demand in shared bikes.

<br>

## Data source

| **Dataset** | **Data source** |
|---|---|
| 2020 Census Block | Census Bureau |
| Metro Bike Share Station | LA Metro GIS data |
| Jobs per census block | LEHD Origin-Destination Employment Statistics (LODES) |
| Zoning | Los Angeles GeoHub |
| Restaurant & Bus stop | OpenStreetMaps |

<br>

## Result
#### _Bike station buffer_
In order to conduct the station-level analysis, the buffer with bike station is set to 300 meters as it is the appropriate buffer reported by a couple bike sharing demand analysis modeling papers.I construct Thiessen-Polygon buffer for each bike share station with road network distance (see ArcGIS ModelBuilder for detailed workflow). As a result, each observed characteristic (which will be addressed in the following section) is assigned to the nearest bike station given that the first law of geography is that “everything is related to everything else, but near things are more related than distant things.”

<p align="center">Bike station Thiessen-Polygon Buffer</p>
<p align="center">
  <img width="60%" height="60%" src="images/LA Metro/ZoomIn.png">
</p>

<br><br>

|Bike stations in West LA | Bike stations in Downtown LA|
|:-:|:-:|
|<img src="images/LA Metro/WestLA.png" width="130%">|<img src="images/LA Metro/DTLA.png" width="130%" >

<br><br>
#### _Bus stops_
It should be noted that the cluster in West Hollywood area seems to have higher number of restaurants around bike station compared with other clusters. A possible explanation is that there are various touristy spots such as Dolby Theatre, Hollywood Walk of Fame, The Hollywood museum and other popular tourist destinations on Hollywood Boulevard.

<p align="center"> Bus stops within 300m of bike stations</p>
<p align="center">
  <img width="75%" height="75%" src="images/LA Metro/Bus stop.png">
</p>
<br><br>

#### _Restaurants_
It should be noted that the cluster in West Hollywood area seems to have higher number of restaurants around bike station compared with other clusters. A possible explanation is that there are various touristy spots such as Dolby Theatre, Hollywood Walk of Fame, The Hollywood museum and other popular tourist destinations on Hollywood Boulevard.
<p align="center"> Restaurants within 300m of bike stations</p>
<p align="center">
  <img width="75%" height="75%" src="images/LA Metro/Restaurant.png">
</p>
<br><br>

#### _Jobs_
As for the number of job counts, the workplace job counts data LEHD Origin-Destination Employment Statistics (LODES) is accessed from Census Bureau at census block level. The number of jobs within 300m buffer of bike station were assigned to each bike station for further analysis. In order to do so, centroid of each census block was calculated, each centroid comes with the number of jobs in the census block. Next, centroids were assigned to the nearest bike station. As shown in Figure 3, the number of jobs is higher for the cluster on the right-hand side, which is downtown Los Angeles. This is reasonable given that city center is usually the employment center. However, there is a noticeable buffer with higher number of jobs alone on the west of Beverly Hills, the reason for the higher number of job counts might be it located at Westwood Village. Westwood Village is a lively place bordering the UCLA campus with chain boutiques, movie theatres, restaurants and casual eateries.

<p align="center"> Jobs within 300m of bike stations</p>
<p align="center">
  <img width="75%" height="75%" src="images/LA Metro/Job.png">
</p>
<br><br>

#### _Bike trips_
As it shown in Figure 4, bike stations in downtown Los Angeles has the higher number of bike trips. However, a couple stations along the coast have noticeable higher inbound bike trips. By comparing figure 3 with figure 4 with initial observation, we can suspect that the number of bike trips might have relationship with the number of jobs at this stage.
<br><br>
#### _Bike trips by weekdays and weekends_
Weekday bike trips share had gone from multimodal distribution to unimodal distribution from 2016 to 2023. The following series of graphs provide the comparison for the bike trip distribution in the Quarter 3 (July to September) of the year from 2016 to 2023. The first graph in the series is being enlarged for legibility.

<br>

|2016|2017|
|:-:|:-:|
|<img src="images/LA Metro/2016-q3.png" width="90%">)|<img src="images/LA Metro/2017-q3.png" width="90%">|

|2018|2019|
|:-:|:-:|
|<img src="images/LA Metro/2018-q3.png" width="90%">)|<img src="images/LA Metro/2019-q3.png" width="90%">|

|2020|2021|
|:-:|:-:|
|<img src="images/LA Metro/2020-q3.png" width="90%">)|<img src="images/LA Metro/2021-q3.png" width="90%">|

<br>
As the series of graphs show that the clear cut of the transformation from multimodal to unimodal distribution occurred during 2019 and 2020. However, the weekday bike trips share distribution are consistent during the period between 2016 and 2019, and the period between 2020 and 2023, respectively, even number of bike trips changed intensely during within two periods. This suggests that bike users from the same or different population might have same demand for shared-bike across the time of day.
<br><br>
<p align="center">Metro bike trips demand (January - March) by years</p>
<p align="center">
  <img width="60%" height="60%" src="images/LA Metro/Metro bike trips demand (January - March) by years.png" width="80%">
</p>

<br>

Besides, there are some possible explanations for the transformation. The first explanation is that the COVID-19 pandemic has dramatically changed bike users’ travel behavior as in home-based telecommuting has been widely adopted since the outset of the pandemic, suggesting that the pandemic caused a shift in bike sharing demand equally on the bike user population. The second explanation for the transformation from multimodal to unimodal distribution might reflect the fact that dataset sampled from different observed groups. In order to test the idea, datasets of 2019 and 2022 are being compared. First, they are two groups before and after the pandemic, respectively. Second, the difference of bike trips between them are quite close, the number of bike trips are 92,124 and 85,171 for 2019 and 2022, respectively. The reason for not picking the 2016 and 2021 pair is that 2021 is the year just after the pandemic, the bike trips just started to bounce back, as a result, it might not be representative at large. The comparison of the pair 2019-2022 is provided as follows. In 2019, the demand started to increase sharply at 5am and first peaked at the 8-9am time window. The bike demand peaked at morning rush hours, suggesting that bike trips might made by workers, together with the second peak at 5pm, corresponding to morning and afternoon rush hours. As for 2022, bike demand was still started to increase at 5am but grows relatively smoothly, meaning that bike demand has shifted towards later part of the day, which can be identified visually readily.
<br>
<p align="center">Comparison of Bike Trip Demand Between 2019 and 2022</p>
<p align="center">
  <img width="60%" height="60%" src="images/LA Metro/Weekday bike trips share (January - March).png" width="80%">
</p>


#### _Regression analysis_
I first use ANOVA to test whether zoning type has an effect on the number of ridership through the R command:
<br>
`summary(aov(in_flow ~ ZONE_SMRY, data = df))`<br>
`zoneeffect_ <- aov(in_flow ~ ZONE_SMRY, data = df)`<br>
`tukey.test <- TukeyHSD(zoneeffect_); tukey.test`<br>

The result shows that zoning type does have an effect on ridership, however, it doesn’t tell us which type of land use has a statistically significant effect on ridership, so I further conduct tukey test which puts any two given types of land use and see if they are statistically significant different from each other. The tukey test result shows that ‘Open Space’ type of land use has a statistically significant effect on ridership. As a result, it is reasonable to include ‘Open Space’ as one of the independent variables by constructing it as a dummy variable in the linear regression model.

<br>

|  | Degrees of freedom | Sum of Squares | Mean of Squares | F value | Pr(>F) |
|---|---|---|---|---|---|
| ZONE_SMRY | 6 | 3556639 | 592773 | 11.57 | 3.04e-11 *** |
| Residuals | 219 | 11219878 | 51232 |  |  |

<br>

The regression output for bike sharing demand analysis is as follows:

| Coefficients: |  |  |  |  |  |
|---|---|---|---|---|---|
|  | Estimate | Standardized Coeff. | Std. Error | t value | Pr(>\|t\|) |
| (Intercept) | -41.93067 | NA | 36.35960 | -1.153 | 0.250 |
| Job | 0.30164 | 0.07712 | 0.22195 | 1.359 | 0.176 |
| Bus_stop | -2.64629 | -0.08522 | 1.83100 | -1.445 | 0.150 |
| Restaurant | 2.54673 | 0.09241 | 1.62139 | 1.571 | 0.118 |
| Open_space | 1392.40932 | 0.52532 | 145.53089 | 9.568 | < 2e-16 *** |
| Bike_station_capacity | 11.57821 | 0.28505 | 2.26185 | 5.119 | 6.83e-07 *** |

<br>

Only two of the independent variables are statistically significant in the model, meaning that they are the variables that have a relationship with the dependent variable at 0.05 significance level. For open space variable, the positive sign of its estimated coefficient is positive as expected, given that the proximity to open space encourage people to take leisure bike trip on-site, including community parks or regional parks. This variable implies that if the closest land use of a given bike-shared station is open space, the number of bike trips would be expected to be 1392 more than its counterpart. In addition, there are only 12 out of 226 bike stations that its closest land use type is open space. This might imply that people may usually take leisure bike trip. For station capacity, the positive sign of its estimated coefficient is expected, given that bike users cannot make trips to a place if there are no bike racks. It is intuitive to think that if a bike station equipped with more bike racks, there would be more departure trips at that station. The station capacity variable indicates that an addition of one bike rack at a station, the number of departure trips would be expected to increase by 12. This suggests that a bike station would have ( 1392 + 12 – 41 ) more bike trips than a bike station that has one bike rack less and its closest land use is not open space.

<br>

As we can see from the output regarding standardized coefficient, open space variable has the largest effect on the ridership in terms of its magnitude, which followed by station capacity variable.

<br>

As for checking the highly influential observations (outliers) in the data, we can use cook’s distance to identify those data points. As the plot shown below, there are several observed data points that have a higher influential on the dependent variable compared to other data points. The number marked in red indicates the index of the data point, index of bike station in this case.

<p align="center">Cooks distance plot</p>
<p align="center">
  <img width="60%" height="60%" src="images/LA Metro/cooks.dist.png" width="80%">
</p>

<br><br>

Outlier bike stations

  
| Index |      Station Name                     | Bike trips |
|:-----:|:-------------------------------------:|:----------:|
|  140  |   Ocean Front Walk & Navy             |   2,085    |
|   78  |        Glendon & Kinross             |    176     |
|  141  |  Ocean Front Walk & North Venice     |   1,594    |
|   54  | Dockweiler Beach at Imperial Hwy     |    775     |



<br>
The table above shows the bike stations with indices corresponding to the data points in the Cook's distance plot.<br>

The Ocean Front Walk & Navy, Ocean Front Walk & North Venice and Dockweiler Beach at Imperial Hwy stations located around Venice Beach where is the touristy spot in Santa Monica, Los Angeles. By knowing their geographic locations, it is not surprised that they have an extreme high number of departure bike trips. We can conclude that it is highly possible that these are leisure bike trips by the beach.<br>

As for the Glendon & Kinross station, it is located in West Village (a commercial dense area), which is in close proximity to the campus of the University of California, Los Angeles. Land use type for the areas marked in purple is public facility, commercial for the areas marked in orange, residential for the one marked in yellow. Given that the information about bike trips are anonymized, we cannot further conclude that these bike trips were made by student population without further information though we can highly suspect that.<br>

Given that this project uses LA Metro Bike share 2023-q3 (July-September) data on analyzing bike share demand, the highly influential data points are expected to be the ones located or near tourist spots. The high number of tourist bike trips reflect the fact that people usually make more bike trips at those tourist spots, especially in tourist season. Given the limited time and ability of the author have, this project only analyzes the bike sharing demand in the context of tourist season, meaning that more variables related to recreational index could be included in the analysis.

## ArcGIS ModelBuilder workflow (construct Thiessen-Polygon from network distance) <br><br>
_Zoom in on the image to see the steps for constructing the Thiessen-Polygon buffer from network distance. The idea is conceptually fairly easy, so don't be intimidated by those boxes! Boxes in the upper part of the image represent the steps for building the network dataset._ <br><br>

<p align="center">ArcGIS ModelBuilder workflow</p>
<p align="center">
  <img width="100%" height="100%" src="images/LA Metro/Model.png">
</p>

<br>

### The basic idea is:
First, construct buffer from points <br>
Second, create Thiessen polygon from points <br>
Third, extract Thiessen polygon line by using _Polygon to Line_ tool <br>
Fourth, use _Intersect_ tool for the results from the first and third steps. <br>
Fifth, extract buffer boundary by usingi _Polygon to Line_ again on the buffer, remember to dissolve! <br>
Sixth, use _Feature to Polygon_ on the results from Fourth and Fifth steps. <br><br>
_Note that this is just my understanding of constructing Thiessen-Polygon buffer, I'd love to know how you build it!_
