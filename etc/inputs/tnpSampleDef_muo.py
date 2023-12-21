from libPython.tnpClassUtils import tnpSample

#dirMC = '/beegfs/data/nanoAODv11/TnP/preliminaryMuonMC/'
#dirMCalt = '/beegfs/data/nanoAODv11/TnP/preliminaryMuonMCAlt/'
#dirdata = '/beegfs/data/nanoAODv11/TnP/preliminaryMuonDATA/'
#dirMC = '/beegfs/data/nanoAODv11/TnP/Muon/MC/'
#dirMCalt = '/beegfs/data/nanoAODv11/TnP/Muon/MCAlt/'
#dirdata = '/beegfs/data/nanoAODv11/TnP/Muon/DATA/'
dirMC = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Muon_conept_v2/MC/'
dirMCalt = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Muon_conept_v2/MCAlt/'
dirdata = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Muon_conept_v2/Data/'
test = {'DY'   : tnpSample('DY',   dirMC + 'DYJetsToLL_M-50_part*.root', isMC = True, nEvts = -1), 
        'DYAlt': tnpSample('DYAlt', dirMCalt + 'DYJetsToLL_M-50_part*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirdata + '*Run2022*.root', lumi = 20.7),
}

