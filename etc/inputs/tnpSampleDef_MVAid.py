from libPython.tnpClassUtils import tnpSample

### qll stat
#dirtest = '/pool/ciencias/userstorage/juanr/TnPtrees/old/TnPfeb19/TnPfeb19/2017/'
#dirtest='/eos/cms/store/group/phys_muon/atrapote/MuonPOG/MVAid/'
#dirtest='/mnt_pool/c3_users/user/jorgeat/Documentos/muon_mva/trees/' #oldone
#dirtest='/eos/cms/store/group/phys_muon/jayllont/muon_mva/TnP_ntuples/'
dirtest='/eos/cms/store/group/phys_muon/jayllont/muon_mva/TnP_ntuples_2023_lxplus7/'
dirtest2='/eos/cms/store/group/phys_muon/jayllont/muon_mva/TnP_ntuples_golden/'
test = {#'DY'  : tnpSample('DY',   dirtest + 'DY_23_BPix_merged.root', isMC = True, nEvts = -1),
        #'data': tnpSample('data', dirtest + 'Muon*Run2023D*_merged.root', lumi = 9.52 )} #Run D: 9.516
        'DY'  : tnpSample('DY',   dirtest + 'DY_23_merged.root', isMC = True, nEvts = -1),
        'data': tnpSample('data', dirtest + 'Muon*Run2023C*_merged.root', lumi = 17.98 )} #Run C: 17.98
        #'DY' : tnpSample('DY',   dirtest + 'DY_*_merged.root', isMC = True, nEvts = -1),
        #'data' : tnpSample('data', dirtest + 'Muon*Run2023*_merged.root', lumi = 27.5)} #check lumi
        #'data' : tnpSample('data', dirtest2 + '*_Run2022*_merged.root', lumi = 34.3)} #check lumi
        #'DY' : tnpSample('DY',   dirtest + 'DY_preEE_merged.root', isMC = True, nEvts = -1),
        #'data' : tnpSample('data', dirtest2 + '*_Run2022[B,C,D]_merged.root', lumi = 7.97)}#preEE->8.62, postEE->26.92
        #'data' : tnpSample('data', dirtest2 + '*_Run2022[E,F,G]_merged.root', lumi = 26.34),}
        #'DY' : tnpSample('DY',   dirtest + 'DY_postEE_merged.root', isMC = True, nEvts = -1)}
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

