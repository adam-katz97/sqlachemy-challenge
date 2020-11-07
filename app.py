import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


app = Flask(__name__)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    return (f"Percipitation <br/>"
    f"Stations <br/>"
    f"tobs <br/>"
    f"Start <br/>"
    f"Start/end<br/>")
    
     

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    weather = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).order_by(Measurement.date.desc()).limit(366)
    session.close()
    
    percip={}
    for date, prcp in weather:
        
        percip[date]=prcp
        


    return jsonify(percip)

#@app.route("/api/v1.0/stations")
#def stations():

#@app.route("/api/v1.0/tobs")
#def tobs():


if __name__ == "__main__":
    app.run(debug=True)
