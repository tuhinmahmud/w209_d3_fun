// require mongoose
var mongoose = require('mongoose');

// create our schema
var locSchema = new mongoose.Schema({
	name: String,
  date_time: Date,
  user_id : Number,
  altitude : Number,
  longitude : Number,
  latitude : Number,
  created_at : Date,
  transport : String
})

// turn the schema into a model
mongoose.model('Loc', locSchema);

// we don't need to export anything because "require" runs the code. see the mongoose.js file in the config folder