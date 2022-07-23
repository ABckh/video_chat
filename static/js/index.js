function enableUiControls(localStream) {

    $("#mic-btn").prop("disabled", false);
    $("#video-btn").prop("disabled", false);
    $("#exit-btn").prop("disabled", false);

    $("#mic-btn").click(function () {
        toggleMic(localStream);
    });

    $("#video-btn").click(function () {
        toggleVideo(localStream);
    });

    $("#exit-btn").click(function () {
        leaveChannel();
    });

    $(document).keypress(function (e) {
        switch (e.key) {
            case "m":
                console.log("quick toggle the mic");
                toggleMic(localStream);
                break;
            case "v":
                console.log("quick toggle the video");
                toggleVideo(localStream);
                break;
            case "q":
                console.log("so sad to see you quit the channel");
                leaveChannel();
                break;
            default: 
        }

     
        if (e.key === "r") {
            window.history.back();
        }
    });
}

function toggleBtn(btn) {
    btn.toggleClass('btn-dark').toggleClass('btn-danger');
}

function toggleMic(localStream) {
    toggleBtn($("#mic-btn")); 
    $("#mic-icon").toggleClass('fa-microphone').toggleClass('fa-microphone-slash');
    if ($("#mic-icon").hasClass('fa-microphone')) {
        localStream.unmuteAudio(); 
        toggleVisibility("#mute-overlay", false); 
    } else {
        localStream.muteAudio(); 
        toggleVisibility("#mute-overlay", true); 
    }
}

function toggleVideo(localStream) {
    toggleBtn($("#video-btn")); 
    $("#video-icon").toggleClass('fa-video').toggleClass('fa-video-slash'); 
    if ($("#video-icon").hasClass('fa-video')) {
        localStream.unmuteVideo();
        toggleVisibility("#no-local-video", false); 
    } else {
        localStream.muteVideo();
        toggleVisibility("#no-local-video", true);
    }
}