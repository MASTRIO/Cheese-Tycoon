// Variables
let inputCommand = "";

function formChanged() {
    inputCommand = document.getElementById("commandBox").value;

    if (inputCommand == "/test")
    alert(inputCommand);

    document.getElementById("airCookerRedeem").innerHTML = '<form action="/index.html"><input type="text" id="commandBox" value="" placeholder="Type /help for a list of commands" style="width: 80%;"><input type="submit" onclick="formChanged()" value="Run"></form>';
}