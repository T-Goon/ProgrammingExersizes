const pool = require('../app')

// Show default landing page
exports.get_landing = function(req, res, next) {
    res.render('landing', { title: 'Express' });
  }

// Submit a lead email
exports.submit_lead = async function(req, res, next) {

  console.log('lead email:', req.body.lead_email);

  // Log email in the database
  try{
    const client = await pool.pool.connect();

    const result = await client.query('INSERT INTO leads (createdOn, updatedOn, email) \
    VALUES ('
    + 'NOW()::date' + ', '
    + 'NOW()::date' + ', '+
     '\''+req.body.lead_email+'\');');
    client.release();
  } catch (err){
    console.error(err);
    res.send("Error "+err)
  }

  res.redirect('/leads');
}

// Shows a list of all leads
exports.show_leads = async function(req, res, next) {
  let rows;

  // Get all leads
  try{
    const client = await pool.pool.connect();

    const result = await client.query('SELECT * FROM leads;');

    res.render('landing', { title: 'Express', leads: result.rows})

    client.release();
  } catch (err){

    console.error(err);
    res.send("Error "+err)
  }
}

exports.show_lead = async function(req, res, next) {

  // Get all leads
  try{
    const client = await pool.pool.connect();

    const result = await client.query('SELECT * FROM leads WHERE id=\''+req.params.lead_id+'\';');

    res.render('lead', { lead: result.rows[0] });

    client.release();
  } catch (err){

    console.error(err);
    res.send("Error "+err)
  }
}

// Show edit form for a lead
exports.show_edit_lead = async function(req, res, next) {

  // Get all leads
  try{
    const client = await pool.pool.connect();

    const result = await client.query('SELECT * FROM leads WHERE id=\''+req.params.lead_id+'\';');

    res.render('lead/edit_lead', { lead: result.rows[0] });

    client.release();
  } catch (err){

    console.error(err);
    res.send("Error "+err)
  }
}

// Edits a lead
exports.edit_lead = async function(req, res, next) {
  // req.params.lead_id - from path
  // req.body.lead_email - from html page

  // Edits a specific lead
  try{
    const client = await pool.pool.connect();

    const result = await client.query('UPDATE leads SET email=\''+req.body.lead_email+'\' WHERE id=\''+req.params.lead_id+'\';');

    res.redirect('/lead/'+ req.params.lead_id);

    client.release();
  } catch (err){

    console.error(err);
    res.send("Error "+err)
  }
}

// Deletes a lead
exports.delete_lead = async function(req, res, next) {

  // Deletes a lead
  try{
    const client = await pool.pool.connect();

    const result = await client.query('DELETE FROM leads WHERE id=\''+req.params.lead_id+'\';');

    res.redirect('/leads');

    client.release();
  } catch (err){

    console.error(err);
    res.send("Error "+err)
  }
}