#############################################################
########## General settings
#############################################################
# flag that defined the numerator
flags = {
    #'passtight'   : '(Probe_cutBased == 4 && Probe_pt > 35 && abs(Probe_eta) < 2.4 && (abs(Probe_eta-Probe_deltaEtaSC)>1.566 || abs(Probe_eta-Probe_deltaEtaSC) < 1.444) && abs(Probe_dxy) < 0.2 && abs(Probe_dz) < 0.5)',
#    'passtight'         : '(Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& (Probe_hoe < 0.10*(Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479)))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.2783 && Probe_mvaTTHRun3 > 0.8 && (abs(Probe_eta-Probe_deltaEtaSC)>1.566 || abs(Probe_eta-Probe_deltaEtaSC) < 1.444))',
#october 13, 2023
#    'passtight'         : '(Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& (Probe_hoe < 0.10*(Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479)))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.2783 && Probe_mvaTTHRun3 > 0.97 && (abs(Probe_eta-Probe_deltaEtaSC)>1.566 || abs(Probe_eta-Probe_deltaEtaSC) < 1.444))',
#december 4, 2023
#    'passtight'         : '(Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& (Probe_hoe < 0.10*(Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479)))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.3196 && Probe_mvaTTHRun3 > 0.97 && (abs(Probe_eta-(-Probe_deltaEtaSC))>1.566 || abs(Probe_eta-(-Probe_deltaEtaSC)) < 1.444))',
    #'passtight'         : '(Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& (Probe_hoe < 0.10*(Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479)))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.3196 && Probe_mvaTTHRun3 > 0.9 && (abs(Probe_eta-(-Probe_deltaEtaSC))>1.566 || abs(Probe_eta-(-Probe_deltaEtaSC)) < 1.444))',
    #adding IP cuts
    #'passtight'         : 'Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& Probe_hoe < 0.10 && (Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.3196 && Probe_mvaTTHRun3 > 0.9 && (abs(Probe_eta-(-Probe_deltaEtaSC))>1.566 || abs(Probe_eta-(-Probe_deltaEtaSC)) < 1.444) && abs(Probe_eta) < 2.5 && abs(Probe_dxy)<0.05 && abs(Probe_dz)<0.1 && Probe_miniPFRelIso_all < 0.4 && Probe_sip3d < 8',
    #adding chargeID
    'passtight'         : 'Probe_conept > 10 && (Probe_eInvMinusPInv>-0.04)&& Probe_hoe < 0.10 && (Probe_sieie<(0.011-(-0.019)*(abs((Probe_deltaEtaSC)-(-Probe_eta))>1.479))) && Probe_convVeto &&  Probe_lostHits==0 && Probe_jetBTagDeepFlavB < 0.3196 && Probe_mvaTTHRun3 > 0.9 && (abs(Probe_eta-(-Probe_deltaEtaSC))>1.566 || abs(Probe_eta-(-Probe_deltaEtaSC)) < 1.444) && abs(Probe_eta) < 2.5 && abs(Probe_dxy)<0.05 && abs(Probe_dz)<0.1 && Probe_miniPFRelIso_all < 0.4 && Probe_sip3d < 8 &&  Probe_tightCharge == 2',
}
#baseOutDir = 'results_v12/ele_tight_altMC/'
#baseOutDir = 'results_v12_preEE_mva09/ele_recototight/'
baseOutDir = 'results_mvaTTH_2023BPix_alldata/electrons/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
#import etc.inputs.tnpSampleDef_ele_v12_preEE as tnpSamples
import etc.inputs.tnpSampleDef_mvaTTH_ele_BPix as tnpSamples
tnpTreeDir = './'#tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.test['data'].clone(),
    'mcNom'  : tnpSamples.test['DY'].clone(),
    #'mcAlt'  : tnpSamples.test['DY'].clone(),
    'mcAlt'  : tnpSamples.test['DYAlt'].clone(), 
    'tagSel' : tnpSamples.test['DY'].clone(),
}

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

weightName = 'puWeight_fix'
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
    { 'var' : 'abs(Probe_deltaEtaSC - (-Probe_eta))' , 'type': 'float', 'bins': [0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] },
    { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [15,25,30,35,40,45,55,70,100,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'
#cutBase = "TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.4 && Tag_pfRelIso03_all < 0.15 && Probe_pt > 20 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched && Probe_cutBased > 1"
#cutBase = "TnP_trigger && Tag_pt > 37 && abs(Tag_eta) < 2.4 && (abs(Tag_eta-Tag_deltaEtaSC)>1.566 || abs(Tag_eta-Tag_deltaEtaSC) < 1.444) && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched"
#loose
cutBase = "TnP_trigger && Tag_conept > 30 && abs(Tag_eta) < 2.5 && (abs(Tag_deltaEtaSC-(-Tag_eta))>1.566 || abs(Tag_deltaEtaSC-(-Tag_eta)) < 1.444) && Tag_jetRelIso < 0.15 && Probe_charge*Tag_charge < 0 && abs(Tag_dxy) < 0.05 && abs(Tag_dz) < 0.1 && Tag_isGenMatched && Probe_isGenMatched == 1  "
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
    #"meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,90.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    #bin10 #higher efficiency but larger systematics
    #"meanP[0.0,-1.0,1.0]","sigmaP[0.1,0.,5.0]",
    #"meanF[0.5,-5.0,5.0]","sigmaF[0.4,0.2,2.0]",
    #"acmsP[100.,50.,150.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[85.0]",
    #"acmsF[60.,50.,70.]","betaF[0.1,0.01,0.2]","gammaF[0.03, 0.02, 1]","peakF[80.0]",
    #"meanP[-2.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[70.,50.,110.]","betaP[0.05,0.01,0.2]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,90.]","betaF[0.05,0.01,0.2]","gammaF[0.1, -1, 2]","peakF[90.0]",
    #bin05
    #"meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,100.]","betaP[0.4,0.01,1]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[80.,50.,90.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -1, 2]","peakF[90.0]",
    #"meanP[0.0,-1.0,1.0]","sigmaP[0.1,0.,5.0]",
    #"meanF[0.5,-5.0,5.0]","sigmaF[0.4,0.2,2.0]",
    #"acmsP[100.,50.,150.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[85.0]",
    #"acmsF[60.,50.,70.]","betaF[0.1,0.01,0.2]","gammaF[0.03, 0.02, 1]","peakF[80.0]",
    #bin47
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,200.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[70.,50.,80.]","betaF[0.04,0.01,0.05]","gammaF[0.03, 0.01, 0.05]","peakF[90.0]",
    #bin01 #better result but larger uncertainty
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,5.0]",
    #"acmsP[60.,50.,150.]","betaP[0.05,0.005,0.07]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,100.]","betaF[0.1,0.01,0.2]","gammaF[0.5, 0.02, 1]","peakF[90.0]",
    "meanP[0.0,-4.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[1,0.2,5.0]",
    "acmsP[60.,50.,150.]","betaP[0.3,0.005,1.2]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,100.]","betaF[0.3,0.01,0.6]","gammaF[0.2, 0.031, 0.5]","peakF[90.0]",
    #bin00 #better result but does not converge
    #"meanP[-1.0,-2.0,2.0]","sigmaP[1.2,0.5,2.0]",
    #"meanF[-1.0,-2.0,2.0]","sigmaF[0.8,0.1,2.0]",
    #"acmsP[80.,50.,150.]","betaP[0.05,0.005,0.2]","gammaP[0.1, -2, 1.5]","peakP[90.0]",
    #"acmsF[80.,50.,200.]","betaF[0.1,0.01,0.3]","gammaF[0.5, 0.02, 0.9]","peakF[80.0]",
    

    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin05
    #"meanP[0.5,-1.0,1.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.4,0.1,0.5]",
    #"meanF[-0.4.,-1.0,1.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.4,0.1,0.5]",
    #"acmsP[25.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[25.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    #bin01
    #"meanP[0.0,-5.0,5.0]","sigmaP[0.9,0.5,2.0]","alphaP[2.0,1.,3.]" ,'nP[1,-5,5]',"sigmaP_2[1.5,0.5,2.0]","sosP[1,0.5,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[0.4,0.2,2.0]","alphaF[2.0,1.,3.]",'nF[1,-5,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[1,0.5,5.0]",
    #"acmsP[60.,50.,180.]","betaP[0.1,0.005,1.0]","gammaP[1.3, 0.1, 1.5]","peakP[95.0]",
    #"acmsF[60.,50.,100.]","betaF[0.1,0.01,0.2]","gammaF[0.1, 0.005, 1.5]","peakF[90.0]",
    #bin00
    #"meanP[-1.0,-3.0,3.0]","sigmaP[2,0.5,5.0]","alphaP[2.0,1.,3.]" ,'nP[1,-5,5]',"sigmaP_2[1.5,0.5,2.0]","sosP[1,0.5,2.0]",
    #"meanF[0.0,-3.0,3.0]","sigmaF[0.4,0.2,5.0]","alphaF[2.0,1.,3.]",'nF[1,-5,5]',"sigmaF_2[1.0,0.5,3.0]","sosF[2,0.5,3.0]",
    #"acmsP[80.,50.,150.]","betaP[0.1,0.09,0.2]","gammaP[1, 0.1, 1.5]","peakP[90.0]",
    #"acmsF[80.,50.,200.]","betaF[0.15,0.01,0.2]","gammaF[0.1, 0.005, 1.5]","peakF[90.0]",
    #bin10
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,3.0]",
    #"meanF[-0.4,-4.0,3.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1.0,0.5,3.0]",
    #"acmsP[60.,50.,100.]","betaP[0.04,0.01,0.5]","gammaP[0.1, 0.005, 1]","peakP[70.0]",
    #"acmsF[75.,60.,110.]","betaF[0.04,0.03,0.7]","gammaF[0.2, 0.001, 1]","peakF[90.0]",
    #bin08 #with meanF [-0.1,-3.0,2-0] the efficency is higher but also the uncertainty
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,5.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,5.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.4]","gammaP[0.05, -0.1, 2.0]","peakP[95.0]",
    #"acmsF[75.,50.,120.]","betaF[0.06,0.003,0.2]","gammaF[0.02, 0.005, 1]","peakF[95.0]",
    #bin47
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,2.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,3.0]","sosP[0.5,-0.1,3.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,3.0]","sosF[0.2,-0.1,3.0]",
    #"acmsP[75.,50.,110.]","betaP[0.9,0.001,2.0]","gammaP[0.05, -0.1, 2.0]","peakP[95.0]",
    #"acmsF[75.,50.,120.]","betaF[0.06,0.003,0.2]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin 47 (2)
    #"meanP[0.5,-2.0,2.0]","sigmaP[0.5,0.1,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.2,-2.0,2.0]","sigmaF[0.5,0.1,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.1,0.01,5.0]",
    #"acmsP[75.,30.,120.]","betaP[0.2,0.01,2]","gammaP[0.1, -4, 4]","peakP[90.0]",
    #"acmsF[75.,30.,200.]","betaF[0.2,0.01,0.5]","gammaF[0.1, -2, 2]","peakF[90.0]",
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,5.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[2,0.5,5.0]",
    #"acmsP[60.,50.,90.]","betaP[0.04,0.01,1.2]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[50.,40.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.3, 0.005, 1]","peakF[90.0]",
    #bin46
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[2,0.5,5.0]",
    #"acmsP[60.,50.,90.]","betaP[0.04,0.01,0.3]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[50.,40.,90.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    
    #bin23
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #bin17 ok
    #"meanP[-2.0,-5.0,5.0]","sigmaP[1,0.7,3.0]","alphaP[2.0,1.2,3.5]" ,'nP[2,-2,5]',"sigmaP_2[1.5,0.5,4.0]","sosP[0.01,0.0,3.0]",
    #"meanF[-2.0,-4.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.5]",'nF[2,-2,5]',"sigmaF_2[2.0,0.5,4.0]","sosF[2,0.01,3.0]",
    #"acmsP[70.,50.,120.]","betaP[0.5,0.001,0.9]","gammaP[0.05, 0.04, 2.0]","peakP[90.0]",
    #"acmsF[90.,70.,120.]","betaF[0.08,0.01,1.5]","gammaF[0.06, 0.01, 0.1]","peakF[90.0]",

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
    #bin40
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,0.1,5.0]",
    #"meanF[-0.1,-0.5,0.5]","sigmaF[0.2,0.1,1.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[1.2,0.1,5.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[95.0]",
    #"acmsF[50.,30.,120.]","betaF[0.06,0.003,0.1]","gammaF[0.2, 0.005, 1]","peakF[90.0]",
    #bin8,9,10
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,5.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,5.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[95.0]",
    #"acmsF[75.,50.,120.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[95.0]",
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
    #"meanP[-0.0,-3.0,3.0]","sigmaP[0.5,0.0,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[0.5,0.01,5.0]","sosP[0.5,-1.0,5.0]",
    #"meanF[0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,2.0]",
    #"acmsP[90.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.5, 0.1, 2]","peakP[89.0]",
    #"acmsF[196.,170.,220.]","betaF[0.05,0.01,0.06]","gammaF[0.5, 0.01, 1]","peakF[90.0]",
    #bin5
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,3.5]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,0.1,0.5]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.01,0.1]","gammaP[1.0, 0.1, 5.0]","peakP[90.0]",
    #"acmsF[75.,50.,150.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin4
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,5.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,0.1,0.2]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.01,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[90.0]",
    #"acmsF[75.,50.,150.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[88.0]",
    #bin2
    #"meanP[-0.3,-2.0,2.0]","sigmaP[0.2,0.01,1.0]","alphaP[2.0,0.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.01,6.0]","sosP[0.5,-0.1,1.0]",
    #"meanF[-0.1,-2.0,2.0]","sigmaF[1.0,0.1,4.0]", "alphaF[2.0,0.2,3.5]", 'nF[3,-5,5]',"sigmaF_2[2.0,0.01,6.0]","sosF[0.2,-0.1,1.0]",
    #"acmsP[75.,50.,110.]","betaP[0.04,0.001,0.1]","gammaP[0.05, -0.1, 1.0]","peakP[90.0]",
    #"acmsF[75.,50.,110.]","betaF[0.06,0.003,0.08]","gammaF[0.02, 0.005, 1]","peakF[90.0]",
    #bin4 0.68, bin 19 and bin 22
    #"meanP[0.2,-2.0,2.0]","sigmaP[0.5,0.1,5.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[0.2,-2.0,2.0]","sigmaF[0.5,0.1,1.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"acmsP[75.,50.,100.]","betaP[0.06,0.01,0.2]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[75.,50.,80.]","betaF[0.06,0.01,0.2]","gammaF[0.1, -2, 2]","peakF[90.0]",
    
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
    #"meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    #"alphaP[0.,-5.,5.]",
    #"alphaF[0.,-5.,5.]",
    #bin05
    #"meanP[0.75,-5.0,5.0]","sigmaP[0.2,0.01,2.0]",
    #"meanF[0.5,-5.0,5.0]","sigmaF[2,0.1,3.0]",
    #"alphaP[0.3,-2,2.0]",
    #"alphaF[0.1,-2,2]",
    #bin10
    #"meanP[0.0,-1.0,1.0]","sigmaP[0.9,0.1,2.0]",
    #"meanF[0.0,-0.7,0.2]","sigmaF[0.2,0.1,1.0]",
    #"alphaP[0.,-1.,2.]",
    #"alphaF[0.,-0.1,0.1]",
    #bin01 #keeps being too low
    #"meanP[2.,-1.0,3.0]","sigmaP[0.1,0.01,0.5]",
    #"meanF[1,-3.0,3.0]","sigmaF[0.71,0.7,3]",
    #"alphaP[0.3,-0.5,0.5]",
    #"alphaF[-1.7,-3.,3.]",
    #bin10
    #"meanP[0.3,-1.0,2.0]","sigmaP[0.5,0.1,2.0]",
    #"meanF[0.1,-2.0,2.0]","sigmaF[1,-2.0,3]",
    #"alphaP[0.5,-1.5,2.0]",
    #"alphaF[-0.0,-1.5,1.5]",
    #bin47
    #"meanP[1.0,-3.0,3.0]","sigmaP[0.2,0.01,2.0]",
    #"meanF[0.5,-3.0,3.0]","sigmaF[2,0.1,3.0]",
    #"alphaP[0.9,-2,2.0]",
    #"alphaF[1,-2,2]",
    "meanP[2.0,-1.0,5.0]","sigmaP[0.2,0.01,1.0]",
    "meanF[-0.5,-1.0,1.0]","sigmaF[0.8,0.1,1.0]",
    "alphaP[-0.9,-1.0,0.001]",
    "alphaF[0.5,-0.01,1]",
    
    #bin2
    #"meanP[0.0,-1.0,1.0]","sigmaP[0.9,0.1,1.0]",
    #"meanF[0.0,-0.2,0.2]","sigmaF[0.2,0.1,1.0]",
    #"alphaP[0.,-1.,1.]",
    #"alphaF[0.,-0.1,0.1]",

    #bin17
    #"meanP[-0.5,-1.0,1.0]","sigmaP[0.2,0.1,1.5]",
    #"meanF[0.0,-1.0,1.0]","sigmaF[0.2,0.1,1.5]",
    #"alphaP[-0.2,-0.5,0.5]",
    #"alphaF[-0.1,-1.,1.]",

    #bin10
    #"meanP[0.3,-1.0,5.0]","sigmaP[0.2,0.1,1.0]",
    #"meanF[0.1,-5.0,5.0]","sigmaF[0.5,-2.0,0.6]",
    #"alphaP[-0.2,-0.5,0.5]",
    #"alphaF[0.0,-1.0,5.]",
    ]
        
