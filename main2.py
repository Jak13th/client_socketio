import socketio
import asyncio
import requests

sio_client = socketio.AsyncClient(logger=True, engineio_logger=True)

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aWJvQGdnLmNvbSIsImV4cCI6MTcwMDkwNzI1Nn0.odlL0DyumCiXT4TucoUptJuXowXFqtxMIINdUER-ETY"

@sio_client.event
async def connect():
    print('Im connected')

@sio_client.event
async def disconnect():
    print('Im disconnected')

@sio_client.event
def message(data):
    print('I received a message!')
    print(data)

async def main():
    await sio_client.connect(url='http://localhost:8000', auth={'token': token}, transports=['websocket'])
    
    await sio_client.wait()
    # print("next")
    # data = await sio_client.receive()
    # await sio_client.emit('on_message', {'foo': 'bar'})
    # print("DATA : ", data)
    
    

asyncio.run(main())