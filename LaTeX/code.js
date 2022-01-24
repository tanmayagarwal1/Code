document.getElementById("submitBtn").addEventListener("click", e =>{
    e.preventDefault();
    var elements = document.getElementById("championForm").elements;
    var submitter_name = document.getElementById("submitter_name").value;
    var submitter_phone = document.getElementById("submitter_phone").value;
    var submitter_email = document.getElementById("submitter_email").value;
    var submitter_state = document.getElementById("submitter_state").value;
    var champion_name = document.getElementById("champion_name").value;
    var champion_phone = document.getElementById("champion_phone").value;
    var champion_email = document.getElementById("champion_email").value;
    var champion_state = document.getElementById("champion_state").value;
    var comment1 = document.getElementById("comment1").value;
    var comment2 = document.getElementById("comment2").value;

    if(document.getElementById("dot-1").checked){
        var submitter_isAnonymous = true;
    }
    else{
        var submitter_isAnonymous = false;
    }
    const arr = {"fields" : [
        {
            "model" : "submitter_name",
            "value" : submitter_name
        },
        {
            "model" : "submitter_phone",
            "value" : submitter_phone
        },
        {
            "model" : "submitter_email",
            "value" : submitter_email
        },
        {
            "model" : "submitter_state",
            "value" : submitter_state
        },
        {
            "model" : "champion_name",
            "value" : champion_name
        },
        {
            "model" : "champion_phone",
            "value" : champion_phone
        },
        {
            "model" : "champion_email",
            "value" : champion_email
        },
        {
            "model" : "champion_state",
            "value" : champion_state
        },
        {
            "model" : "comment1",
            "value" : comment1
        },
        {
            "model" : "comment2",
            "value" : comment2
        },
        {
            "model" : "submitter_isAnonymous",
            "value" : submitter_isAnonymous
        },
        {
            "model" : "image",
            "value" : base64String
        },
    ]};

    console.log(JSON.stringify(arr));
    alert("form submitted");

})

let base64String = "";
  
function imageUploaded() {
    var file = document.querySelector(
        'input[type=file]')['files'][0];
  
    var reader = new FileReader();
    console.log("next");
      
    reader.onload = function () {
        base64String = reader.result.replace("data:", "")
            .replace(/^.+,/, "");
  
        imageBase64Stringsep = base64String;
  
        // alert(imageBase64Stringsep);
        console.log(base64String);
    }
    reader.readAsDataURL(file);
}