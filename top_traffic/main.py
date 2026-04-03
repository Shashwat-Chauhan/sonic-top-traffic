import time
from .counter_reader import CounterReader
from .traffic_calculator import TrafficCalculator


class TopTraffic:
    def __init__(self, interval=5, top_n=5):
        self.interval = interval
        self.top_n = top_n
        self.reader = CounterReader()

    def get_top_interfaces(self):
        prev = self.reader.get_interface_counters()
        time.sleep(self.interval)
        curr = self.reader.get_interface_counters()

        rates = TrafficCalculator.calculate_rate(prev, curr, self.interval)

        sorted_ifaces = sorted(
            rates.items(),
            key=lambda x: x[1]["total"],
            reverse=True
        )

        return dict(sorted_ifaces[:self.top_n])
