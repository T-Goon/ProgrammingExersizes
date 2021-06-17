// Shows the login page
exports.show_login = function(req, res, next) {
    res.render('user/login', { title: 'Express', formData: {}, errors: {} });
}

// Shows the user signup page
exports.show_signup = function(req, res, next) {
    res.render('user/signup', { title: 'Express', formData: {}, errors: {} });
}

exports.show_signup = function(req, res, next) {
    
}