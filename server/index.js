const http = require('http').createServer();

const io = require('socket.io')(http, {
	cors: { origin: "*" }
});
var dict = {};
io.on('connection', (socket) => {
	console.log(`a user connected: ${socket.id}`);
	socket.on('name', (name) => {
		dict[socket.id] = name;
		io.to(socket.id).emit('message', `MOD: Hello ${name}`);
	});

	socket.on('message', (message) => {
		console.log(`${socket.id}: ${message}`);
		io.emit('message', `${dict[socket.id]}: ${message}`);
	});

	socket.on('admin', (admin) => {
		io.emit('message', `Admin: ${admin}`);
	});
});

http.listen(4321, () => console.log('listening on 192.168.0.27:4321'));
