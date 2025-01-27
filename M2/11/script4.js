document.getElementById('parent').addEventListener('click', function() {
    console.log('Parent bubbling phase');
});
document.getElementById('parent').addEventListener('click', function() {
    console.log('Parent capturing phase');
}, true);

document.getElementById('child').addEventListener('click', function(event) {
    console.log('Child bubbling phase');
});
document.getElementById('child').addEventListener('click', function(event) {
    console.log('Child capturing phase');
}, true);

let i = 0;
let colors = ["red", "blue", "green", "black"];
// Получаем элемент и задаем обработчик через свойство onclick
const button = document.getElementById('btn');
button.addEventListener('click', function(event) {
    console.log('target phase');
    document.body.style.backgroundColor = colors[i % colors.length];
    i++;
});