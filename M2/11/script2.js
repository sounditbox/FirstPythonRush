// Использование capture для триггера событие сначала на parent
document.getElementById('parent').addEventListener('click', function(event) {
    console.log('Parent capture');
    event.stopPropagation();
    }, true);
document.getElementById('child').addEventListener('click', function() {
    console.log('Child capture');}, true);