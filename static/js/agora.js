
var cameraVideoProfile = '480p_4';
var screenVideoProfile = '480p_2';

var client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });
var screenClient = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });

var remoteStreams = {}; 

var localStreams = {
    camera: {
        id: "",
        stream: {}
    },
    screen: {
        id: "",
        stream: {}
    }
};

var mainStreamId;
var screenShareActive = false; 

function initClientAndJoinChannel(agoraAppId, channelName, token, userID) {
    client.init(agoraAppId, function () {
        console.log("AgoraRTC client initialized");
        joinChannel(channelName, token, userID); 
    }, function (err) {
        console.log("[ERROR] : AgoraRTC client init failed", err);
    });
}


client.on('stream-published', function (evt) {
    console.log("Publish local stream successfully");
});

client.on('stream-added', function (evt) {
    var stream = evt.stream;
    var streamId = stream.getId();
    console.log("new stream added: " + streamId);
    if (streamId != localStreams.screen.id) {
        console.log('subscribe to remote stream:' + streamId);
        client.subscribe(stream, function (err) {
            console.log("[ERROR] : subscribe stream failed", err);
        });
    }
});

client.on('stream-subscribed', function (evt) {
    var remoteStream = evt.stream;
    var remoteId = remoteStream.getId();
    remoteStreams[remoteId] = remoteStream;
    console.log("Subscribe remote stream successfully: " + remoteId);
    if ($('#full-screen-video').is(':empty')) {
        mainStreamId = remoteId;
        remoteStream.play('full-screen-video');
    } else {
        addRemoteStreamMiniView(remoteStream);
    }
});

client.on("peer-leave", function (evt) {
    var streamId = evt.stream.getId();
    if (remoteStreams[streamId] != undefined) {
        remoteStreams[streamId].stop();
        delete remoteStreams[streamId];
        if (streamId == mainStreamId) {
            var streamIds = Object.keys(remoteStreams);
            var randomId = streamIds[Math.floor(Math.random() * streamIds.length)];
            remoteStreams[randomId].stop(); 
            var remoteContainerID = '#' + randomId + '_container';
            $(remoteContainerID).empty().remove();
            remoteStreams[randomId].play('full-screen-video'); 
            mainStreamId = randomId;
        } else {
            var remoteContainerID = '#' + streamId + '_container';
            $(remoteContainerID).empty().remove(); 
        }
    }
});

client.on("mute-audio", function (evt) {
    toggleVisibility('#' + evt.uid + '_mute', true);
});

client.on("unmute-audio", function (evt) {
    toggleVisibility('#' + evt.uid + '_mute', false);
});

client.on("mute-video", function (evt) {
    var remoteId = evt.uid;
    if (remoteId != mainStreamId) {
        toggleVisibility('#' + remoteId + '_no-video', true);
    }
});

client.on("unmute-video", function (evt) {
    toggleVisibility('#' + evt.uid + '_no-video', false);
});

function joinChannel(channelName, token, userID) {
    client.join(token, channelName, userID, function (uid) {
        console.log("User " + uid + " join channel successfully");
        createCameraStream(uid);
        localStreams.camera.id = uid; 
    }, function (err) {
        console.log("[ERROR] : join channel failed", err);
    });
}

function createCameraStream(uid) {
    var localStream = AgoraRTC.createStream({
        streamID: uid,
        audio: true,
        video: true,
        screen: false
    });
    localStream.setVideoProfile(cameraVideoProfile);
    localStream.init(function () {
        console.log("getUserMedia successfully");
        localStream.play('local-video'); 

        client.publish(localStream, function (err) {
            console.log("[ERROR] : publish local stream error: " + err);
        });

        enableUiControls(localStream);
        localStreams.camera.stream = localStream;
    }, function (err) {
        console.log("[ERROR] : getUserMedia failed", err);
    });
}

function leaveChannel() {

    if (screenShareActive) {
        stopScreenShare();
    }

    client.leave(function () {
        console.log("client leaves channel");
        localStreams.camera.stream.stop() 
        client.unpublish(localStreams.camera.stream); 
        localStreams.camera.stream.close();
        $("#remote-streams").empty() 
        $("#mic-btn").prop("disabled", true);
        $("#video-btn").prop("disabled", true);
        $("#screen-share-btn").prop("disabled", true);
        $("#exit-btn").prop("disabled", true);
        toggleVisibility("#mute-overlay", false);
        toggleVisibility("#no-local-video", false);
        $("#modalForm").modal("show");
    }, function (err) {
        console.log("client leave failed ", err);
    });
}