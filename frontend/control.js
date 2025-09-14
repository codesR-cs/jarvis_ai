$(document).ready(function () {
    eel.expose(DisplayMessage) // Expose the DisplayText function to Python
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message); // Update the text of the first <li> element
        $(".siri-message").textillate('start');        // Restart the textillate animation

    }
    eel.expose(Show)
    function Show(){       //func name is Show thats exposed to python
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
});