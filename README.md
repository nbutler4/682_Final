# 682_Final Washington DC Crime Analysis 
Nate Butler 7/20/19

Analysis Introduction - 
This final project is a crime analysis describing the patterns of gun releated crimes in Washington D.C. Taken into consideration as data for this analysis where a few data layers: gun crimes commited in 2017 in each ward of D.C and data collected by a technology called gun shot spotter to detect apparent gun shots. This data allowed me to determine the number of gun crimes committed and gun shots detected by shot spotter per 10,000 people in D.C's wards for my analysis.

Analysis of the project-
My analysis required three foundational data layers. Those layers are: "Ward_From_2012.shp", "Shot_Spotter_Gun_Shots.shp", and "Crime_Incidents_in_2017.shp" to proformace my analysis and get results. These three layer are the record's of crimes committed and/or detected in D.C as well as allow for the display of these crimes by ward through "Ward_From_2012.shp". Both of the data layers dealing with crimes in D.C are geocoded to the ward's of D.C that they occurred in. The layer "Crime_Incidents_in_2017.shp" is a data layer of crimes of all kinds of methods committed in 2017. My analysis first isoloated crimes committed through the method of a gun. As a result I was able to join this data to the shapefile layer of the D.C Wards. I could then use that data to determine how many gun crimes were committed and shots detected in the Wards of D.C. Here are links for each data layer: https://opendata.dc.gov/datasets/ward-from-2012, https://opendata.dc.gov/datasets/crime-incidents-in-2017, https://opendata.dc.gov/datasets/89bfd2aed9a142249225a638448a5276_29.

I created two themetic maps to display the results of my analysis. I created the maps using QGIS by uploading my D.C data into the map production tool "Print Compressor". The data displayed are my two crime data layers joined to my Wards layer. The crime layer was filtered through and "gun crime methods" were isoloated. Once that join was completed I begin working on my two seperate thematic maps. The first map "Gun Crimes Map" I divided the total number of gun crimes by the total population and multiplied by 10,000 to geth the number of gun crimes per 10,000 people in each D.C Ward. My second map held to the same method but instead of gun crimes divided by population I used shooting incidents detected by shot spotter for getting the number of shoot incidents detected per 10,000 people. I created a thematic afterward by categorizing the column which held the crime data by its value. 
Embedded image of 1st and 2nd map 
https://raw.githubusercontent.com/nbutler4/D.C-thematic-maps/master/Gun%20Crimes%20map.jpg
https://raw.githubusercontent.com/nbutler4/D.C-thematic-maps/master/Shot%20Spotter%20map.jpg 

Gun crimes committed per 10,000 people in D.C's eight Wards in 2017:
Ward 1 - 14 gun crimes 
Ward 2 - 7 gun crimes
Ward 3 - 3 gun crimes
Ward 4 - 15 gun crimes
Ward 5 - 33 gun crimes
Ward 6 - 19 gun crimes
Ward 7 - 57 gun crimes
Ward 8 - 52 gun crimes

Shooting incidents detected by shot spotter in D.C Wards per 10,000 people in 2017:
Ward 1 - 189 shooting incidents
Ward 2 - 7 shooting incidents
Ward 3 - 0 shooting incidents
Ward 4 - 333 shooting incidents
Ward 5 - 472 shooting incidents
Ward 6 - 270 shooting incidents
Ward 7 - 1323 shooting incidents
Ward 8 - 1610 shooting incidents 

Automated/code funtionality- 
The code that is written for this analysis of D.C crime allows me to automate task for analysis such as uploading the necessary data layers, spatial joining the correct data layers and displaying the calculation of targeted information after a manual islotation performance to gun crimes data. For example, "## Join Polygons by location (wards and shot spotter gun shots)
import processing  
processing.runalg("qgis:joinattributesbylocation",{
"TARGET":"G:/geog 682 final/Ward_from_2012.shp", 
"JOIN":"G:/geog 682 final/Shot_Spotter_Gun_Shots.shp", 
"PREDICATE":u'contains',   
"SUMMARY":1,
"KEEP":0,
"OUTPUT":"G:/geog 682 final/Shot_Spotter_Gun_wards.shp"})" 

This is a code I wrote to spatially join two data layers for the purpose of calculating targeted information for my analysis. 

Again I wrote: "## calculate the number of shooting incidents detected by ShotSpotter per 10,000 people in each ward
for feature in Shot_Spotter_shp.getFeatures():
    num = (feature['count'] / feature['POP_2011_2']) * 10000
    print("Shooting incidents in ward {ward} per 10000 people: {number:.2f}").format(ward=feature['WARD'],number=num)" 
    
in order to automate the task for calculation of data shot spotter detections to population per 10,000 people.

Finally all of my automation code first needed the foundational data files uploaded to perform the analysis. For example,
"#add election wards to the map 
election_wards = "G:/geog 682 final/Ward_from_2012.shp"
shp =  QgsVectorLayer(election_wards, 'Ward_from_2012.shp', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)"
is the code used to upload the Wards piece of data. This is the functionality of my python code.

Results- 
According to the result of my analysis I would recommed that the Wards: 5,7, and 8 be covered by an expanded gunshot dectetion network. These wards are among the highest in gun crimes commited in 2017 therefore in order to deter those crimes the gunshot detection network should be expanded throughout those Wards ontop of the network spots that are already in place.

I think two limitations of my analysis were, one, not every gun crime committed was documented. Not all crimes are documented there may have been gun crimes committed in each D.C ward that were not recorded. Two, suddent population change in any of D.C's wards could make the results of my analysis inaccurate for the purpose of finding the wards that need a gun shot dectetion network expansion. 


