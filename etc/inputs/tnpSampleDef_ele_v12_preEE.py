from libPython.tnpClassUtils import tnpSample

dirMC = '/lustrefs/hdd_pool_dir/nanoAODv12/wz-run3/trees_v3/TnP/Electron/2022/MC/'
dirMCalt = '/lustrefs/hdd_pool_dir/nanoAODv12/wz-run3/trees_v3/TnP/Electron/2022/MCAlt/'
dirdata = '/lustrefs/hdd_pool_dir/nanoAODv12/wz-run3/trees_v3/TnP/Electron/2022/Data/'
test = {'DY'   : tnpSample('DY',   dirMC + 'DYJetsToLL_M_50_part*.root', isMC = True, nEvts = -1), 
        'DYAlt': tnpSample('DYAlt', dirMCalt + 'DYJetsToLL_M_50_part*.root', isMC = True, nEvts = -1), 
        'data' : tnpSample('data', dirdata + '*Run2022*.root', lumi = 8.2),
}

