#############################################################
########## General settings
#############################################################
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passMediumId': '(Probe_mediumId == 1)',# && Probe_isTrigMatched == 1)',#TnP_trigger == 1)',
    'passTightId': '(Probe_tightId == 1)',# && Probe_isTrigMatched == 1)',#TnP_trigger == 1)',
    'passMVAIdMedium': '(Probe_mvaMuID > 0.08)',# && Probe_isTrigMatched == 1)',#TnP_trigger == 1)',
    'passMVAIdTight': '(Probe_mvaMuID > 0.20)',# && Probe_isTrigMatched == 1)',#TnP_trigger == 1)',
    'passSoftMVA': '(Probe_softMva > 0.58)',# && TnP_trigger == 1)',
    'passM'   : '(Probe_passM == 1 && Probe_isGenMatched == 1)',
    'passMP'  : '(Probe_passMP == 1 && Probe_isGenMatched == 1)',
    'passMultiIsoL'       : '(Probe_passMultiIsoL == 1 && Probe_isGenMatched == 1)',
    'passMultiIsoM'       : '(Probe_passMultiIsoM == 1 && Probe_isGenMatched == 1)',
    'passMultiIsoM2017'   : '(Probe_passMultiIsoM2017 == 1 && Probe_isGenMatched == 1)',
    'passMultiIsoM2017v2' : '(Probe_passMultiIsoM2017v2 == 1 && Probe_isGenMatched == 1)',
    'passMiniIsoL'       :  '(Probe_passMiniIsoL == 1 && Probe_isGenMatched == 1)',
    'passMiniIsoM'       :  '(Probe_passMiniIsoM == 1 && Probe_isGenMatched == 1)',
    'passMiniIsoT'       :  '(Probe_passMiniIsoT == 1 && Probe_isGenMatched == 1)',
    'passMiniIsoVT'      :  '(Probe_passMiniIsoVT == 1 && Probe_isGenMatched == 1)',
    'passRelIsoT'         : '(Probe_passRelIsoT == 1 && Probe_isGenMatched == 1)',
    }

#baseOutDir = 'results/withData/test_rf67/eta_pu/' #eta_pt, eta_pu
baseOutDir = 'results/withData/run3_2023/eta_pt/'
#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef_MVAid as tnpSamples
tnpTreeDir = './'#tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.test['data'].clone(),
    'mcNom'  : tnpSamples.test['DY'].clone(),
    'mcAlt'  : tnpSamples.test['DY'].clone(),
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
weightName = 'puWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_06152018/2018Data_1/PU/DY_madgraph_2018_30p_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.9, 2.4]},#[0.9, 1.2, 2.1, 2.4] },#[0,2.4]},#
   { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [10,20,30,40,50,60,80,120] },
   #{ 'var' : 'TnP_npvsGood' , 'type': 'float', 'bins': [0,10,20,25,30,35,40,45,60] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'Tag_pt > 10 && abs(Tag_eta) < 2.4 && Probe_pt > 10 && abs(Probe_eta) < 2.4'# && Probe_pfIsoId>=4 && Tag_pfIsoId>=4'
#cutBase = "TnP_trigger && Tag_pt > 26 && abs(Tag_eta) < 2.4 && Tag_iso < 0.15 && Probe_pt > 20 && abs(Probe_eta) < 2.4 && Probe_passL && Probe_charge*Tag_charge < 0 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched"
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
    ]
'''
#bin 01
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[70.,40.,90.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[-6,-8.,8.]","betaF[0.04,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    ]
'''
'''
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[50.,30.,90.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[-6,-8.,8.]","betaF[0.04,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    ]
'''
'''
#bin 01
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,0.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[50.,30.,90.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[-6,-8.,10.]","betaF[0.05,0.01,0.05]","gammaF[0.1, -1, 2]","peakF[90.0]",
    ]
'''
tnpParNomFit = [ #duplicated
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[50.,30.,90.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,190.]","betaF[0.04,0.001,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
    
