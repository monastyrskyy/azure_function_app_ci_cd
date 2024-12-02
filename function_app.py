import logging
import azure.functions as func
import datetime as dt
import pytz  # For timezone handling

# Define Berlin timezone
BERLIN_TZ = pytz.timezone("Europe/Berlin")

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    # Get the current UTC time and convert it to Berlin time
    berlin_time = dt.datetime.now(pytz.utc).astimezone(BERLIN_TZ)
    logging.info(f'Python timer trigger function executed, at this time: {berlin_time}') 