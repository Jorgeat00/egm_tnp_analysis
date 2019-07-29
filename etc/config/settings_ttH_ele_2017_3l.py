#############################################################
########## General settings
#############################################################
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag that defined the numerator
flags = {
    #for sergio's ntuples the '+' so I have used two - signs to make it +
    'passttH'         : '(Probe_pt > 10 && (Probe_hoe<(0.10-0.00*(abs((Probe_deltaEtaSC) - (-Probe_eta))>1.479))) && (Probe_eInvMinusPInv>-0.04)&& (Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479))) && Probe_convVeto &&  Probe_jetBTagDeepFlavB < 0.3033 && Probe_lostHits == 0 && Probe_mvaTTH > 0.8)',
    }

#baseOutDir = 'results/TnP_ttH_ele_2017_3l/'
baseOutDir = 'finalresults/TnP_ttH_ele_2017_3l/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef_ttH_ele_2017 as tnpSamples
tnpTreeDir = './'#tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.test['data'].clone(),
    'mcNom'  : tnpSamples.test['DY'].clone(),
    'mcAlt'  : tnpSamples.test['DY'].clone(),
    'tagSel' : tnpSamples.test['DY'].clone(),
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017C'] )

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
    { 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0, 0.9, 1.2, 2.1, 2.5] },
   { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [10,15,20,25,30,35,40,45,60,80,120]},
   #{ 'var' : 'Probe_pt' , 'type': 'float', 'bins': [20,30,40,50,120] },
   #{ 'var' : 'TnP_ht' , 'type': 'float', 'bins': [30,100,200,300,400,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase = "TnP_trigger && Tag_pt > 26 && abs(Tag_eta) < 2.4 && Tag_iso < 0.15 && Probe_pt > 20 && abs(Probe_eta) < 2.4 && Probe_passL && Probe_charge*Tag_charge < 0 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched"
#cutBase += " && Probe_passMP == 1" # Eff over medium prompt
#sergio's ntuples
cutBase = "TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.5 && Tag_jetRelIso < 0.15 && Probe_charge*Tag_charge < 0 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched && Probe_isGenMatched == 1 && Probe_pt > 7 && abs(Probe_eta) < 2.5 && abs(Probe_dxy)<0.05 && abs(Probe_dz)<0.1 && Probe_miniPFRelIso_all < 0.4 && Probe_sip3d < 8  && Probe_mvaFall17V2noIso_WPL"

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',

}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    #"meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,90.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    #bin 11
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,110.]","betaP[0.05,0.01,0.1]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,110.]","betaF[0.05,0.01,0.1]","gammaF[0.1, -2, 2]","peakF[90.0]",
    #bin 11
    "meanP[0.0,-5.0,5.0]","sigmaP[0.4,0.2,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    "acmsP[90.,50.,110.]","betaP[0.05,0.01,0.1]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[90.,50.,110.]","betaF[0.05,0.01,0.1]","gammaF[0.1, -2, 2]","peakF[90.0]",
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
        
