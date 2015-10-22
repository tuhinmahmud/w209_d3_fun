import sys
import os
import json
import pymongo
import datetime, pytz
import re
from pymongo import MongoClient
# from datetime import datetime
# from dateutil import tz
#following needed for processing zipped files
import glob
import csv
import zipfile
import StringIO

class LoadData():

    client = MongoClient('localhost', 27017)
    db = client.w209project #create/set database name as "w209project"
    collection = db.locs    #create/set collection name as "locs"
    
    def removeData(self):
        self.collection.remove({})
    
    def load(self,data_file):
        with open(data_file, 'r') as f:
            for line in f:
                user_id,latitude,longitude,altitude,date,time,transport = line.strip().split(',')
                user_id = int(user_id)
                latidude = float(latitude)
                longitude = float(longitude)
                altidude = float(altitude)

                #ensure it's china timezone to ensure correct timezone input
                local = pytz.timezone ("Asia/Shanghai")
                naive = datetime.datetime.strptime (date+" "+time, "%Y-%m-%d %H:%M:%S")
                local_dt = local.localize(naive, is_dst=None)
#                 utc_dt = local_dt.astimezone (pytz.utc)
#                 print latitude,longitude,altitude,date,time,transport
                
                location = {"user_id":user_id,
                            "latitude":latitude,
                            "longitude":longitude,
                            "altitude":altitude,
                            "date_time":local_dt,
                            "transport":transport,
                            "created_at":datetime.datetime.utcnow()}
                self.collection.insert_one(location)

            print '\n',self.collection.count(),'records loaded into MongoDB'
    ########
    # Following module to load ziped files into mongodb
    #  zipped files in put in the directory dirName in the following format
    #  000.zip contains 000.csv file realated to userid 000
    #  Each file like 000.csv contains comma separted values for each user as follow
    #  
    #########
    def read_zip_files(dirName):
        if not dirName:
            return
        dirStr=dirName+"/*.zip"
        print dirStr
        for name in glob.glob(dirStr):
            base = os.path.basename(name)
            filename = os.path.splitext(base)[0]
            #print "************ %s ***************" % filename


            datadirectory = dirName
            dataFile = filename
            archive = '.'.join([dataFile, 'zip'])
            fullpath = os.path.join(datadirectory, archive)
            csv_file = dataFile


            filehandle = open(fullpath, 'rb')
            zfile = zipfile.ZipFile(filehandle)
            data = StringIO.StringIO(zfile.read(csv_file)) #don't forget this line!
            reader = csv.reader(data)

            for row in reader:
                #print row
                user_id,latitude,longitude,altitude,date,time,transport = row
                user_id = int(user_id)
                latidude = float(latitude)
                longitude = float(longitude)
                altidude = float(altitude)
                #ensure it's china timezone to ensure co
                local = pytz.timezone ("Asia/Shanghai")
                naive = datetime.datetime.strptime (date+" "+time, "%Y-%m-%d %H:%M:%S")
                local_dt = local.localize(naive, is_dst=None)
                #print latitude,longitude,altitude,date,time,transport
                local_dt = local.localize(naive, is_dst=None)
#               utc_dt = local_dt.astimezone (pytz.utc)
#               print latitude,longitude,altitude,date,time,transport
                
                location = {"user_id":user_id,
                            "latitude":latitude,
                            "longitude":longitude,
                            "altitude":altitude,
                            "date_time":local_dt,
                            "transport":transport,
                            "created_at":datetime.datetime.utcnow()}
                self.collection.insert_one(location)

        print '\n',self.collection.count(),'records loaded into MongoDB'
    
if __name__ == '__main__':
    l = LoadData()
    data_file = sys.argv[1]
    remove_data = sys.argv[2]  #if true, then remove existing data
    if remove_data:
        l.removeData()
    l.load(data_file)
