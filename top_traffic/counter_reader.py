import time
import redis

COUNTERS_DB = 2

class CounterReader:
    def __init__(self, host="localhost", port=6379):
        self.db = redis.Redis(host=host, port=port, db=COUNTERS_DB)

    def get_interface_counters(self):
        keys = self.db.keys("COUNTERS:Ethernet*")
        counters = {}

        for key in keys:
            iface = key.decode().split(":")[1]
            data = self.db.hgetall(key)

            counters[iface] = {
                "rx_bytes": int(data.get(b"SAI_PORT_STAT_IF_IN_OCTETS", 0)),
                "tx_bytes": int(data.get(b"SAI_PORT_STAT_IF_OUT_OCTETS", 0)),
            }

        return counters