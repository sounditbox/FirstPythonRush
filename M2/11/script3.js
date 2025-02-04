document.getElementById('parent').addEventListener('click', function() {
    console.log('Parent clicked');
});
document.getElementById('child').addEventListener('click', function(event) {
    console.log('Child clicked');
});