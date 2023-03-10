from signal_outputter import SignalOutputter
from logger import Logger
from paho.mqtt.publish import single
from datetime import datetime, timezone, timedelta
from socket import gethostname
import time
import json

logger = Logger("test.log")
tz_taipei = timezone(timedelta(hours=8))

hostname = gethostname()

def output_callback(sensor_name: str):
    logger.debug("output")
    broker_host = 'twn-pdb.sram.com'
    prod_line = 'Shifter/1'

    topic = 'event/Shifter/1'
    payload = {"event":"product_output"}
    single(topic, payload=json.dumps(payload), hostname=broker_host)

driver_pin = 19
opt_pin = 26


SignalOutputter(26, 3, lambda: output_callback("opt_sensor")).listen()

while (True):
    time.sleep(1)
