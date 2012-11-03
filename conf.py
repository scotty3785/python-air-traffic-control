import json

configfile = "config.json"
loaded = ""

def writeout():
    with open(configfile,"w") as f:
        json.dump(loaded,f)
    
def load():
    global loaded
    with open(configfile) as f:
        loaded = json.load(f)

load()