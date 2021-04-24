import asyncio
import websockets
import time
import json

uri = "wss://api.upbit.com/websocket/v1"

async def assignment():
    count = 0
    query = '[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW-BTC"]}, {"type":"orderbook","codes":["KRW-BTC"]}]'
    async with websockets.connect(uri) as websocket:
        while count != 10: # to pass only 10 responses
            await websocket.send(query)

            answer = await websocket.recv()
            answer = answer.decode("ascii")
            answer = json.loads(answer)

            if answer["type"] == "trade":
                print("trade_price:"+str(answer["trade_price"])+
                      "\t trade_volume:"+str(answer["trade_volume"])+
                      "\t ask_bid:"+answer["ask_bid"])
            elif answer["type"] == "orderbook":
                print("ask_price:"+str(answer["orderbook_units"][0]["ask_price"])+
                      "\t bid_price:"+str(answer["orderbook_units"][0]["bid_price"])+
                      "\t ask_size:"+str(answer["orderbook_units"][0]["ask_size"])+
                      "\t bid_size:"+str(answer["orderbook_units"][0]["bid_size"]))
            else:
                pass
            
            count += 1    
            time.sleep(60) # to see the difference
            
asyncio.get_event_loop().run_until_complete(assignment())
