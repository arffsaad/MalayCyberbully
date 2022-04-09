function tfSock() {

    if ("WebSocket" in window) {
        var ws = new WebSocket("ws://localhost:9998/tensor");
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
            if (evt.data == 'gaduh' or evt.data == 'buli') {
                $('#cybPrompt').modal()
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
