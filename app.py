try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

import os
import beeline
import database
from flask import Flask
from flask_healthz import healthz, HealthError
from beeline.middleware.flask import HoneyMiddleware

app = Flask(__name__)
HoneyMiddleware(app, db_events=True)
app.register_blueprint(healthz, url_prefix="/healthz")


def liveness():
    pass


def readiness():
    try:
        database.connect()
    except Exception:
        raise HealthError("Can't connect to the database")


app.config["HEALTHZ"] = {"live": liveness, "ready": readiness}


@app.route("/")
def root():
    return "OK"
