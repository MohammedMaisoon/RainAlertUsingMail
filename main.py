import requests
import smtplib
api_key =YOUR API KEY
my_email = YOUR EMAIL
my_password = YOUR PASSWORD
parameters = {
    "lat":YOUR LATITUDE,
    "lon":YOUR LONGITUDE,
    "appid":api_key,
    "cnt":4,
}
end_point = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
end_point.raise_for_status()
data = end_point.json()


will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=YOUR EMAIL,msg="Subject:Weather Report\n\nBring an Umbrella.")
    print("Bring an Umbrella.")




