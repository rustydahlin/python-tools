#-------------------------------------------------------------------------------
# Name:        Declaration Map Export
# Purpose:     Exports PDFS from pre-made MXDs and puts them on the webserver
#
# Author:      jstonneson
#
# Created:     10/05/2013
# Copyright:   (c) jstonneson 2013
#-------------------------------------------------------------------------------

import arcpy
import arcpy.mapping
import os
import ftplib
import sys
import time
date_string = time.strftime("%Y%m%d")

user ="USERNAME"
password = "PASSWORD"

ip = "FTP IP ADDRESS"

mxd = arcpy.mapping.MapDocument(r"\\SERVERNAME\ITD\GISData\FireIndexBackMapPublishToWebImage.mxd")
arcpy.mapping.ExportToPNG(mxd, "C:\PDFDump\FireIndex.png")
arcpy.mapping.ExportToPNG(mxd, r'\\SERVERNAME\desit\backups\FireIndexDaily\ '+ date_string +'-FireIndexDaily.png')

#mxd = arcpy.mapping.MapDocument(r"\\SERVERNAME\ITD\GISData\FloodDeclarations.mxd")
#arcpy.mapping.ExportToPDF(mxd, "C:\PDFDump\FloodDeclarations.pdf")

#mxd = arcpy.mapping.MapDocument(r"\\SERVERNAME\ITD\GISData\Flood_Declarations_May_17_TBD_2013.mxd")
#arcpy.mapping.ExportToPDF(mxd, "C:\PDFDump\Flood_Declarations_May_17_TBD_2013.pdf")

#mxd = arcpy.mapping.MapDocument(r"\\SERVERNAME\ITD\GISData\Summer_Storms_Declarations_2013.mxd")
#arcpy.mapping.ExportToPDF(mxd, "C:\PDFDump\summer.pdf")

#mxd = arcpy.mapping.MapDocument(r"\\SERVERNAME\ITD\GISData\Winter_Storms_Declarations_2013.mxd")
#arcpy.mapping.ExportToPDF(mxd, "C:\PDFDump\winter.pdf")

ftp = ftplib.FTP(ip, user, password)
ftp.cwd("des/ndelevationLookup/firedeclarations")
ftp.storbinary('STOR FireIndex.png', open("C:\PDFDump\FireIndex.png", 'rb'))

#ftp = ftplib.FTP(ip, user, password)
#ftp.cwd("des/NDElevationLookup/FloodDeclarations")
#ftp.storbinary('STOR FloodDeclarations.pdf', open("C:\PDFDump\FloodDeclarations.pdf", 'rb'))

#ftp = ftplib.FTP(ip, user, password)
#ftp.cwd("des/NDElevationLookup/SummerStorms")
#ftp.storbinary('STOR Flood_Declarations_May_17_TBD_2013.pdf', open("C:\PDFDump\Flood_Declarations_May_17_TBD_2013.pdf", 'rb'))

#ftp = ftplib.FTP(ip, user, password)
#ftp.cwd("des/NDElevationLookup")
#ftp.storbinary('STOR summer.pdf', open("C:\PDFDump\summer.pdf", 'rb'))

#ftp = ftplib.FTP(ip, user, password)
#ftp.cwd("des/NDElevationLookup")
#ftp.storbinary('STOR winter.pdf', open("C:\PDFDump\winter.pdf", 'rb'))