const http = require('http').createServer();

const io = require('socket.io')(http, {
	cors: { origin: "*" }
});
var dict = {};
var dict2 = {};
io.on('connection', (socket) => {
	console.log(`a user connected: ${socket.id}`);
	socket.on('name', (name) => {
		if (name.split(":")[0]=="01272004"){
			if (name.split(":")[1]==name.split(":")[2]){
				console.log(`"${name.split(":")[1]}" disconnected.`);
				socket.broadcast.emit('message', `MOD: ${dict[name.split(":")[0].slice(0,-2)]} has left the chat!`);
			} else {
				dict[name.split(":")[1].slice(0,-2)] = name.split(":")[2];
				io.to(socket.id).emit('message', `MOD: Hello ${name}`);
				console.log(dict);
			}
		} else {
			io.to(socket.id).emit('name', "error 314.");
		}
	});

	socket.on('name2', (name2) => {
		dict2[socket.id] = dict[name2];
		socket.broadcast.emit('message', `MOD: ${dict2[socket.id]} has entered the chat room!`);
		io.to(socket.id).emit('message', `MOD: Hello ${dict2[socket.id]}.`);
	});

	socket.on('message', (message) => {
		console.log(`${socket.id}: ${message}`);
		socket.broadcast.emit('message', `${dict2[socket.id]}: ${message}`);
		//socket.emit('message', `${dict2[socket.id]}: ${message}`);
		io.to(socket.id).emit('message', `Me: ${message}`);
	});

	socket.on('admin', (admin) => {
		io.emit('message', `Admin: ${admin}`);
	});
});

http.listen(8880, () => console.log('listening on 192.168.0.27:8880'));
