import logging, datetime
from typing import List
import azure.functions as func

timestamp = datetime.datetime.utcnow()

#def main(events: List[func.EventHubEvent]):
#    for event in events:

def main(event: func.EventHubEvent):
    logging.info(f"{timestamp}: Python EventHub trigger processed an event: {event.get_body().decode('utf-8')}")
