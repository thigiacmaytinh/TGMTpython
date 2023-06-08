import asyncio
import time
import websockets
 
# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"Data recieved as:  {data}!"
    while(True):
        await websocket.send(reply)
        await asyncio.sleep(1)
 
 
 
start_server = websockets.serve(handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server) 
asyncio.get_event_loop().run_forever()