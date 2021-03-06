var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
let passport = require('passport');
let session = require('express-session');
const flash = require('connect-flash');
// database setup
var { Pool } = require('pg');
const pg_username = process.env.PG_USERNAME;
const pg_password = process.env.PG_PASSWORD;
var pool = new Pool({
  connectionString: process.env.DATABASE_URL || 'postgresql://'+pg_username+':'+pg_password+'@localhost:5432/'+pg_username,
  ssl: process.env.DATABASE_URL ? { rejectUnauthorized: false } : false 
});
// ssl: { rejectUnauthorized: process.env.DATABASE_URL ? true : false }
exports.pool = pool;

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

// Setup passport
require('./passport_setup')(passport);

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use(flash());

// session and passport setup for authentication
// NOTE: do not change order of lines
app.use(session({ secret: 'my secret' }));
app.use(passport.initialize());
app.use(passport.session());



// Website routes
app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error', { title: 'Error' });
});

module.exports = app;
