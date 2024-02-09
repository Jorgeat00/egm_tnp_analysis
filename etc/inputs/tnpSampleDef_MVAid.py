from libPython.tnpClassUtils import tnpSample

### qll stat
#dirtest = '/pool/ciencias/userstorage/juanr/TnPtrees/old/TnPfeb19/TnPfeb19/2017/'
#dirtest='/eos/cms/store/group/phys_muon/atrapote/MuonPOG/MVAid/'
#dirtest='/mnt_pool/c3_users/user/jorgeat/Documentos/muon_mva/trees/' #oldone
dirtest='/eos/cms/store/group/phys_muon/jayllont/muon_mva/'
test = {'DY' : tnpSample('DY',   dirtest + 'DYpreEE/DY_preEE_merged.root', isMC = True, nEvts = -1),
        'data' : tnpSample('data', dirtest + 'Data/Data_DE/Muon_Run2022*_merged.root', lumi = 25)} #check lumi
        #'DY'   : tnpSample('DY',   dirtest + 'DYJetsToLL_M50_pu_trigger.root', isMC = True, nEvts = -1), 
        #'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run*pu_trigger.root', lumi = 59.7)}
        #'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),
        #'dataMP' : tnpSample('dataMP', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),
        #'dataL' : tnpSample('dataL', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),
        #'dataM' : tnpSample('dataM', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),
        #'dataT' : tnpSample('dataT', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),
        #'dataB': tnpSample('dataB',dirtest + 'Tree_SingleMuon_Run2017B_TnP.root', lumi = 4.79),
        #'dataC': tnpSample('dataC',dirtest + 'Tree_SingleMuon_Run2017C_TnP.root', lumi = 9.754),
        #'dataD': tnpSample('dataD',dirtest + 'Tree_SingleMuon_Run2017D_TnP.root', lumi = 4.32),
        #'dataE': tnpSample('dataE',dirtest + 'Tree_SingleMuon_Run2017E_TnP.root', lumi = 9.423),
        #'dataF': tnpSample('dataF',dirtest + 'Tree_SingleMuon_Run2017F_TnP.root', lumi = 13.566)}

