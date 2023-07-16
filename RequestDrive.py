import json
import requests



def EnvioDrive(arquivo,archive):
    

 headers = {"Authorization": "Bearer ya29.a0AbVbY6Nxkn_eki1j2MyRxIEzVhOzvfakE8BB288-d0eXh-obytCQwZFW9LdI-kGJztxKkiKEcVvlzYUSnkLppXV0OuFLTV-2kiViZ24HjUPf1G8MDIG6xfYVto6QfwW8ultVwYNT9dTPRl7D-JpuWODiPdi9aCgYKAfUSARESFQFWKvPlOF2KOf3UucoSswoodVEq-w0163"}
 para = {
    "name": archive,
    "parents":["167kh3HWDdZ1nXSrjp0q2xLOv4kn55miodb02lQTGwSq2csCjE_XlTPIOmS6tSsFmxdMMv-oh"]
}
 files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open(arquivo, "rb")
}
 r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
 print(r.text)

