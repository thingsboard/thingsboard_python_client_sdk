import logging
from tb_device_mqtt import TBClient

logging.basicConfig(level=logging.DEBUG)
telemetry = {"temperature": 451}
#telemetry = [{"temp": 1001}, {"kek":"lol"}]
#telemetry = {"ts":1451649600512, "values":{"key1":"222", "key2":"123"}}
#attributes = {"firmwareVersion": "v2.3.2", "temp": 1}

client = TBClient("127.0.0.1", "A1_TEST_TOKEN")
client.connect()
client.send_telemetry(telemetry, 1, blocking=True)
#client.send_attributes(attributes)
client.disconnect()