function tfSock() {

    if ("WebSocket" in window) {
        var ws = new WebSocket("ws://acbe-2400-8901-00-f03c-93ff-fee2-9f17.ngrok.io/tensor");
        console.log("WebSocket connected!");

        ws.onopen = function() {
            var x = document.getElementById("textInput").value
            ws.send(x);
            document.getElementById("alertText").textContent = x;
            console.log("Message is sent...");
        };
        ws.onmessage = function(evt) {
            var received_msg = evt.data;
            console.log(evt.data)
            if (evt.data == 'gaduh' || evt.data == 'buli') {
                var cybmodal = new bootstrap.Modal(document.getElementById('cybPrompt'));
                cybmodal.toggle();
            } else {
                if (evt.data == 'empty'){
                    var notModal = new bootstrap.Modal(document.getElementById('nothingposted'));
                    notModal.toggle();
                }
                else{
                document.getElementById("userPost").action = "/";
                document.getElementById("userPost").submit();
            }
            }
            ws.close()
        };
        ws.onclose = function() {
            console.log("Connection is closed...");
        };

    } else {
        alert("WebSocket NOT supported by your Browser!");
    }
}

function createPost() {
    document.getElementById("expl").value = "1";
    document.getElementById("userPost").action = "/";
    document.getElementById("userPost").submit();
}

function unblur(postId) {
    document.getElementById(postId).style = "";
    var button = "expbutton" + postId;
    document.getElementById(button).style = "display:none";
}
