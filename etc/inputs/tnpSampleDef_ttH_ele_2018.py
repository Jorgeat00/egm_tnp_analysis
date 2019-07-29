from libPython.tnpClassUtils import tnpSample

dirtest = '/pool/ciencias/userstorage/balvarez/TnPntuplesttH/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Electron2018_*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleElectron_Run2018*.root', lumi = 51.7)}
