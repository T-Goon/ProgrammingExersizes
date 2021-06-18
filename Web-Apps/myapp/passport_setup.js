const pool = require('./app');
let LocalStrategy = require('passport-local').Strategy;
let bcrypt = require('bcrypt');
const flash = require('connect-flash');

// Checks if password is valid
const vailidPassword = function(user, password) {
    // compares hashes
    return bcrypt.compareSync(password, user.password);
}

// Setup passport for authentication
module.exports = function(passport) {
    // Saves data for the session
    passport.serializeUser(function(user, done) {
        done(null, user.id);
    }); 

    // Gets user object from data saved in serializeUser()
    passport.deserializeUser(async function(id, done) { 
        try{
            const client = await pool.pool.connect();
        
            const result = await client.query('SELECT * FROM users WHERE id=\''+id+'\';');
        
            client.release();

            if(result.rowCount == 0) {
                done(new Error('Wrong user id.'));
            }

            if(result.rowCount > 1) {
                done(new Error('User id not unique.'));
            }

            done(null, result.rows[0]);

          } catch (err){
            done(err, false);
          }
    }); 

    // Authentification function
    passport.use(new LocalStrategy(
        {
            usernameField: 'email', // names of input fields
            passwordField: 'password',
            passReqToCallback: true
        },
        async function(req, email, password, done) {
            try{
                const client = await pool.pool.connect();

                if(req.path == '/signup') {
                    const result = await client.query('SELECT * FROM users \
                    WHERE email=\''+email+'\';');

                    if(result.rowCount > 0){
                        req.flash('message', "Email in use.");
                        return done(null, false);
                    }
                }
            
                const result = await client.query('SELECT * FROM users WHERE email=\''+email+'\';');
            
                client.release();
    
                if(result.rowCount == 0) {
                    req.flash('message', 'Incorrect credentials.');
                    return done(null, false);
                } else if(result.rowCount > 1) {
                    return done(null, false);
                } else if(result.rows[0].password == null || result.rows[0].password == undefined) {
                    req.flash('message', 'You must reset your password.');
                    return done(null, false);
                } else if(!vailidPassword(result.rows[0], password)) {
                    req.flash('message', 'Incorrect credentials');
                    return done(null, false);
                } else {
                    return done(null, result.rows[0]);
                }
    
              } catch (err){
                console.log(err);
                done(err, false);
              }
        }
    ));
}