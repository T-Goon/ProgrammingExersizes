let validator = require('validator');
const pool = require('../app');

// Add errors if email and password is invalid on sign up
const validateCreateUserFields = function(errors, req) {
    if (!validator.isEmail(req.body.email)) {
        errors['email'] = 'Please use a valid email.';
    } 
    
    if (!validator.isAscii(req.body.password)) {
        errors['password'] = 'Invalid characters in password, please try another.';
    }

    if(!validator.isLength(req.body.password, { min: 8, max: 25 })) {
        errors['password'] = 'Your password must be between 8 and 25 characters.';
    }
}

// Ensures that a new user can be created
exports.validateUser = function(errors, req) {
    return new Promise(async function(resolve, reject) {
        try {

            validateCreateUserFields(errors, req);

            const client = await pool.pool.connect();
    
            const result = await client.query('SELECT * FROM users \
            WHERE email=\''+req.body.email+'\';');

            if(result.rowCount > 0) {
                errors['email'] = 'Email alread in use.';
            }
    
            client.release();
    
          } catch (err) {
            console.log(err);
          }

        resolve(errors);
    });
}