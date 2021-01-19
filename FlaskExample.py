from flask import Flask
app = Flask(__name__)

dict = {
  "1": "Monday",
  "2": "Tuesday",
  "3": "Wednesday"
}

@app.route("/predictDay/<date>")
def predictDay(date):
    return dict[date]

if __name__ == "__main__":
    app.run()