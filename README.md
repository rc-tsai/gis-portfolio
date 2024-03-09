# gis-portfolio


This project attempts to identify bald eagles’ habitat in Georgia by looking for a natural environment that provides a suitable location and enough food sources. The criteria used for selecting a location are as follows.


## Suitability mode

The ordinal combination is used to evaluate the suitability of potential habitat for bald eagles in Georgia. I concatenated the layers to identify potential habitat. However, this is an intermediate result. The final result will be detailed, followed by the maps in the next few pages.

<img src="Pbppm.jpg" width=50% height=50%/>



<!-- 
  IMPORTANT! 
  
  Keep this file unchanged to use as a template for all future project pages. 
  For every new project you add to your portfolio, make a copy of this file in the
  'project-pages' folder with a name related to the project.
-->


<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
    <!-- 
      TODO
      Upload your Unemployable (or whatever photo you like) to the assets/images folder
      and change the name of the image below to match the uploaded one
      Change the title in the <title> tag to whatever you would like the title of your portfolio to be
      This should be the same across all pages.
     -->
     <link rel="icon" href="../assets/images/GISMapping_Walmart.jpg" />
     <title>My GIS Journey</title>
    <meta name="description" content="A GIS portfolio made by Danaée Félix.">
    <meta name="viewport" content="width=device-width, initial-scale=1" />

		<link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/typography.css">
    <link rel="stylesheet" href="../css/utilities.css">

		<script defer src="../js/script.js"></script>
	</head>
	<body>
    <!-- NAVBAR -->
    <div class="navbar">
      <a class="nav-title-link" href="../index.html">
        <!-- 
          TODO - Change the "Portfolio Title" to whatever you want displayed in the top left
          (this should be the same across all pages)
         -->
        <span class="nav-title">My GIS Journey</span>
        <!-- 
          TODO - Change the email after 'mailto:' to your email address for contact 
        
          (this should be the same across all pages)
        -->
        <a class="button" href="mailto:danaeefel@gmail.com">
          <span class="button-text">Contact Me</span>
        </a>
      </a>
    </div>

    <!-- MAIN PAGE CONTENT -->
    <div id="main-content">

      <!-- PROJECT HEADER -->
      <div id="project-header">
          <!-- 
            TODO
            - Change the 'main-title' text to the name of your project
            - Change the 'body-text' text to a short and sweet description of your project (maybe the same as the one on the project card)
            - Change "desktop.jpeg" to the image filename you uploaded in the assets/images folder.
          -->
        <div class="main-title">Walmart Invasion</div>
        <div class="body-text">With Walmart being such a popular store, it guesses the question "where is this company most popular?" Lets find out.</div>
        <image class="project-header-image" src="../assets/images/GISMapping_Walmart.jpg">
      </div>

      <!-- PROJECT DETAILS -->
      <!-- 
        TODO
        - Change the 'subheader-text' to whatever header you want for project details
        - Add paragraphs using the <div class="body-text"></div> elements in the "project-details-content"
      -->
      <div id="project-details">
        <div class="subheader-text">Background on the Walmart Invasion</div>
        <div class="project-details-content">
          <div class="body-text">Map displays the layout of Walmart stores per capita within the United States from Econometrica, Inc.’s 2011 data. The data’s attribute table revealed that California has he least Walmart stores per capita, meanwhile Arkansas has the most Walmart stores per capita. Additionally, Texas has the most Walmart stores, as it leads with 315 Walmart stores from when this data was published. Furthermore, this analysis concludes that the popular retail corporation is more dominant in rural areas in comparison to urban places.</div>
        </div>
      </div>

      <!-- IMAGE GALLERY -->
      <div id="project-gallery">
        <!-- TODO - Change the 'subheader-text' to whatever you want the Gallery section header to say -->
        <div class="subheader-text">More Maps!</div>
        <div class="project-gallery-content">
            <!-- 
              TODO
              This is where the images in the gallery live. Here's a simple gallery image for you to copy:
              Full Width Image:
                <div class="gallery-image-container">
                  <img src="../assets/images/GISMapping_Walmart.jpeg" class="gallery-image">
                  <span class="image-caption">Map displays the ditribution of Walmart stores in America.</span>
                </div>
              Half Width Image: 
                <div class="gallery-image-container half-width">
                  <img src="../assets/images/GISMapping_Walmart.jpg" class="gallery-image">
                  <span class="image-caption">IMAGE_CAPTION</span>
                </div>
              - To add an image to the this area, copy one of the above, paste it below this comment, and change the following:
                  - IMAGE_NAME: the name of the image file in assets/images
                  - IMAGE_CAPTION: to the caption of the image
            -->
            <div class="gallery-image-container half-width"> JAPAN'S GEOGRAPHY
              <img src="../assets/images/QGIS_Japan_Map.png" class="gallery-image">
              <span class="image-caption">Unlike the Walmart Invasion map, this map of Japan was created via QGIS. This was my first map ever made with an open-sourced GIS software. Creating the map was fun as I gained a better understanding of the proximity of Japan to its neighbouring countries, while also earning experience with QGIS.</span>
	    <div class="gallery-image-container"> THE SEPTIC SYSTEM IN TEXAS
              <img src="../assets/images/GIS_Texas_Population.jpg" class="gallery-image">
              <span class="image-caption">This map contains data for identify and analyzing areas in Texas affected by the septic system. Septic systems contribute wastewater, thus very hazardour to humans. Such areas impacted by a septic system are located in Austin, Texas and have less than 1,000 people. The highlighted geology in the map above also contains a distribution of limestone, terrace, and alluvium.</span>
            </div>
        </div>
      </div>
    </div>

    <!-- FOOTER -->
    <div id="footer">
      <!-- 
        TODO - Change href to your Phone number account (can also delete entire "a" element if no Phone) 
        This should be the same across all pages.
      -->
      <a class="icon-link" target="_blank" href="tel:207-460-1500">
        <image src="../assets/icons/Phone_call.svg" class="footer-icon"/>
      </a>
      <!-- 
        TODO - Change href to your LinkedIn account (can also delete entire "a" element if no LinkedIn) 
      
        This should be the same across all pages.
      -->
      <a class="icon-link" target="_blank" href="http://www.linkedin.com/in/danaéefélix">
        <image src="../assets/icons/LinkedIn_icon.svg" class="footer-icon"/>
      </a>
      <!-- 
        TODO - Change the email after "mailto" to your contact email 
      
        This should be the same across all pages.
      -->
      <a class="icon-link" href="mailto:danaeefel@gmail.com">
        <image src="../assets/icons/Gmail_icon.svg" class="footer-icon"/>
      </a>
    </div>

	</body>
</html> 

