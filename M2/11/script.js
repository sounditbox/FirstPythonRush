let i = 0;
let colors = ["red", "blue", "green", "black"];
// Получаем элемент и задаем обработчик через свойство onclick
const button = document.getElementById('myButton');
button.addEventListener('click', function(event) {
    console.log(event);
    document.body.style.backgroundColor = colors[i % colors.length];
    i++;
});