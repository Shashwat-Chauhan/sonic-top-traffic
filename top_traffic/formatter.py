import json

def format_table(data):
    print(f"{'Interface':<12}{'RX(Mbps)':<12}{'TX(Mbps)':<12}{'Total(Mbps)':<12}")
    print("-" * 50)

    for iface, stats in data.items():
        print(f"{iface:<12}{stats['rx']:<12.2f}{stats['tx']:<12.2f}{stats['total']:<12.2f}")


def format_json(data):
    print(json.dumps(data, indent=4))