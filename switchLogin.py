from requests import Session
from bs4 import BeautifulSoup as bs


with Session() as s:
    baseUrl="http://192.168.0.0"
    password="******"

    site = s.get(baseUrl+"/password.htm")

    login_data = {"password":password}
    s.post(baseUrl+"/pass",login_data)

    home_page = s.get(baseUrl+"/sys?submit=Refresh", stream=True)
    html=bs(home_page.content, "html.parser")

    switchName = html.find("input", {"name":"nm"})["value"]
    macAddress = html.find_all("font")[2].text
    swVer = html.find_all("font")[4].text
    hwVer = html.find_all("font")[6].text

    print("Switch Names: " + switchName)
    print("Mac Address: " + macAddress)
    print("S/W Version: " + swVer)
    print("H/W Version: " + hwVer)
