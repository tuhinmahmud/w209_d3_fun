##Instructions to run website on local machine:
####Install Nodejs
http://howtonode.org/how-to-install-nodejs
####After successful installation, install nodemon
```
npm install -g nodemon
```
####Must also install mongodb
http://docs.mongodb.org/manual/installation/
####Clone this repository to your local computer
```
git clone https://github.com/maktrix16/w209_d3_fun.git
```
####Start mongodb server
```
sudo mongod
```
####Go to repository folder and load data into MongoDB
```
#two arugments are needed (1) the datafile and (2) boolean value for whether to remove data from existing database
python data/load.py data/test_data.txt T

#you may need to install pymongo package (just do "pip install pymongo")
```
####Check if data loaded properly by starting Mongo client to check
```
mongo
```
####Enter these commands to see if data exists properly
```
use w209project
db.locations.count()   #this should return value of 10
db.locations.find({}).pretty()   #this should return all the values being stored
```

####Once confirm data ok, go to new terminal window and start Node server (note: you must do have already started your MongoDB server at this point)
```
nodemon website/server.js
```
####Open web browser and go to following link to view website
http://localhost:8000/


