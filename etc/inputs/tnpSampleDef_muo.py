from libPython.tnpClassUtils import tnpSample

### qll stat
dirtest = '/pool/phedex/userstorage/balvarez/TnP_ttbarRun3_merged/'
diralt = '/pool/phedex/userstorage/balvarez/TnP_ttbarRun3_alt_merged/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DYJetsToLL_M50_Muon_0.root', isMC = True, nEvts = -1), 
        'DYAlt': tnpSample('DYAlt', diralt + 'Tree_DYJetsToLL_M50_Muon_0.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_*Muon_Run2022_0.root', lumi = 1.2),
}

