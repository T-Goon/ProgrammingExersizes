function deleteLead(leadId){

    $.ajax({
        url: '/lead/'+ leadId + '/delete-json', // route to execute
        contentType: 'application/json; charset-utf-8',
        dataType: 'json',
        data: JSON.stringify({leadId}),
        type: 'POST',
        success: ((res) => {
            // Replace follow button with unfollow
            console.log('Result: '+ res);
            $('#'+leadId).remove(); // Remove html element with id
        }),
        error: ((error) => {
            console.log('Error: '+ error);
        })
    });
}