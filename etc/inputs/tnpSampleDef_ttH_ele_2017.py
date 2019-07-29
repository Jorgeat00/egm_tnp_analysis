from libPython.tnpClassUtils import tnpSample

dirtest = '/pool/ciencias/userstorage/balvarez/TnPntuplesttH/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Electron2017_*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleElectron_Run2017*.root', lumi = 41.9)}
