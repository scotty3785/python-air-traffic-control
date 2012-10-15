import csv
import configparser

class info_logger:
    def __init__(self,configfile):
        self.config = configparser.ConfigParser()
        self.config.read_file(open(configfile))
        self.dictkeys = eval(self.config['logger']['dictkeys'])
        self.logfile = self.config['logger']['logfile']
        self.csvwriter = csv.DictWriter(open(self.logfile,"w"),self.dictkeys)
        self.csvwriter.writeheader()
        self.workingdict = dict(zip(self.dictkeys,[None]*10))
    
    def add_value(self,id,key,value):
        if key not in self.dictkeys or id == None:
            return
        if self.workingdict['id'] != id and self.workingdict['id'] != None:
            self.writeout()
        self.workingdict[key] = value
    
    def writeout(self):
        if self.workingdict['id'] != None:
            self.csvwriter.writerow(self.workingdict)
            self.workingdict = dict(zip(self.dictkeys,[None]*10))
