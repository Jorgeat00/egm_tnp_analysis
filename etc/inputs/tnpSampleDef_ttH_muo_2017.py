from libPython.tnpClassUtils import tnpSample

dirtest = '/pool/ciencias/userstorage/balvarez/TnPntuplesttH/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Muon2017_*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.9)}
