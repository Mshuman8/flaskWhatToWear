from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("/index.html")
    

@app.route('/sendWeather', methods = ["GET", "POST"])
def sendWeather():
    if request.method == "POST":
        user_data = formopener.dict_from(request.form)
        print(user_data)
        user_intensity = user_data["intensity"]
        user_temp = user_data["temperature"]
        user_wind = user_data["wind"]
        user_humidity = user_data["humidity"]
        # For some reason it isn't finding the condition.  I commented it out of the html form so that it would run. It wasn't even printing the results of whatever was typed. 
        # user_condition = user_data["conditions"]
        the_clothes = model.what_to_wear(user_temp, user_humidity, user_wind, user_humidity)
        return render_template("/results.html", the_clothes = the_clothes)
    else:
        return "Please go back and try again."