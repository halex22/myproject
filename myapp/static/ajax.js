$(document).ready(
    console.log("What would we do with the drunken sailor ?")    
)


function activateBtn() {
    const endpointURL = $("#endpoint").val();
    const token = $("input").val();
    const artistID = $("#artist_id").val();
    console.log($("#artist_id").val());
    
    $.ajax({
        type: "POST",
        url: endpointURL,
        headers: {
            'X-CSRFToken': token
        },
        data: {"artist_info": artistID},
        success: (res) => {
            console.log(res);
        },
        error: (res) => {
            alert("An error acourred. Please try again.");
        }        
    })
};
