
from flask import Flask


app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    return (f"Percipitation <br/>"
    f"Stations <br/>"
    f"tobs <br/>"
    f"Start <br/>"
    f"Start/end<br/>")
    
     

#@app.route("/api/v1.0/precipitation")
#def precipitation():


#@app.route("/api/v1.0/stations")
#def stations():

#@app.route("/api/v1.0/tobs")
#def tobs():


if __name__ == "__main__":
    app.run(debug=True)
