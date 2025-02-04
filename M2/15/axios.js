// const axios = require('axios');

let urlInput = document.getElementById("address");
let getBtn = document.getElementById("getBtn");
let postBtn = document.getElementById("postBtn");


function sendRequest(method, data) {
    if (method === "GET") {
        return axios.get(urlInput.value);
    } else {
        return axios.post(urlInput.value, data)
        .then(response => response.data)
        .catch(error => error.response.data);
    }
}


getBtn.addEventListener("click", () => {
    sendRequest("GET")
    .then(response => console.log(response))
    .catch(error => console.log(error));
});
postBtn.addEventListener("click", () => {
    sendRequest("POST", {
        email: "eve.holt@reqres.in",
        password: "pistol"
    })
    .then(response => console.log(response));
});