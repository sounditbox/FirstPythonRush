// Обновление содержимого параграфа
const paragraph = document.querySelector('p'); // Выбор первого параграфа
paragraph.textContent = 'Новый текст параграфа'; // Замена текста параграфа
// Создание нового элемента и добавление его на страницу
const newDiv = document.createElement('div'); // Создание нового div элемента
newDiv.className = 'new-class'; // Добавление класса к новому div элементу
newDiv.textContent = 'Это новый элемент'; // Добавление текста
document.body.appendChild(newDiv); // Добавление div к body

const h1 = document.getElementById('MyHeader');
h1.style.color = 'red';

