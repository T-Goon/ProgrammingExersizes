let createError = require('http-errors');

exports.isLoggedIn = function(req, res, next) {
    if (req.user) {
        next();
    } else {
        // Execution chain stops, send an error
        next(createError(404, 'Page does not exist. Please log in.'));
    }
}

exports.hasAuth = function(req, res, next) {
    if (req.user && req.user.isadmin == true) {
        next();
    } else {
        next(createError(404, 'Page does not exist for this user.'));
    }
}