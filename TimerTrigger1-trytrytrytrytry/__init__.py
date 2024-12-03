import datetime
import logging
import pytz  # You need to install the pytz library

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    # Define the Berlin timezone
    berlin_tz = pytz.timezone('Europe/Berlin')

    # Get the current UTC time and convert it to Berlin time
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc)
    berlin_timestamp = utc_timestamp.astimezone(berlin_tz).isoformat()

    logging.info('WWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!! Python timer trigger function ran at %s (Berlin time)', berlin_timestamp)
