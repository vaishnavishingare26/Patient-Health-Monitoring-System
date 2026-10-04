import pywhatkit as pwk
import datetime

def sendInfoWA(patient_name, doctor_name, doctor_num, temperature):

    # ✅ Bibwewadi Coordinates (Corrected)
    lat = "18.4635"
    longi = "73.8682"

    # ✅ Correct Google Maps URL
    urlstr = "https://www.google.com/maps?q=" + lat + "," + longi

    # ✅ Alert Message
    message = "🚨 ALERT ALERT ALERT !!!\n"
    message += "Dear Doctor,\n"
    message += doctor_name + "\n\n"
    message += "Your patient " + patient_name
    message += " under home surveillance shows CRITICAL condition.\n"
    message += temperature + "\n\n"
    message += "Please take immediate action.\n"
    message += "📍 Patient Location:\n" + urlstr + "\n\n"
    message += "🩺 Automatic Health Monitoring System"

    # ✅ Mobile number format
    mobilenumber = "+91" + doctor_num

    # ✅ Correct Image Path
    reference_image_path = "Captured_Images/Temp.jpg"

    # ✅ Send WhatsApp Image
    pwk.sendwhats_image(
        mobilenumber,
        reference_image_path,
        message
    )