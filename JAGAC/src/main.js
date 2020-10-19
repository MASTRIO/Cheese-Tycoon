var vex = require('vex-js');
vex.registerPlugin(require('vex-dialog'));
vex.defaultOptions.className = 'vex-theme-os';

// Variables
let inputCommand = "";

// Functions
function formChanged() {
    inputCommand = document.getElementById("commandBox").value;
    
    document.getElementById("commandInput").innerHTML = '<form action="/index.html"><input type="text" id="commandBox" value="" placeholder="Type /help for a list of commands" style="width: 80%;"><input type="submit" onclick="formChanged()" value="Run"></form>'    ;
}

function summonBilly() {
    alert("No");

    vex.dialog.prompt({
        message: 'What is ur name',
        placeholder: 'cheese'
    })
}