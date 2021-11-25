from libPython.tnpClassUtils import tnpSample

### qll stat
dirtest = '/eos/cms/store/group/phys_muon/balvarez/TnP_TopEFT_merged/'
test = {'DY'   : tnpSample('DY',   dirtest + 'Tree_DYJetsToLL_M*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856)}

