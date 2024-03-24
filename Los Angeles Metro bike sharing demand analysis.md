## Introduction
This project combines Python, R, and ArcGIS Pro to conduct a bike sharing demand analysis. Using Python to deal with data and arcpy to do spatial analysis then constructing built environment-related variables for a further bike demand analysis which conducted in R. This project utilizes Python to create a user-friendly interface for users to access the information about weekly, monthly (both on weekday and weekend) shared-bike ridership by two steps: import bike sharing data (which is public accessible on LA Metro GIS data website), then enter the numeric number corresponding to that month. The dependent variable is the number of bike trips made to each bike station, the independent variables including zoning, number of restaurants, number of jobs, number of bus stops, and station capacity.

## Bike-sharing demand
Bike-sharing demand in urban environment is influenced by multiple factors including, land use and built environment, workday and weekend, supported cycling infrastructure, access to public transportation, socio-economic factor and weather condition. An intuitive way to understand bike-sharing demand is by referring to the number of bike trip, which is the dependent variable in this research. The factors mentioned above have various impact on bike-sharing either in the direction of encouraging or discouraging the usage of shared bikes. The way in which one can identify bike trip purpose is through bike-sharing origin-destination (OD) pairs. Land use and built environment and access to public transportation can have positive influence on cycling behavior, for example, businesses district might attract more bike work trips, district with recreational might attract more leisure bike trips. Nonetheless, identifying the bike OD pairs through different days and time of week on top of land use factor would provide us a better understanding in cycling behavior. Which is to say, it is intuitive to make the assumptions that recreational hubs where parks, shopping malls located might attract more leisure bike trips on the weekend as opposed to weekdays in the case of business district. Supported cycling infrastructure such as bike racks or different types of bike lanes (conventional/buffered/contra-flow/left-sided) has positive impact on cycling behavior as they are in service of providing a better biking experience and increase bike safety for cyclists. As for socio-economic factor, it could be referred to long-term and short-term subscriber in this case. Weather condition might be the dichotomous constraint for analyzing bike-sharing demand as its presence may exclude the demand in shared bikes.

## Data source

| **Dataset** | **Data source** |
|---|---|
| 2020 Census Block | < 20    |
| Metro Bike Share Station | LA Metro GIS data |
| Jobs per census block | LEHD Origin-Destination Employment Statistics (LODES) |
| Zoning | Los Angeles GeoHub |
| Restaurant & Bus stop | OpenStreetMaps |


## Result
### _Bike station buffer_
In order to conduct the station-level analysis, the buffer with bike station is set to 300 meters as it is the appropriate buffer reported by a couple bike sharing demand analysis
modeling papers. Considering bike share stations are concentrated in downtown Los Angeles, many of bike stations buffers overlap with each other, Thiessen polygon method is integrated into creating bike station buffer for each bike station (Figure 1) with a closer look at Thiessen polygon buffer (Figure 2). As a result, each observed characteristic (which will be addressed in the following section) is assigned to the nearest bike station given that the first law of geography is that “everything is related to everything else, but near things are more related than distant things.”

### _Commercial point of interest_
It should be noted that the cluster in West Hollywood area seems to have higher number of restaurants around bike station compared with other clusters. A possible explanation is that there are various touristy spots such as Dolby Theatre, Hollywood Walk of Fame, The Hollywood museum and other popular tourist destinations on Hollywood Boulevard.

### _Jobs_
As for the number of job counts, the workplace job counts data LEHD Origin-Destination Employment Statistics (LODES) is accessed from Census Bureau at census block level. The number of jobs within 300m buffer of bike station were assigned to each bike station for further analysis. In order to do so, centroid of each census block was calculated, each centroid comes with the number of jobs in the census block. Next, centroids were assigned to the nearest bike station. As shown in Figure 3, the number of jobs is higher for the cluster on the right-hand side, which is downtown Los Angeles. This is reasonable given that city center is usually the employment center. However, there is a noticeable buffer with higher number of jobs alone on the west of Beverly Hills, the reason for the higher number of job counts might be it located at Westwood Village. Westwood Village is a lively place bordering the UCLA campus with chain boutiques, movie theatres, restaurants and casual eateries.

### _Bike trips_
As it shown in Figure 4, bike stations in downtown Los Angeles has the higher number of bike trips. However, a couple stations along the coast have noticeable higher inbound bike trips. By comparing figure 3 with figure 4 with initial observation, we can suspect that the number of bike trips might have relationship with the number of jobs at this stage.

### _Bike trips by weekdays and weekends_
Weekday bike trips share had gone from multimodal distribution to unimodal distribution from 2016 to 2023. The following series of graphs provide the comparison for the bike trip distribution in the quarter 3 of the year from 2016 to 2023. The first graph in the series is being enlarged for legibility.

|Suitable habitat in East Georgia|Suitable habitat in Southeast Georgia|
|:-:|:-:|
|![First Image](https://github.com/rc-tsai/gis-portfolio/blob/main/images/LA%20Metro/2016-q3.png)|![Second Image](images/LA-Metro/2017-q3.png)|


As the series of graphs show that the clear cut of the transformation from multimodal to unimodal distribution occurred during 2019 and 2020. However, the weekday bike trips share distribution are consistent during the period between 2016 and 2019, and the period between 2020 and 2023, respectively, even number of bike trips changed intensely during within two periods. This suggests that bike users from the same or different population might have same demand for shared-bike across the time of day.



Besides, there are some possible explanations for the transformation. The first explanation is that the COVID-19 pandemic has dramatically changed bike users’ travel behavior as in home-based telecommuting has been widely adopted since the outset of the pandemic, suggesting that the pandemic caused a shift in bike sharing demand equally on the bike user population. The second explanation for the transformation from multimodal to unimodal distribution might reflect the fact that dataset sampled from different observed groups. In order to test the idea, datasets of 2019 and 2022 are being compared. First, they are two groups before and after the pandemic, respectively. Second, the difference of bike trips between them are quite close, the number of bike trips are 92,124 and 85,171 for 2019 and 2022, respectively. The reason for not picking the 2016 and 2021 pair is that 2021 is the year just after the pandemic, the bike trips just started to bounce back, as a result, it might not be representative at large. The comparison of the pair 2019-2022 is provided as follows. In 2019, the demand started to increase sharply at 5am and first peaked at the 8-9am time window. The bike demand peaked at morning rush hours, suggesting that bike trips might made by workers, together with the second peak at 5pm, corresponding to morning and afternoon rush hours. As for 2022, bike demand was still started to increase at 5am but grows relatively smoothly, meaning that bike demand has shifted towards later part of the day, which can be identified visually readily.
