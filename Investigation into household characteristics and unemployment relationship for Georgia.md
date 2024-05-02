## Table of Content
- [Background](#Background)<br>
- [Variables selection](#Variable-selection)<br>
- [Methods](#Methods)<br>
- [Data assembly](#Result)<br>
- [Data](#ArcGIS-ModelBuilder_constructing-Thiessen-Polygon-buffer)
- [Result]()
<br><br><br>

## Background
Considerable research has been conducted into various types of unemployment, with three major categories being structural, frictional, and cyclical unemployment. The Reserve Bank of Australia has provided clear explanations of these types.

The first type, involuntary unemployment, arises from a mismatch between a worker's qualifications or skills and the requirements of available jobs, or when available jobs are geographically distant from job seekers. The second type, voluntary unemployment, occurs when workers voluntarily leave their current job to search for another, creating a transitional gap. The third type of unemployment occurs due to changes in economic activity during the business cycle, where the demand for workers by businesses is lower than the number of available job seekers.

A body of literature has examined unemployment at both macro and micro levels, exploring the relationship between economic factors, socioeconomic characteristics, and their direct or indirect impacts on unemployment.

## Variable selection

_Social benefits (Public Assistance Income)_ <br>
Alcan et al. (2016) maintain that receiving social benefits lead to protracted unemployment duration and a slower transition from unemployed to employed status (p. 2). Røed and Zhang (2003) find that a marginal increase in unemployment benefits reduces the escape rate from unemployment significantly, regardless business cycle conditions and unemployment duration (p. 204). Kupets (2006) find that recipients of unemployment benefits tend to have longer unemployment duration if they have income from casual work such farming (p. 244). I use the census variable on public assistance income which includes cash and non-cash benefits to low-income individuals or families.

_Household with a mortgage_ <br>
Baert et al. (2014) investigate into the relationship between unemployment duration and mortgage payment, concluding that outright owners stay unemployed longer than homeowners who has a mortgage (p. 280). Given that homeowners have a mortgage to pay, which press them to get a job faster than outright homeowners, which may lead to lower unemployment rate.

_Lower-paying jobs to worker ratio_ <br>
Mahmood et al. (2014) conduct a stepwise regression model to examine the factors that have an impact on unemployment. In their final best fit model, they point out that labor force has a positively effect on unemployment rate, while foreign direct investment (FDI) and inflation has a negative effect on the unemployment (p. 1173). Although stepwise regression has been considered a relatively coarse method, it serves well in exploratory analysis.

_Lower-paying jobs to worker dissimilarity_ <br>
Ihlanfeldt (1994) illustrates that racial discrimination constrains the residential locations of blacks, results in a smaller job opportunity set. Consequently, leading to higher black unemployment given that there is less chance for a successful match to occur between workers and jobs (p. 221). This concept has been referred by researchers as one of the spatial mismatch hypotheses. To measure spatial mismatch, dissimilarity index has been widely used by researchers. Stoll and Covington (2012) construct dissimilarity index to measure spatial imbalance between workers’ job and residential locations at the ZIP code for 267 metropolitan areas. Their methods result in a single value for a metropolitan area is convenient for interpretation.

It's important to note the distinction between the measurements of Lower-paying jobs to worker ratio and Lower-paying jobs to worker dissimilarity, despite their apparent similarity in involving the number of lower-paying jobs and workers. These metrics differ in nature. In my regression model, the first measurement serves as an indicator of the ease of accessing nearby jobs in a given census tract, operating under the assumption that low-income workers typically secure employment nearby due to limited access to information about available lower-paying jobs. On the other hand, Lower-paying jobs to worker dissimilarity assesses the level of worker-job segregation within a census tract relative to all other tracts in the state of Georgia. Both variables are valuable for comparison with the job accessibility index constructed from a gravity-based model. Indeed, I assessed the variance inflation factor to ensure that the inclusion of these two variables does not pose any issues.

_Job Accessibility Index for lower-paying jobs_ <br>
Jin and Paulsen (2018) find that increases in job accessibility lead to decreases in unemployment for African Americans. Their findings also show that increased job accessibility reduces unemployment and improves household income for low-income households (p. 108).

## Methods
- Gravity-based Accessibility Measure
- Ordinary Least Regression
- Spatial Regression

