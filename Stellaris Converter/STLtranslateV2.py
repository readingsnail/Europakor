from configparser import ConfigParser as cfp
import os
import multiprocessing as mp
from numpy import array_split
import glob

class Line:
    def __init__(self, line, dlmVal, dlmChain, wrap):
        if dlmVal:
            try:
                self.name, self.value = line.split(dlmVal, 1)
            except:
                print("Error with value delimiter:| %s | %s |" % (line, dlmVal))
                      
            self.value = unwrap(self.value, wrap)

            if dlmChain:
                try:
                    self.name, self.chain = self.name.split(dlmChain)
                except:
                    print("Error with chain delimiter:| %s | %s |" % (self.name, dlmChain))

class File:
    def __init__(self, path, config):
        self.dat = []
        
        with open(path, 'r', encoding='UTF-8-SIG') as f:
            for line in f.readlines():
                line = line[:line.find(config['ref'])].strip()

                if line and line != config['headline']:
                    self.dat.append(Line(line, config['valdelim'], config['chaindelim'], config['wletter']))

    def out(self, path, config):
        text = ''
        
        if config['headline']:
            text += config['headline'] + '\n'

        indent = ' ' * int(config['indent'])

        for line in self.dat:
            text += '%s%s%s%s%s%s%s%s\n' % (indent, line.name, config['chaindelim'], line.chain, config['valdelim'], config['wletter'], line.value, config['wletter'])

        with open(path, 'w', encoding='UTF-8-SIG') as f:
            f.write(text)
            
def unwrap(line, letter) :
        result = line
        if result == '' or result == letter :
            result = ''
        else :
            if result[0] == letter :
                result = result[1:]
            if result[-1] == letter :
                result = result[:-1]
            else :
                pass
        return result

def wrap(s, w):
    return '%s%s%s' % (w, s, w)

def worker1(lst, paths, config):
    print("Checking if chain delimiter has been sent correctly: %s" % config['chaindelim'])
    print("Checking if value delimiter has been sent correctly: %s" % config['valdelim'])
    
    for path in paths:
        lst.append(File(path, config))

def worker2(lst, paths, config):
    for i in range(len(lst)):
        lst[i].out(paths[i], config)

if __name__ == '__main__':
    _config_default = """
## Orient : directory of JProc file (*.properties) you want to convert.
[PATH]
    Orient = ./jproc/
    Dest = ./result/

[DATAFORMAT]
     ## name of file format u convert from.
    ## these values are case sensitive.
    orn_formatname = JavaProperties
    
    ## name of file format you'll get as result.
    ## these values are case sensitive.
    dest_formatname = ParadoxPsudoYml_l_english
    
    ##example of file format, section name [sectionname] must be same as orn/dest_name values of [data] section.
    ##others will be ignored.
    ##you can use multiple charactors as same delmitor but it may cause unintened behavior, use at your own risk.
    ##these values must be wraped with ' (single quato).
    [ParadoxPsudoYml]
    ## suffix of file, used for searching file in directory.
        suffix = '.yml'
        valdelim =  ' '
        chaindelim = ':'
        ref = '#'
        wletter = '"'
        headline = ''
        indent = 1
    [ParadoxPsudoYml_l_english]
    ## suffix of file, used for searching file in directory.
        suffix = '.yml'
        valdelim =  ' '
        chaindelim = ':'
        ref = '#'
        wletter = '"'
        headline = 'l_english:'
        indent = 1
    [ParadoxPsudoYml_l_english_tag]
    ## suffix of file, used for searching file in directory.
        suffix = '.yml'
        valdelim =  ' '
        chaindelim = ':'
        ref = '#'
        wletter = '"'
        headline = 'l_english_tag:'
        indent = 1
    [JavaProperties]
        suffix = '.properties'
        valdelim = '='
        chaindelim = '|'
        ref = '#'
        wletter = '"'
        headline = ''
        indent = 0
    [JavaPropertiesOldType]
        ## suffix of file, used for searching file in directory.
        suffix = '.properties'
        valdelim = '='
        chaindelim = '코'
        ref = '#'
        wletter = ''
        headline = ''
        indent = 0

## error handling and print setting for line parse.
#### "ignore" : just ignore that line does nothing
#### "warnwrite" : try parse and warn that line at result 
#### "warnpass"  : skip line and warn that line at result 
#### "nowrite" : don't write file and warn that line at result
[LINEPARSE]
    NoKey = warnpass
    NoValue = warnwrite
    BadKey = warnwrite
    NoDelim = nowrite
    NoData = ignore

[DEBUG]
    DebugPrint = False
"""

    _numOfProcs = 4

    print("Type in working directory")
    print("Example: C:\\Users\\Administrator")
    os.chdir(input())
    
    config = cfp()
    configOrient = {}
    configDest = {}
    
    try:
        _configfile = open('STSconfig.ini', 'r')
        config.read('STSconfig.ini')
        print("Read STSconfig.ini")
    except:
        config.read_string(_config_default)
        print("Did not read STSconfig.ini")
        print("Trying to check current directory")
        print(glob.glob(os.getcwd() + '\\*.ini'))
        print("Current directory is : %s" % os.getcwd())

    config['PATH']['Orient'] = os.path.abspath(config['PATH']['Orient']) 
    config['PATH']['dest'] = os.path.abspath(config['PATH']['dest'])

    configOrnt = config[config['DATAFORMAT']['orn_formatname'] ]
    configOrnt['name'] = config['DATAFORMAT']['orn_formatname']
    configDest = config[config['DATAFORMAT']['dest_formatname'] ]
    configDest['name'] = config['DATAFORMAT']['dest_formatname']

    print("Checking if chain delimiter is read correctly: %s" % configOrnt['chaindelim'])
    print("Checking if value delimiter is read correctly: %s" % configOrnt['valdelim'])

    for i in configOrnt:
        configOrnt[i] = unwrap(configOrnt[i], "'")
    for i in configDest:
        configDest[i] = unwrap(configDest[i], "'")
    
    paths = glob.glob(os.path.join(config['PATH']['orient'], ('*%s' % unwrap(configOrnt['suffix'], "'"))))
    paths = array_split(paths, _numOfProcs)

    manager = mp.Manager()
    files = [manager.list() for i in range(_numOfProcs)]

    procs = [mp.Process(target=worker1, args=(files[i], paths[i], configOrnt)) for i in range(_numOfProcs)]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    for i in range(_numOfProcs):
        for ii, path in enumerate(paths[i]):
            paths[i][ii] = path.replace(config['PATH']['orient'], config['PATH']['dest']).replace(configOrnt['suffix'], configDest['suffix'])

    procs = [mp.Process(target=worker2, args=(files[i], paths[i], configDest)) for i in range(_numOfProcs)]

    for proc in procs:
        proc.start()
        
    for proc in procs:
        proc.join()

    input()
