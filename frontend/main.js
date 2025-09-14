$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    speed: 1500,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });

  var wave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    style: "ios9",
    amplitude: "2",
    speed: "0.05",
    height: 200,
    frequency: 1,
    autostart: true,
  });

  $("#MicBtn").click(function () {
    const clickSound = new Audio("assets/audio/jrsound.mp3");
    clickSound.play();
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.takeCommand()()                             // Call the Python function here
  });
});