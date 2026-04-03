import click
from top_traffic.main import TopTraffic
from top_traffic.formatter import format_table, format_json


@click.command()
@click.option('--interval', default=5, help='Sampling interval in seconds')
@click.option('--top', default=5, help='Top N interfaces')
@click.option('--json', 'json_output', is_flag=True, help='JSON output')
def show_top_traffic(interval, top, json_output):
    """
    Show top N interfaces by traffic
    """

    tt = TopTraffic(interval=interval, top_n=top)
    data = tt.get_top_interfaces()

    if json_output:
        format_json(data)
    else:
        format_table(data)