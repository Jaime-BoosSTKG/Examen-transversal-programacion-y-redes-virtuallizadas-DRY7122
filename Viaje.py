import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "CWEcskfST8Tz8Bbw5AcV0KhVlidjADp9"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "Salir" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "Salir" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})     
    print("URL: " + (url))      
    json_data = requests.get(url).json()     
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Desde " + (orig) + " Hasta " + (dest))
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("Uso de combustible (Ltr): " + str(json_data["route"]["fuelUsed"])*3.78)
        print("=============================================")
        print("************************************************************************")
        print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("************************************************************************\n")