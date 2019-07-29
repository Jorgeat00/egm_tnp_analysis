from libPython.tnpClassUtils import tnpSample

dirtest = '/pool/ciencias/userstorage/balvarez/TnPntuplesttH/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DY_Muon2016_*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2016*.root', lumi = 35.9)}
