if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
                const { latitude, longitude } = position.coords;
                let p = document.createElement('p');
                p.textContent = `Your current location: Latitude: ${latitude}, Longitude: ${longitude}`;
                document.body.appendChild(p);
            },
        (error) => { console.error('Error getting geolocation:', error); },
        {
            enableHighAccuracy: true, // Высокая точность
            timeout: 5000, // Таймаут ожидания ответа (мс)
            maximumAge: 0
            // Максимальное время, в течение которого можно использовать кэшированные данные (мс)
        }
    );
    } else {
    console.log('Geolocation is not supported by this browser.');
}