
function dateValidation() {
    let date_input = document.getElementsById("appointment-form").elements["date"];
    let output = document.getElementsById("appointment-form").elements["message"];
    var today = date_input.value;
    output.innerHTML = today.value;
}