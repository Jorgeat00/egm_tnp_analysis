#############################################################
########## General settings
#############################################################
# flag that defined the numerator
flags = {
    'passtight'   : '(Probe_cutBased == 4 && Probe_pt > 35 && abs(Probe_eta) < 2.4 && (abs(Probe_eta-Probe_deltaEtaSC)>1.566 || abs(Probe_eta-Probe_deltaEtaSC) < 1.444) && abs(Probe_dxy) < 0.2 && abs(Probe_dz) < 0.5)',
}
#baseOutDir = 'results/eletight/'
#baseOutDir = 'results/eletight_inc/'
#baseOutDir = 'results/eletight_newbinning/'
#baseOutDir = 'results/eletight_forapproval/' #bining 1.44 and 1.566 
#baseOutDir = 'results/eletight_forapproval_v2/'#new eta binning with 1.5
#baseOutDir = 'results/eletight_forapproval_v3/' #no Alt sample
#baseOutDir = 'results/elerecoandtight_alt_effMC_newbinning_v2/' #no Alt sample
#baseOutDir = 'results/elerecoandtight_alt_effMC_newbinning_v3/' #no Alt sample
baseOutDir = 'results/elerecoandtight_clustereta/' #no Alt sample

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef_ele as tnpSamples
tnpTreeDir = './'#tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.test['data'].clone(),
    'mcNom'  : tnpSamples.test['DY'].clone(),
    #'mcAlt'  : tnpSamples.test['DY'].clone(),
    'mcAlt'  : tnpSamples.test['DYAlt'].clone(),
    'tagSel' : tnpSamples.test['DY'].clone(),
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017C'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017D'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017E'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017F'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    #samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_2018_runAB.totWeight'
#weightName = 'puWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   #{ 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.9, 1.2, 2.1, 2.4] },
   #{ 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.5, 1.0, 2.0, 2.4] },
   #{ 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.4] },
   #{ 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.4] },
    { 'var' : 'abs(Probe_eta - Probe_deltaEtaSC )' , 'type': 'float', 'bins': [0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.4] },
   { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [35,40,45,55,70,100,500] },
   #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [35,45,55,65,85,200] },
   #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [30,40,50,60,80,200] },
   #{ 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 2.4] },
   #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [20,30,40,50,120] },
   #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [20,30,40,50,60,80,120] },
   # { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [35,1200] },
   #{ 'var' : 'TnP_ht' , 'type': 'float', 'bins': [30,100,200,300,400,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'
#cutBase = "TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.4 && Tag_pfRelIso03_all < 0.15 && Probe_pt > 20 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched && Probe_cutBased > 1"
cutBase = "TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.4 && (abs(Tag_eta-Tag_deltaEtaSC)>1.566 || abs(Tag_eta-Tag_deltaEtaSC) < 1.444) && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched"
#cutBase += " && Probe_passMP == 1" # Eff over medium prompt
# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,90.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    #bin18
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,200.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,80.]","betaF[0.04,0.01,0.05]","gammaF[0.03, 0.02, 0.05]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin17 ok
    #"meanP[-2.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.01,0.0,5.0]",
    #"meanF[-2.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.8,0.5,5.0]",
    #"acmsP[110.,100.,120.]","betaP[0.1,0.01,0.5]","gammaP[0.05, 0.04, 0.06]","peakP[90.0]",
    #"acmsF[110.,100.,120.]","betaF[0.08,0.01,0.1]","gammaF[0.06, 0.01, 0.1]","peakF[90.0]",
    #bin15 ok
    #"meanP[0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[100.,80.,200.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin15 ok
    #"meanP[0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[100.,80.,200.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[90.,80.,200.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin18 looks very good, but eff. to high
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.1,0.0,1.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[0.1,0.1,1.0]","sosP[0.1,0.0,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.1,0.0,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[0.1,0.1,1.0]","sosF[0.1,0.0,5.0]",
    #"acmsP[100.,90.,200.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[100.,90.,200.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin4, better worked, maybe bin 12 too
    #"meanP[0.0,-1.0,1.0]","sigmaP[0.5,-1.0,1.0]","alphaP[0.0,-1,1]" ,'nP[3,-5,5]',"sigmaP_2[0.5,-1,1]","sosP[0.5,-1,1]",
    #"meanF[0.0,-1.0,1.0]","sigmaF[0.5,-1.0,1.0]","alphaF[0.0,-1,1]",'nF[3,-5,5]',"sigmaF_2[0.5,-1,1]","sosF[0.5,-1,1]",
    #"acmsP[58.,40.,93.]","betaP[0.5,-1.0,1.5]","gammaP[0.0, -1.0, 1]","peakP[92.0]",
    #"acmsF[58.,40.,93.]","betaF[0.3,-1.0,1.5]","gammaF[0.0, -1.0, 1]","peakF[92.0]",
    #bin4
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.4,-1.0,1.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1.0,0.05,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[75.,60.,110.]","betaF[0.04,0.03,0.08]","gammaF[0.02, 0.001, 1]","peakF[91.0]",
    #bin03,04
    #"meanP[0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,5.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.1,0.0,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[60.,50.,120.]","betaF[0.04,0.01,1.0]","gammaF[0.1, 0.005, 1]","peakF[85.0]",
    #bin14
    #"meanP[1.0,-4.0,4.0]","sigmaP[0.5,0.1,1.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[1.0,-4.0,4.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,-0.5,5.0]",
    #"acmsP[80.,75.,100.]","betaP[0.04,0.01,1.0]","gammaP[-0.1, -1.0, 1.0]","peakP[90.0]",
    #"acmsF[80.,75.,100.]","betaF[0.1,0.0,5.0]","gammaF[0.1, -1.0, 1.0]","peakF[90.0]",
    #binX
    #"meanP[0.3,-1.0,1.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,1.0]",
    #"meanF[0.1,-1.0,1.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,1.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[90.0]",
    #"acmsF[75.,50.,110.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin8,9,10
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,1.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,1.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[95.0]",
    #"acmsF[75.,50.,110.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[95.0]",
    #bin18
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.002,0.001,0.003]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[85.,50.,100.]","betaF[0.08,0.07,0.09]","gammaF[0.028, 0.02, 0.03]","peakF[90.0]",
    #bin15
    #"meanP[0.5,0.0,2.0]","sigmaP[1,0.7,1.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.5,0.0,2.0]","sigmaF[1,0.1,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.2,0.01,0.3]",
    #"acmsP[85.,50.,150.]","betaP[0.04,0.01,0.5]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[85.,50.,100.]","betaF[0.08,0.07,0.5]","gammaF[0.028, 0.02, 0.03]","peakF[90.0]",
    #bin15
    #"meanP[0.5,0.0,2.0]","sigmaP[0.1,0.0,0.5]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.1,-0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[85.,50.,150.]","betaP[0.04,0.01,0.5]","gammaP[0.1, 0.005, 1]","peakP[91.0]",
    #"acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin16
    #"meanP[0.5,0.0,2.0]","sigmaP[0.1,0.0,0.5]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.1,-0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[85.,50.,150.]","betaP[0.04,0.01,0.5]","gammaP[0.1, 0.005, 1]","peakP[91.0]",
    #"acmsF[100.,90.,200.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin17
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[100.,90.,200.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin17
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[100.,90.,200.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[93.0]",
    #"acmsF[100.,90.,200.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[93.0]",
    #bin22
    #"meanP[-0.0,-3.0,3.0]","sigmaP[0.5,0.0,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[0.5,0.01,5.0]","sosP[0.5,-1.0,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,2.0]",
    #"acmsP[100.,50.,110.]","betaP[0.04,0.01,0.06]","gammaP[0.5, 0.1, 2]","peakP[89.0]",
    #"acmsF[196.,170.,220.]","betaF[0.05,0.01,0.06]","gammaF[0.5, 0.01, 1]","peakF[90.0]",    
    #bin22
    "meanP[-0.0,-3.0,3.0]","sigmaP[0.5,0.0,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[0.5,0.01,5.0]","sosP[0.5,-1.0,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,2.0]",
    "acmsP[90.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.5, 0.1, 2]","peakP[89.0]",
    "acmsF[196.,170.,220.]","betaF[0.05,0.01,0.06]","gammaF[0.5, 0.01, 1]","peakF[90.0]",
    #bin4
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,1.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,1.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[90.0]",
    #"acmsF[75.,50.,110.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin4 0.68, bin 19 and bin 22
    #"meanP[0.2,-2.0,2.0]","sigmaP[0.5,0.1,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.2,-2.0,2.0]","sigmaF[0.5,0.1,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[75.,50.,100.]","betaP[0.06,0.01,0.2]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[75.,50.,80.]","betaF[0.06,0.01,0.2]","gammaF[0.1, -2, 2]","peakF[90.0]",
    #bin
    #"meanP[0.2,-2.0,2.0]","sigmaP[0.5,0.1,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.2,-2.0,2.0]","sigmaF[0.5,0.1,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.1,0.01,5.0]",
    #"acmsP[75.,30.,120.]","betaP[0.06,0.01,0.2]","gammaP[0.1, -4, 4]","peakP[93.0]",
    #"acmsF[75.,30.,100.]","betaF[0.1,0.01,0.5]","gammaF[0.1, -4, 4]","peakF[90.0]",
    #bin14
    #"meanP[1.0,-5.0,5.0]","sigmaP[1,0.0,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.5,0.,1.0]",
    #"meanF[1.4,-5.0,5.0]","sigmaF[1,0.0,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[2.4,0.5,5.0]",
    #"acmsP[75.,50.,90.]","betaP[0.04,0.01,0.06]","gammaP[0.05, 0.0, 1]","peakP[95.0]",
    #"acmsF[75.,60.,80.]","betaF[0.06,0.03,0.08]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin22,bin23 weird errors
    #"meanP[0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]",'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.2,0.0,1.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[1,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.5,0.5,6.0]","sosF[0.2,0.0,1.0]",
    #"acmsP[60.,50.,100.]","betaP[0.05,0.01,0.1]","gammaP[-0.1, -2, 2]","peakP[95.0]",
    #"acmsF[60.,50.,100.]","betaF[0.05,0.01,0.1]","gammaF[-0.1, -2, 2]","peakF[95.0]",
    #bin22
    #"meanP[0.4,-5.0,5.0]","sigmaP[1,0.01,1.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.4,-1.0,1.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1.0,0.05,2.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, -0.5, 1]","peakP[93.0]",
    #"acmsF[60.,50.,75.]","betaF[0.01,-0.5,0.08]","gammaF[0.01, -1, 1]","peakF[93.0]",

]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
