import logging
import os
import beeline


def post_worker_init(worker):
    logging.info(f"beeline initialization in process pid {os.getpid()}")
    debug = os.environ.get("HONEYCOMB_DATASET") == "development"
    beeline.init(
        # Get this via https://ui.honeycomb.io/account after signing up for Honeycomb
        writekey=os.environ.get("HONEYCOMB_API_KEY"),
        dataset=os.environ.get("HONEYCOMB_DATASET"),
        service_name=os.environ.get("SERVICE_NAME"),
        # defaults to False. if True, data doesn't get sent to Honeycomb
        debug=debug,
    )
