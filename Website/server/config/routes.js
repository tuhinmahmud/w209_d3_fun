var locs = require('../controllers/locs');

module.exports = function(app) {
	app.get('/getLocs',function(req,res){
		locs.getLocs(req,res);
	});
	// app.post('/addUser',function(req,res){
	// 	users.addUser(req,res);
	// });
	// app.post('/removeUser', function(req, res) {
	// 	users.removeUser(req,res);
	// });
	// app.post('/editUser', function(req, res) {
	// 	users.editUser(req, res);
	// });
}