import json
print("INterface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
data = []
with open("jsoon.py.json", "r") as f:
    d = json.load(f)

for i in d['imdata']:
    dn = i['l1PhysIf']['attributes']['dn']
    de = i['l1PhysIf']['attributes']['descr']
    s = i['l1PhysIf']['attributes']['speed']
    mtu = i['l1PhysIf']['attributes']['mtu']
    
    print("{:<50} {:<20} {:<8} {:<8}".format(dn, de, s, mtu))