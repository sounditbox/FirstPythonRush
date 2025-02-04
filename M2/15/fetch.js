let urlInput = document.getElementById("address");
let getBtn = document.getElementById("getBtn");
let postBtn = document.getElementById("postBtn");


function sendRequest(method, data) {
        return fetch(urlInput.value, method == "GET" ? {} : {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error(response.statusText));
        });
}

getBtn.addEventListener("click", () => {
    sendRequest("GET")
    .then(response => console.log(response));
});
postBtn.addEventListener("click", () => {
    sendRequest("POST", {
        name: "morpheus",
        job: "leader"
    })
    .then(response => console.log(response));
});