from libPython.tnpClassUtils import tnpSample

### qll stat
dirtest = '/pool/phedex/userstorage/balvarez/TnP_ttbarRun3_merged/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DYJetsToLL_M50_Electron_0.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_EGamma_Run2022_0.root', lumi = 1.12),
}

