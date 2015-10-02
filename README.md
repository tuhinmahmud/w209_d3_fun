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
python data/load.py data/test_data.txt
```
####Start Node server (note: you must do have already started your MongoDB server at this point)
```
mongod website/server.js
```
####Open web browser and go to following link to view website
http://localhost:8000/


