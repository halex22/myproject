$(document).ready(
    console.log("What would we do with the drunken sailor ?")    
)


function addFavArtist(x) {
    const endpointURL = $("#endpoint").val();
    const token = $("input").val();
    const artistID = $("#artist_id").val();
    console.log($("#artist_id").val());
    
    $.ajax({
        type: "POST",
        url: endpointURL,
        headers: {'X-CSRFToken': token},
        data: {"artist_info": artistID},
        success: (res) => {
            console.log(res);
            $(x).hide(); // hide the clicked button 
        },
        error: (res) => {
            alert("An error acourred. Please try again.");
        }        
    })
};


function hideBtn(x) {
    console.log($(x));
    $(x).hide();
}