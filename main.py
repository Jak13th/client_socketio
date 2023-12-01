import socketio
import asyncio
import requests

sio_client = socketio.AsyncClient(logger=True, engineio_logger=True)

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiZXJ0cmFuZHRoaWJhdXQucHJvQGdtYWlsLmNvbSIsImV4cCI6MTcwMDkyNjU1NH0.pbdVBgklTnL1ibCgFaT9-HI8lrddfBt0nPmSzWea44A"

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
    await sio_client.connect(url='https://app-services-api-soundscribe.azurewebsites.net/socket.io/', auth={'token': token}, transports=['websocket']) 
    # https://app-services-api-soundscribe.azurewebsites.net/socket.io/?EIO=4&transport=websocket
    
    await sio_client.wait()
    # print("next")
    # data = await sio_client.receive()
    # await sio_client.emit('on_message', {'foo': 'bar'})
    # print("DATA : ", data)
    
asyncio.run(main())