const messages = document.getElementById('messages');
const sendButton = document.getElementById('send');
const messageInput = document.getElementById('message');
sendButton.addEventListener('click', sendMessage);

let socket = new WebSocket("ws://localhost:8000/ws");
init_socket(socket);

function sendMessage() {
    if (!messageInput.value) {
        alert('Message cannot be empty');
        return
    }
    const message = messageInput.value;
    messageInput.value = '';
    addMessage(message, 'user');
    socket.send(message);
}

const userClassLists = {
    container: 'd-flex flex-row justify-content-end mb-4'.split(' '),
    mes: 'small p-2 me-3 mb-1 text-white rounded-3 bg-primary'.split(' '),
    time: 'small me-3 mb-3 rounded-3 text-muted d-flex justify-content-end'.split(' '),
    img: 'avatar.jpg'
}

const botClassLists = {
    container: 'd-flex flex-row justify-content-start mb-4'.split(' '),
    mes: 'small p-2 ms-3 mb-1 rounded-3 bg-body-tertiary'.split(' '),
    time: 'small ms-3 mb-3 rounded-3 text-muted'.split(' '),
    img: 'avatar2.png'
}



function addMessage(message, sender) {
    let cl;
    if (sender == 'user') {cl = userClassLists;}
    else {cl = botClassLists;}
    const container = document.createElement('div');
    container.classList.add(...cl.container);

    const inner = document.createElement('div');

    const mes = document.createElement('p');
    mes.classList.add(...cl.mes);
    mes.textContent = message;

    const time = document.createElement('p');
    time.classList.add(...cl.time);
    const now = new Date();
    time.textContent = now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0');
    const img = document.createElement('img');
    img.src = '/' + cl.img;
    img.style = 'width: 40px; height: 40px;';


    inner.appendChild(mes);
    inner.appendChild(time);
    if (sender == 'user') {

        container.appendChild(inner);
        container.appendChild(img);

    } else {

        container.appendChild(img);
        container.appendChild(inner);
    }
    messages.appendChild(container);
}


function init_socket(socket) {
    socket.addEventListener("open", (event) => {
      console.log('Соединение установлено');

    });

    socket.addEventListener("message", (event) => {
          addMessage(event.data, 'bot');
     });

    socket.addEventListener("close", (event) => {
      console.log("Connection closed");
    });
}



