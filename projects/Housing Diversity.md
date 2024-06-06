## About Housing Diversity
Neighborhoods that feature less diverse housing types tend to experience increased rates of foreclosure and property sales. The relationship between foreclosure and sales rates and restrictive zoning differs based on the statistical model used and the region in question. While a limited range of housing types correlates with higher rates of foreclosure and sales, the proportion of borrowers and the vacancy rate have a greater impact on these rates. Additionally, census tracts with more sprawling layouts, defined by factors like development density, mix of land use, location of population and employment centers, and street accessibility, show higher foreclosure rates.

<br>

## Constructing housing diversity index

#### Housing Category
There is a total of 11 variables in the dataset. The dataset includes the number of housing units (both vacant and occupied) in different types and sizes, as well as the number of living quarters that are occupied as housing units. Types of housing units include one-family homes, apartments, and mobile homes. There are two categories of 1-unit housing, include detached and attached.

#### Mobile Home
This category contains occupied and vacant mobile homes with no permanent rooms. Mobile homes used for residential purposes seem counted in this category.

#### 1-Unit, Detached
This category includes detached one-family homes and housing units. Housing units with open space on all four sides fall into this category even if they contain a business.

#### 1-Unit, Attached
Housing units in this category contain two or more housing units. There are six subdivisions in the apartments category.

#### Boat, RV, Van, Etc.
Any living quarter occupied as a housing unit falls into this category if they don’t fit the previous categories. Living quarters such as campers, recreational vehicles, and houseboats are included only if they show signs of place of residence.

## Calculation
Housing diversity index contains three formulas as follows:
#### Proportions calculation formula

<p align="center">
  <img width="100%" height="100%" src="../images/Housing Diversity/proportions.png">
</p>

<br>

#### Log of the proportions calculation formula

<p align="center">
  <img width="100%" height="100%" src="../images/Housing Diversity/log of the proportions.png">
</p>

<br>

#### Product of the proportions and their respective logs formula

<p align="center">
  <img width="100%" height="100%" src="../images/Housing Diversity/product of the proportions.png">
</p>

<br>

## Housing Diversity Index for Georgia state

<p align="center">
  <img width="80%" height="80%" src="../images/Housing Diversity/HDIndex.jpg">
</p>

I chose to use natural break classification to map the housing diversity index. Given the nature of natural break classification, we can see the housing diversity comparison more vividly across urban and rural areas in Georgia. Housing diversity is usually higher in urbanized areas, especially in part of the Atlanta Metropolitan Area (AMA). The areas with higher housing diversity in AMA seems to located along highway.
