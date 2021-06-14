import urllib.request, urllib.parse, urllib.error
import json
import ssl
cant = 0
sum = 0
valor=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
if len(address) >0:
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())

    info = json.loads(data)
    #print('Count:', len(info["comments"]))
    #print(info["comments"][1])
    #print(info["comments"][2])
    #print(info["comments"][2]["count"])
    #print(info["comments"])
    # fuentes:
    #Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    #Actual data: http://py4e-data.dr-chuck.net/comments_892448.json (Sum ends with 99)
    #com=info["comments"]

    for item in info["comments"]:
        #print('Valor info', item["count"])
        valor=item["count"]
        sum= sum + int(valor)
print('Sum:',sum)
