import numpy as np
import datetime as dt
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
    return (f"/api/v1.0/precipitation <br/>"
    f"/api/v1.0/stations <br/>"
    f"/api/v1.0/tobs <br/>"
    f"/api/v1.0/start <br/>"
    f"/api/v1.0/start/end <br/>")
    
     

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
@app.route("/api/v1.0/<start>")
def summary_start(start):
    
    session=Session(engine)
    stats=[Measurement.date, func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    summary=session.query(*stats).group_by(Measurement.date).filter(Measurement.date>=start).all()
    session.close()
    sum_stat=list(summary)
    
    return jsonify(sum_stat)
@app.route("/api/v1.0/<start>/<end>")
def ranged_stats(start, end):
    session=Session(engine)
    stats=[Measurement.date, func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    ranged_data=session.query(*stats).group_by(Measurement.date).filter(Measurement.date>=start, Measurement.date<=end).all()
    session.close()
    temp_list=list(ranged_data)
    return jsonify(temp_list)

if __name__ == "__main__":
    app.run(debug=True)
