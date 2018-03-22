#This script is used to create an ArcGIS tool which will add a new field named HEX and populate it.
#Requires a file in Python dictionary format of Key: Value pairs representing Attribute: Hex colors.
#This is used to add custom colors used in the leaflet symbology for the layer containing geologic units.

import arcpy
import ast

#parameters
shpFile = arcpy.GetParameterAsText(0) #shapefile
field = arcpy.GetParameterAsText(1) #field from shapefile
hexDictFile = arcpy.GetParameterAsText(2) #file

#open hex dictionary file and store in variable
myFile = open(hexDictFile)
hexDict = ast.literal_eval(myFile.read())
myFile.close()

#Add HEX field to shapefile
arcpy.AddField_management(shpFile,"HEX","TEXT","#","#","6","#","NULLABLE","NON_REQUIRED","#")

#initiate cursor
cursor = arcpy.UpdateCursor(shpFile)
row = cursor.next()

#iterate over rows
while row:
    #check current value of field
    currentVal = row.getValue(field)
    #if value exists set value
    if currentVal in hexDict:
        row.setValue("HEX", hexDict[currentVal])
    cursor.updateRow(row)
    row = cursor.next()