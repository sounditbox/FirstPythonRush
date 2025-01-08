let colors = ["red", "blue", "green", "black"];
let c = 0;
console.log('Привет, мир!');
console.log('Это сообщение будет выведено в консоль браузера.');



function changeColor() {
    let btn = document.getElementById("text");
    btn.style.color = colors[c % colors.length];
    c++;
}