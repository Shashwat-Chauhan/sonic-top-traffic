def test_rate_calculation():
    prev = {"Eth0": {"rx_bytes": 1000, "tx_bytes": 2000}}
    curr = {"Eth0": {"rx_bytes": 3000, "tx_bytes": 4000}}

    from top_traffic.traffic_calculator import TrafficCalculator

    rates = TrafficCalculator.calculate_rate(prev, curr, 2)

    assert rates["Eth0"]["total"] > 0