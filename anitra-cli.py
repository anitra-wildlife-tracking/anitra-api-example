import os
import click
import click_spinner
import time
import csv 
from api.api import AnitraApi
from formatter.csvformatter import CSVFormatter
from formatter.xlsxformatter import XLSXFormatter
import os, psutil
import time
import datetime as dt

pass_anitra = click.make_pass_decorator(AnitraApi, ensure=True)

@click.group()
@click.option('--clientid', envvar='ANITRA_API_USER', required=True, help = 'Your Anitra API client ID')
@click.option('--clientkey', envvar='ANITRA_API_PASSWORD', required=True, help = 'Your Anitra API client key')
@click.option('--apiurl', envvar='ANITRA_API_URL', required=True, help = 'Anitra API url', default = 'https://app.anitra.cz/api/v2/')
@click.pass_context
def cli(ctx, clientid, clientkey, apiurl):
    ctx.obj = AnitraApi(clientid, clientkey, apiurl, False)

@cli.command()
@click.option("--format", '--f', multiple=False, default=["csv"], type=click.Choice(['csv', 'xlsx']), help='Output format')
@click.option('--output', '--o', required=True, type=click.Path(exists=False), help = 'Output file, if none is specified the tool will print to console')
@pass_anitra
def device_list(anitra, format, output):
    with click_spinner.spinner():
        click.secho('Exporting device list...', fg='green')
        res = anitra.get_devices()
        click.secho('Formatting device list...', fg='green')

        if (format == 'csv'):
            formatter = CSVFormatter(output)
            formatter.writeJSON(res)

        if (format == 'xlsx'):
            formatter = XLSXFormatter(output)
            formatter.writeJSON(res)

    click.secho('Exporting complete!', fg='green')

    pass

@cli.command()
@click.option("--format", '--f', multiple=False, default=["csv"], type=click.Choice(['csv', 'xlsx']), help='Output format')
@click.option('--output', '--o', required=True, type=click.Path(exists=False), help = 'Output file, if none is specified the tool will print to console')
@click.argument('device', type=int, required = True)
@click.option('--date_from', '--from', type=click.STRING, help = 'Date from in ISO8601 short format (no spaces) with millisecond precision')
@click.option('--date_to', '--to', type=click.STRING, help = 'Date to in ISO8601 short format (no spaces) with millisecond precision')
@pass_anitra
def device_data(anitra, format, output, device, date_from = None, date_to = None):
    start_time = time.time()

    with click_spinner.spinner():
        click.secho('Exporting device data...', fg='green')
        res = anitra.get_devicedata(device, date_from, date_to, None, None)
        click.secho('Formatting device data...', fg='green')

        if (format == 'csv'):
            formatter = CSVFormatter(output)
            formatter.writeScroll(res)
        
        if (format == 'xlsx'):
            formatter = XLSXFormatter(output)
            formatter.writeScroll(res)

    click.secho('Exporting complete!', fg='green')

    pass

if __name__ == '__main__':
    cli()