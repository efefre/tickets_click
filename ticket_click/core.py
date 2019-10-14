import click
import pendulum

from ticket_click.utils import Ticket


@click.command()
@click.option('--start_date', prompt='Kiedy bilet został aktywowany? ', help="Date in format dd-mm-yyyy", default='')
@click.option('--stop_date', prompt='Do kiedy bilet jest ważny? ', help="Date in format dd-mm-yyyy")
@click.option('--cancel_date', prompt='Kiedy chcesz anulować bilet? ', help="Date in format dd-mm-yyyy")
@click.option('--period', default=30, prompt='Na ile dni wykupiłeś bilet (30/90)? ', help="Number: 30 or 90. Default value: 30")
@click.option('--ticket_price',default=0.00, prompt='Ile zapłaciłeś za bilet? ', help="Ticker price: float. Default value: 0.00")
def cli(start_date, stop_date, cancel_date, period, ticket_price):
    """ This is a simple app in which you can count how much money you will receive back,
        if you cancel your ZTM (Warsaw) ticket."""

