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

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Measurement.station).group_by(Measurement.station)
    session.close()
    stat_lis=[]
    for station in stations:
        stat_lis.append(station)
    return jsonify(stat_lis)

@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    active=session.query(Measurement.date, Measurement.tobs).filter(Measurement.station=="USC00519281", Measurement.date>="2016-08-18").order_by(Measurement.date.desc())
    session.close()
    temp={}
    for date, tobs in active: 
        temp[date]=tobs
    return jsonify(temp)



if __name__ == "__main__":
    app.run(debug=True)
