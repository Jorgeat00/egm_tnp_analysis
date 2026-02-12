from libPython.tnpClassUtils import tnpSample

#All checked

### qll stat
#dirtest = '/pool/ciencias/userstorage/juanr/TnPtrees/old/TnPfeb19/TnPfeb19/2017/'
#dirtest='/eos/cms/store/group/phys_muon/atrapote/MuonPOG/MVAid/'
#dirtest='/mnt_pool/c3_users/user/jorgeat/Documentos/muon_mva/trees/' #oldone
#dirtest='/eos/cms/store/group/phys_muon/jayllont/muon_mva/TnP_ntuples/'
dirtest='/lustrefs/hdd_pool_dir/nanoAODv12/geq1l_2022Run3/mvaTTHSF_run3/TnP_ntuples/Muon/2023/'
dirtest_data = '/lustrefs/hdd_pool_dir/nanoAODv12/geq1l_2022Run3/mvaTTHSF_run3/TnP_ntuples/Muon/2023/allData/'
test = {'DY' : tnpSample('DY',   dirtest + 'MC/DYJetsToLL/*.root', isMC = True, nEvts = -1),
        'DYAlt' : tnpSample('DYAlt',   dirtest + 'DYJetsToLL_alternative_2023.root', isMC = True, nEvts = -1),
        #'data' : tnpSample('data', dirtest + '*Run2023C.root', lumi = 17.794)} #check lum
        'data' : tnpSample('data', dirtest_data + '*.root', lumi = 17.794)}
        #'DY'   : tnpSample('DY',   dirtest + 'DYJetsToLL_M50_pu_trigger.root', isMC = True, nEvts = -1), 
        #'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run*pu_trigger.root', lumi = 59.7)}
        #'data' : tnpSample('data', dirtest + 'Tree_SingleMuon_Run2017*.root', lumi = 41.856),

