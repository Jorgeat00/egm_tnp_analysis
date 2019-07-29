from libPython.tnpClassUtils import tnpSample

dirtest = '/pool/ciencias/userstorage/balvarez/TnPntuplesttH/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Muon2018_*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2018*.root', lumi = 51.7)}
#test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Muon2018_0.root', isMC = True, nEvts = -1), 
#        'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2018A_0.root', lumi = 51.7)}
