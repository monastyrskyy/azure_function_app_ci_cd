import logging
import azure.functions as func
import datetime as dt

app = func.FunctionApp()

@app.timer_trigger(schedule="* * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info(f'Speed!!!!!!! Python timer trigger function executed, at this time: {dt.datetime.now()}')