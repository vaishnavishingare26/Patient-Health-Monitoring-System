import requests
import time
import LiveImageCapturter
import WhatsAppSender
from pygame import mixer
import threading


def playvoice():
    mixer.init()
    mixer.music.load("medical alert.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)


def read_thingspeak_data(patient_name, doctor_name, doctor_num):

    heart_rate_threshold = 1000
    temperature_threshold = 80.0
    iteration = 2

    heart_rate_count = 0
    temperature_count = 0
    alert_active = False

    channel_id = '3272990'
    read_key = '2CV6JC0ZSYRG4JE1'

    while True:

        print("\n📡 Monitoring running...")

        url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_key}&results=1'

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:

                data = response.json()

                if 'feeds' in data and len(data['feeds']) > 0:

                    latest_entry = data['feeds'][0]

                    temperature = latest_entry.get('field1')
                    heart_rate = latest_entry.get('field2')

                    if heart_rate and temperature:

                        try:
                            heart_rate_value = float(heart_rate)
                            temperature_value = float(temperature)

                            temperature_value = (temperature_value * 9 / 5) + 32

                            print(f"❤️ Pulse Value: {heart_rate_value}")
                            print(f"🌡 Temperature: {temperature_value:.2f} °F")

                            if heart_rate_value == 0 or heart_rate_value > 4000:
                                print("⚠ Invalid Pulse Skipped")
                                continue

                            if heart_rate_value >= heart_rate_threshold:
                                heart_rate_count += 1
                            else:
                                heart_rate_count = 0

                            if temperature_value >= temperature_threshold:
                                temperature_count += 1
                                print("🚨 High Temperature Detected!")
                            else:
                                temperature_count = 0

                            if (heart_rate_count >= iteration or temperature_count >= iteration) and not alert_active:

                                alert_active = True
                                print("\n🚨 EMERGENCY ALERT TRIGGERED!")

                                captured_image = LiveImageCapturter.getLiveImage()

                                if captured_image == 1:
                                    print("📸 Patient Image Captured")

                                    t1 = threading.Thread(target=playvoice)
                                    t1.start()

                                    WhatsAppSender.sendInfoWA(
                                        patient_name,
                                        doctor_name,
                                        doctor_num,
                                        f"Pulse: {heart_rate_value}\nTemp: {temperature_value:.2f} °F"
                                    )

                                    print("✅ Alert sent successfully.")

                                heart_rate_count = 0
                                temperature_count = 0

                                print("⏳ Cooling down...\n")
                                time.sleep(20)

                                alert_active = False

                        except ValueError:
                            print("⚠ Invalid numeric data.")

                    else:
                        print("⚠ Missing data.")

                else:
                    print("⚠ No feeds found.")

            else:
                print(f"⚠ ThingSpeak Error: {response.status_code}")

        except requests.exceptions.RequestException:
            print("⚠ Network issue.")

        time.sleep(5)