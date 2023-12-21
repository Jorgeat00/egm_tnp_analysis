from libPython.tnpClassUtils import tnpSample

#dirMC = '/beegfs/data/nanoAODv11/TnP/preliminaryElectronMC/'
#dirMCalt = '/beegfs/data/nanoAODv11/TnP/preliminaryElectronMCAlt/'
#dirdata = '/beegfs/data/nanoAODv11/TnP/preliminaryElectronDATA/'
dirMC = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Electron_conept_v2/MC/'
dirMCalt = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Electron_conept_v2/MCAlt/'
dirdata = '/lustrefs/hdd_pool_dir/nanoAODv11/TnP/Electron_conept_v2/Data/'
test = {'DY'   : tnpSample('DY',   dirMC + 'DYJetsToLL_M-50_part*.root', isMC = True, nEvts = -1), 
        'DYAlt': tnpSample('DYAlt', dirMCalt + 'DYJetsToLL_M-50_part*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirdata + '*Run2022*.root', lumi = 20.7),
}

