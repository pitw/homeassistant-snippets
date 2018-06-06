import requests
from requests.auth import HTTPDigestAuth
import xml.etree.ElementTree as ET

url = 'http://***CAM_IP***/camera-cgi/admin/param.cgi?action=list&group=SystemInfo'

response = requests.get(url, auth=HTTPDigestAuth('***CAM_USER', '***CAM_PASSWORD***'))
if(response.ok):
 tree = ET.fromstring(response.content)
 values = tree.find('envSensor')
 temp = values.find('RH')
 print(int(temp.text))
else:
 response.raise_for_status()
