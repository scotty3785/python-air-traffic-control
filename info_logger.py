import csv
import configparser
import os

class info_logger:
    def __init__(self,configfile):
        self.config = configparser.ConfigParser()
        self.config.read_file(open(configfile))
        self.dictkeys = eval(self.config['logger']['dictkeys'])
        self.logfile = self.config['logger']['logfile']
        self.dictlist = []
        writelater = self.check_exists()
        self.file = open(self.logfile,"w")
        self.csvwriter = csv.DictWriter(self.file,self.dictkeys)
        self.csvwriter.writeheader()
        self.workingdict = dict(zip(self.dictkeys,[None]*10))
        self.id = 0
        if writelater:
            for row in self.dictlist:
                self.workingdict = row
                self.writeout()
            try:
                self.id = self.dictlist[-1]['id']
            except IndexError:
                print("!!!!!CSV not written out properly to disk from previous run!!!!!")
                
    
    def check_exists(self):
        if os.path.exists(self.logfile):
            with open(self.logfile) as f:
                csvreader = csv.DictReader(f)
                for row in csvreader:
                    self.dictlist.append(row)
            return True
            
    def get_id(self):
        return self.id
    
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
            self.file.flush()
            os.fsync(self.file.fileno())
