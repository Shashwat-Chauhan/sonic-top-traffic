class TrafficCalculator:
    @staticmethod
    def calculate_rate(prev, curr, interval):
        rates = {}

        for iface in curr:
            if iface in prev:
                rx_delta = curr[iface]["rx_bytes"] - prev[iface]["rx_bytes"]
                tx_delta = curr[iface]["tx_bytes"] - prev[iface]["tx_bytes"]

                rx_mbps = (rx_delta * 8) / (interval * 1e6)
                tx_mbps = (tx_delta * 8) / (interval * 1e6)

                rates[iface] = {
                    "rx": rx_mbps,
                    "tx": tx_mbps,
                    "total": rx_mbps + tx_mbps
                }

        return rates