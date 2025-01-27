// Создаем новый div элемент
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello, I am a new div!'; // Устанавливаем текстовое содержимое
//newDiv.className = 'new-div'; // Задаем класс для нового элемента
// document.body.appendChild(newDiv); // Добавление div к body

// Допустим, у нас есть существующий элемент с id "parent"
const parentElement = document.getElementById('parent');
// Вставляем новый элемент в конец родителя
//parentElement.appendChild(newDiv);
// Вставляем новый элемент в начало родителя
//parentElement.prepend(newDiv);
// Вставляем новый элемент перед referenceElement
parentElement.insertBefore(newDiv, document.getElementById('reference'));