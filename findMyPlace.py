import webbrowser
def myplace(city):
    g_url = f"https://earth.google.com/web/search/{city}"
    webbrowser.open(g_url)
cityName= input("Enter your city name: ")
myplace(cityName)