## Nate Butler 7/20/19 GEOG 682 final
 
 #add crime spots shapefiles to the map
crime_data = "G:/geog 682 final/Crime_Incidents_in_2017.shp" 
crime_shp = iface.addVectorLayer(crime_data,"Crime data","ogr") 

#add election wards to the map 
election_wards = "G:/geog 682 final/Ward_from_2012.shp"
shp =  QgsVectorLayer(election_wards, 'Ward_from_2012.shp', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)

#add shot spotter gun shots data
shot_spotter = "G:/geog 682 final/Shot_Spotter_Gun_Shots.shp"
shp =  QgsVectorLayer(shot_spotter, 'Shot_Spotter_Gun_Shots.shp', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)

## Join Polygons by location (wards and Gun incidents)
import processing  
processing.runalg("qgis:joinattributesbylocation",{
"TARGET":"G:/geog 682 final/Ward_from_2012.shp", 
"JOIN":"G:/geog 682 final/GUN_CRIMES.shp", 
"PREDICATE":u'contains',   
"SUMMARY":1,
"KEEP":0,
"OUTPUT":"G:/geog 682 final/crime_wards.shp"})

## Join Polygons by location (wards and shot spotter gun shots)
import processing  
processing.runalg("qgis:joinattributesbylocation",{
"TARGET":"G:/geog 682 final/Ward_from_2012.shp", 
"JOIN":"G:/geog 682 final/Shot_Spotter_Gun_Shots.shp", 
"PREDICATE":u'contains',   
"SUMMARY":1,
"KEEP":0,
"OUTPUT":"G:/geog 682 final/Shot_Spotter_Gun_wards.shp"})

## Load crime_wards layer to QGIS
crime_wards = "G:/geog 682 final/crime_wards.shp"
crime_shp =  QgsVectorLayer(crime_wards, 'crime_wards.shp', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(crime_shp)  

##Load Shot_Spotter_Gun_Wards layer to QGIS
Shot_Spotter_Gun_wards = "G:/geog 682 final/Shot_Spotter_Gun_wards.shp"
Shot_Spotter_shp =  QgsVectorLayer(Shot_Spotter_Gun_wards, 'Shot_Spotter_Gun_wards.shp', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(Shot_Spotter_shp)

## Calculate the number of gun crimes per 10,000 people in each ward.
for feature in crime_shp.getFeatures():
    num = (feature['count'] / feature['POP_2011_2']) * 10000
    print("Gun crimes in ward {ward} per 10000 people: {number:.2f}").format(ward=feature['WARD'],number=num)

## calculate the number of shooting incidents detected by ShotSpotter per 10,000 people in each ward
for feature in Shot_Spotter_shp.getFeatures():
    num = (feature['count'] / feature['POP_2011_2']) * 10000
    print("Shooting incidents in ward {ward} per 10000 people: {number:.2f}").format(ward=feature['WARD'],number=num)