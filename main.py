import asyncio
from datetime import datetime
from time import sleep

from Components import ContextPrinter, Database
from Drivers import *
from mission_modes import *

# Time in seconds to sleep before initializing drivers
SLEEP_DURATION = 1#30 * 60

# TODO: initialize database
# TODO: Query database for initial time
db = Database()
initial_time = None

if initial_time is None:
    initial_time = datetime.now()
    # TODO: Record initial boot time in database

delta = datetime.now() - initial_time
if delta.seconds < SLEEP_DURATION:
    sleep(SLEEP_DURATION - delta.seconds)


async def startLoop():
    context = {"MissionMode": MissionMode.PRE_TX}
    lock = asyncio.Lock()
    drivers = [ContextPrinter()]
    await asyncio.gather(*[d.run(context, lock) for d in drivers])


try:
    asyncio.run(startLoop())
except KeyboardInterrupt:
    pass
