const socket = io('ws://192.168.0.27:4321');
socket.emit('name', 'test');
socket.on('message', text => {
    const el = document.createElement('li');
    el.innerHTML = text;
    document.querySelector('ul').appendChild(el);
});

function send_message() {
    const text = document.getElementById('message').value;
    socket.emit('message', text);
}

function send_name() {
    const text = document.getElementById('name').value;
    socket.emit('name', text);
    document.getElementById('sendname').style.display = 'none';
    document.getElementById('name').style.display = 'none';
}


document.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        const text = document.getElementById('message').value;
    	socket.emit('message', text);
    }
});
