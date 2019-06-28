feels_like = 0
extra_clothes = []
string_clothes = "You should wear"

def get_temp(user_temp):
    global feels_like
    feels_like = int(user_temp)
    return feels_like
    
def get_humidity(user_humidity):
    global feels_like
    if user_humidity == "yes":
        global feels_like
        feels_like += 5
        return feels_like
    elif user_humidity == "no":
        return feels_like

def get_wind(user_wind):
    global feels_like
    if user_wind == "no_wind":
        return feels_like
    elif user_wind == "light_wind":
        feels_like -= 5
        return feels_like
    elif user_wind == "heavy_wind":
        feels_like -= 10
        return feels_like
        
def get_intensity(user_intensity):
    global feels_like
    if user_intensity == "easy_run":
        return feels_like
    elif user_intensity == "long_run":
        feels_like += 5
        return feels_like
    elif user_intensity == "hard_workout" or user_intensity == "race":
        feels_like += 10
        return feels_like
    
    
def total_temp(user_temp, user_humidity, user_wind, user_intensity):
    global feels_like
    get_temp(user_temp)
    get_humidity(user_humidity)
    get_wind(user_wind)
    get_intensity(user_intensity)
    # get_conditions(user_condition)
    return feels_like
    
def get_conditions(user_condition):
    global feels_like
    global extra_clothes
    if user_condition == "clear":
        extra_clothes = []
        extra_clothes.append("sunscreen")
        return extra_clothes
    elif user_condition == "rain":
        extra_clothes = []
        extra_clothes.append("a rain jacket")
        return extra_clothes
    elif user_condition == "snow":
        extra_clothes = []
        extra_clothes.append("be careful!")
        return extra_clothes
        
    
def determine_clothes():
    global feels_like
    global string_clothes
    string_clothes = "You should wear"
    clothes = ["a sports bra", "sneakers", "socks"]
    freezing_clothes = ["insulated spandex", "an insulated long sleeved top", "a headband", "gloves"]
    cold_clothes = ["long spandex", "an insulated long sleeved top"]
    medium_clothes = ["long spandex", "a long sleeve shirt"]
    warm_clothes = ["long spandex", "a short sleeve shirt"]
    warmer_clothes = ["spandex shorts", "a short sleeve shirt"]
    hot_clothes = ["spandex shorts", "a tank top"]
    if feels_like < 20: 
        clothes = clothes + freezing_clothes 
        # print .join(clothes))
        num_clothes = len(clothes)
        # print(num_clothes)
    # I have removed extra clothes from each of the lists of clothes because I currently don't have the conditions working.
    elif feels_like < 30: 
        clothes = clothes + cold_clothes
        # print(clothes)
    elif feels_like < 45: 
        clothes = clothes + medium_clothes 
        # print(clothes)
    elif feels_like < 60: 
        clothes = clothes + warm_clothes 
        # print(clothes)
    elif feels_like < 70:
        clothes = clothes + warmer_clothes 
        # print(clothes)
    else: 
        clothes = clothes + hot_clothes 
        # print(clothes)
    for x in range(len(clothes)):
        if x < len(clothes) - 1:
            string_item = " " + clothes[x] + ","
            string_clothes += string_item
        else: 
            string_item = " and " + clothes[x] + "."
            string_clothes += string_item
    print(string_clothes)
    return(string_clothes)
    
def what_to_wear(user_temp, user_humidity, user_wind, user_intensity):
    total_temp(user_temp, user_humidity, user_wind, user_intensity)
    determine_clothes()
    return string_clothes
