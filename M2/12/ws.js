const messages = document.getElementById('messages');
const chat = document.getElementById('chat');
messages.style.display = 'none';
let username;
const sendButton = document.getElementById('send');
const messageInput = document.getElementById('message');
sendButton.addEventListener('click', initChat);
let socket = new WebSocket("ws://localhost:80");
init_socket(socket);
let exitBtn = document.createElement('input');
exitBtn.type = 'button';
exitBtn.value = 'Exit';
exitBtn.addEventListener('click', () => {
      socket.send(JSON.stringify({type: 'exit', username: username}));
      location.reload();
});

exitBtn.style = 'display: none';

function initChat() {
    if (messageInput.value == '') {
        alert('Please enter your name');
        return;
    }
    exitBtn.style = 'display: block';
    username = messageInput.value;
    messageInput.value = '';
    sendButton.value = 'Send';
    messageInput.placeholder = 'Enter your message...';
    messages.style = 'display: block';
    sendButton.removeEventListener('click', initChat);
    sendButton.addEventListener('click', sendMessage);
    socket.send(JSON.stringify({type: 'join', username: username}));
    chat.appendChild(exitBtn);
}

function sendMessage() {
    if (!messageInput.value) {
        alert('Message cannot be empty');
        return
    }
    const message = messageInput.value;
    messageInput.value = '';
    socket.send(JSON.stringify({type: 'message', message: message, username: username}));
}

function addMessage(message) {
    const li = document.createElement('li');
    li.textContent = message;
    messages.appendChild(li);
}


function init_socket(socket) {
    socket.addEventListener("open", (event) => {
      console.log('Соединение установлено');

    });

    socket.addEventListener("message", (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'message') {
          addMessage(data.message);
      }
      else if (data.type === 'join') {
          addMessage(`${data.username} joined the chat`);
          data.messages.forEach((message) => {
              addMessage(message);
          });
      }
      else if (data.type === 'exit') {
          addMessage(`${data.username} left the chat`);
      }
     });
    socket.addEventListener("close", (event) => {
      console.log("Connection closed");
    });
}



