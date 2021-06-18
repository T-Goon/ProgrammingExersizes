const passport = require('passport');
const myPassport = require('../passport_setup')(passport);
const pool = require('../app');
const bcrypt = require('bcrypt');
const flash = require('connect-flash');

// Shows the login page
exports.show_login = function(req, res, next) {
    res.render('user/login', { title: 'Express', formData: {}, errors: {} });
}

// Shows the user signup page
exports.show_signup = function(req, res, next) {
    res.render('user/signup', { title: 'Express', formData: {}, errors: {} });
}

// Hash and salt password with bcrypt
const generateHash = function(password){
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
}

// Signup submit
exports.signup = async function(req, res, next) {
    const password = generateHash(req.body.password);

    try{
        const client = await pool.pool.connect();
    
        const result = await client.query('INSERT INTO users (email, password) \
        VALUES ('
        + '\'' + req.body.email + '\', '
        + '\''+ password + '\') ON CONFLICT DO NOTHING;');
    
        client.release();
      } catch (err){
        console.error(err);
      }
    
      passport.authenticate('local', {
          successRedirect: '/',
          failureRedirect: '/signup',
          failureFlash: true
      })(req, res, next);
}

// Login submit
exports.login = function(req, res, next) {
    passport.authenticate('local', {
        successRedirect: '/',
        failureRedirect: '/login',
        failureFlash: true
    })(req, res, next);
}

// Logout get and post
exports.logout = function(req, res, next) {
    req.logout();
    req.session.destroy();
    res.redirect('/');
}