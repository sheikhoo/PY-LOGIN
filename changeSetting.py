from requests import Session
from bs4 import BeautifulSoup as bs
import lxml.html
from lxml.cssselect import CSSSelector

with Session() as s:
    baseUrl="http://192.168.155.111"
    password="Supericb"

    site = s.get(baseUrl+"/password.htm")

    login_data = {"password":password}
    s.post(baseUrl+"/pass",login_data)

    system_page = s.get(baseUrl+"/sys?submit=Refresh", stream=True)
    html=bs(system_page.content, "html.parser")

    #print(html.find_all("input"))

    home_page = s.get(baseUrl+"/sys?submit=Refresh", stream=True)

    home_page.raw.decode_content = True
    tree = lxml.html.parse(home_page.raw)

    td_empformbody = CSSSelector('input')
    for elem in td_empformbody(tree):
        print(elem.value)

    # setting={
    #     "ip": html.find("input", {"name":"ip"})["value"],
    #     "sm": html.find("input", {"name":"sm"})["value"],
    #     "gw": html.find("input", {"name":"gw"})["value"],
    #     "mvlan": html.find("input", {"name":"mvlan"})["value"],
    #     "nm": html.find("input", {"name":"nm"})["value"],
    #     "pw": html.find("input", {"name":"pw"})["value"],
    #     "timeout": html.find("input", {"name":"timeout"})["value"],
    #     "SNMP": html.find("input", {"name":"SNMP"})["value"],
    #     "trap": html.find("input", {"name":"trap"})["value"],
    #     "Readcommunity": html.find("input", {"name":"Readcommunity"})["value"],
    #     "Writecommunity": "t", #html.find("input", {"name":"Writecommunity"})["value"],
    #     "Trapcommunity": html.find("input", {"name":"Trapcommunity"})["value"],
    #     "submit": "Apply"
    # }

    #s.post(baseUrl+"/sys",setting)
