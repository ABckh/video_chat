$("#join-channel").click(function (event) {
    var agoraAppId = "a6af85f840ef43108491705e2315a857";
    var channelName = $('#form-channel').val();
    initClientAndJoinChannel(agoraAppId, channelName, token);
    $("#modalForm").modal("hide");
});

function enableUiControls(localStream) {

    $("#mic-btn").prop("disabled", false);
    $("#video-btn").prop("disabled", false);
    $("#screen-share-btn").prop("disabled", false);
    $("#exit-btn").prop("disabled", false);

    $("#mic-btn").click(function () {
        toggleMic(localStream);
    });

    $("#video-btn").click(function () {
        toggleVideo(localStream);
    });

    $("#screen-share-btn").click(function () {
        toggleScreenShareBtn();
        $("#screen-share-btn").prop("disabled", true); 
        if (screenShareActive) {
            stopScreenShare();
        } else {
            initScreenShare();
        }
    });

    $("#exit-btn").click(function () {
        leaveChannel();
    });

    $(document).keypress(function (e) {
        switch (e.key) {
            case "m":
                console.log("squick toggle the mic");
                toggleMic(localStream);
                break;
            case "v":
                console.log("quick toggle the video");
                toggleVideo(localStream);
                break;
            case "s":
                console.log("initializing screen share");
                toggleScreenShareBtn(); 
                $("#screen-share-btn").prop("disabled", true);
                if (screenShareActive) {
                    stopScreenShare();
                } else {
                    initScreenShare();
                }
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

function toggleScreenShareBtn() {
    $('#screen-share-btn').toggleClass('btn-danger');
    $('#screen-share-icon').toggleClass('fa-share-square').toggleClass('fa-times-circle');
}

function toggleVisibility(elementID, visible) {
    if (visible) {
        $(elementID).attr("style", "display:block");
    } else {
        $(elementID).attr("style", "display:none");
    }
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