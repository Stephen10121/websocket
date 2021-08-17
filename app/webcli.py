import socketio

sio = socketio.Client()

def send_info(what, key):
	if key=="01272004":
		sio.emit('name', what)
	else:
		return False

@sio.event
def connect():
	print('connection established')

@sio.event
def disconnect():
	print('disconnected from server')

sio.connect('http://192.168.0.27:8880')
