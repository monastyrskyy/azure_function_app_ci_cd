import datetime
import logging
import pytz
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    # Define the Berlin timezone
    berlin_tz = pytz.timezone('Europe/Berlin')

    # Get the current UTC time and convert it to Berlin time
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    berlin_timestamp = utc_timestamp.astimezone(berlin_tz).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info(f'WWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!! Python timer trigger function ran at {berlin_timestamp} (Berlin time)')
