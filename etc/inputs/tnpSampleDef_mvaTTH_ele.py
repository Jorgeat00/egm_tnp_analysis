from libPython.tnpClassUtils import tnpSample


#All data checked
### qll stat
#dirtest = '/pool/ciencias/userstorage/juanr/TnPtrees/old/TnPfeb19/TnPfeb19/2017/'
#dirtest='/eos/cms/store/group/phys_muon/atrapote/MuonPOG/MVAid/'
#dirtest='/mnt_pool/c3_users/user/jorgeat/Documentos/muon_mva/trees/' #oldone
#dirtest='/eos/cms/store/group/phys_muon/jayllont/muon_mva/TnP_ntuples/'
dirtest='/lustrefs/hdd_pool_dir/nanoAODv12/geq1l_2022Run3/mvaTTHSF_run3/TnP_ntuples/Electron/2023/'
dirtest_data='/lustrefs/hdd_pool_dir/nanoAODv12/geq1l_2022Run3/mvaTTHSF_run3/TnP_ntuples/Electron/2023/allData/'
test = {'DY' : tnpSample('DY',   dirtest + 'DYJetsToLL_M_50_nominal_2023.root', isMC = True, nEvts = -1),
        'DYAlt' : tnpSample('DYAlt',   dirtest + 'DYJetsToLL_M_50_alternative_2023.root', isMC = True, nEvts = -1),
        #'data' : tnpSample('data', dirtest + '*Run2023C.root', lumi = 17.794)} #check lum
        'data' : tnpSample('data', dirtest_data + '*.root', lumi = 17.794)}
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

