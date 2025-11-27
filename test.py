from ib_async import *
import asyncio

ib = IB()

# Connect to TWS/Gateway
# Change port and clientId as needed. clientId=0 is usually for the main controller.
if not ib.isConnected():
    ib.connect('127.0.0.1', 7497, clientId=1)
    print("Connected!")
else:
    print("Already connected.")