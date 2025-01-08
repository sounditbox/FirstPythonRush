function changeTheme() {
    let body = document.querySelector("body");
    console.log(body.style);
    body.style.font = "20px times new roman";
    if (body.classList.contains("dark-theme")) {
        body.classList.remove("dark-theme");
    } else {
        body.classList.add("dark-theme");
    }
}
