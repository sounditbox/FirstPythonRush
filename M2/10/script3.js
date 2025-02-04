function showImage() {
    const image = document.createElement('img');
    image.setAttribute('src', 'image.jpg');
    image.setAttribute('alt','Описание изображения');
    image.width = 720;
    image.height = 480;
    document.body.appendChild(image);
}