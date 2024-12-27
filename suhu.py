temp_type = ""
moisture_type = "Moist"

if temp_type == "Cold":
    if moisture_type == "Dry":
        print("Penyiraman 15 menit")
    elif moisture_type == "Moist":
        print("Penyiraman 10 menit")
    elif moisture_type == "Wet":
        print("Penyiraman 5 menit")
    else:
        print("Perangkat Error")
elif temp_type == "Normal":
    if moisture_type == "Dry":
        print("Penyiraman 15 menit")
    elif moisture_type == "Moist":
        print("Penyiraman 10 menit")
    elif moisture_type == "Wet":
        print("Penyirmana 5 menit")
    else:
        print("Perangkat Error")
elif temp_type == "Hot":
    if moisture_type == "Dry":
        print("Penyiraman 15 menit")
    elif moisture_type == "Moist":
        print("Penyiraman 10 menit")
    elif moisture_type == "Wet":
        print("Penyirman 5 menit")
    else:
        print("Perangkat Error")
else:
    print("perangkat Error")
