import os
from multiprocessing import Pool

def GetCommand(command, den, year, lep, tag):
  return command%(den, year, lep, tag)

def ex(command):
  print 'Executing command: ', command
  os.system(command)

def RunTnP(listOfArguments):
  print 'RunTnP: ', listOfArguments
  den, year, lep, tag = listOfArguments 
  for c in commands: ex(GetCommand(c, den, year, lep, tag))
  return True

den = ['ttH'] 
num = ['passttH'] 
years = ['2016', '2017', '2018']
leps = ['3l', '2lss']

listInput = []
for d in den:
  for y in years:
    for l in leps:
      for n in num:
        listInput.append([d,y,l,n])
njobs = len(listInput)
print 'List of inputs (%i):\n'%njobs, listInput

commands = [
#3l muon
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --createBins',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --createHists',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --doFit',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --doFit --mcSig --altSig',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --doFit --altSig',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --doFit --altBkg',
  'python tnpEGM_fitter.py etc/config/settings_%s_ele_%s_%s.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_3l.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_3l.py --flag %s --sumUp'

#2lss muons
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2016_2lss.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_muo_2017_2lss.py --flag %s --sumUp'

#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --createBins',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --createHists',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --doFit',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --doFit --mcSig --altSig',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --doFit --altSig',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --doFit --altBkg',
#  'python tnpEGM_fitter.py etc/config/settings_%s_muo_2018_2lss.py --flag %s --sumUp'

#3l electrons
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_3l.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_3l.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_3l.py --flag %s --sumUp'

#2lss electrons
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2016_2lss.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2017_2lss.py --flag %s --sumUp'

# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --createBins',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --createHists',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --doFit',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --doFit --mcSig --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --doFit --altSig',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_%s_ele_2018_2lss.py --flag %s --sumUp'

]
if njobs == 1:
  print 'Secuential mode...'
  RunTnP(listInput[0])
else: 
  print 'Multiprocess: calculating %i scale factors...'%njobs
  pool = Pool(njobs)
  retlist = pool.map(RunTnP, listInput)
  pool.close()
  pool.join()

#os.system("mv results results_mar25_ttH")
