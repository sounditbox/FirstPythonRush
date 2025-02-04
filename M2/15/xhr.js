let urlInput = document.getElementById("address");
let getBtn = document.getElementById("getBtn");
let postBtn = document.getElementById("postBtn");


function sendRequest(method, data) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.open(method, urlInput.value);
        if (method === "POST") {
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.body = JSON.stringify(data);
        }

        xhr.addEventListener("load", () => resolve(JSON.parse(xhr.responseText)));
        xhr.send();
        })
}

getBtn.addEventListener("click", () => {
    sendRequest("GET")
    .then(response => console.log(response));
});
postBtn.addEventListener("click", () => {
    sendRequest("POST",
    {
        name: "morpheus",
        job: "leader"
   })
   .then(response => console.log(response));

});