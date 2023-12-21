import math

class efficiency:
    #    altEff = [-1]*7
    iAltBkgModel = 0
    iAltSigModel = 1
    iAltMCSignal = 2
    iAltTagSelec = 3
    iPUup        = 4
    iPUdown      = 5
    iAltFitRange = 6

    def __init__(self,abin):
        self.ptBin   = abin
        self.effData = -1
        self.effMC   = -1
        self.altEff  = [-1]*7
        self.syst    = [-1]*7
    
    def __init__(self,ptBin,etaBin,effData,errEffData,effMC,errEffMC,effAltBkgModel,effAltSigModel,effAltMCSignal,effAltTagSel):
        self.ptBin      = ptBin
        self.etaBin     = etaBin
        self.effData    = effData
        self.effMC      = effMC
        self.errEffData = errEffData        
        self.errEffMC   = errEffMC
        self.altEff = [-1]*7
        self.syst   = [-1]*9
        self.altEff[self.iAltBkgModel] = effAltBkgModel
        self.altEff[self.iAltSigModel] = effAltSigModel
        self.altEff[self.iAltMCSignal] = effAltMCSignal
        self.altEff[self.iAltTagSelec] = effAltTagSel

    def __str__(self):
        return '%2.3f\t%2.3f\t%2.1f\t%2.1f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f' % (self.etaBin[0],self.etaBin[1],
                                                                                                       self.ptBin[0] ,self.ptBin[1] ,
                                                                                                       self.effData, self.errEffData, self.effMC, self.errEffMC,
                                                                                                       self.altEff[0],self.altEff[1], self.altEff[2], self.altEff[3] )

    @staticmethod
    def getSystematicNames():
        return [ 'statData', 'statMC', 'altBkgModel', 'altSignalModel', 'altMCEff', 'altTagSelection' ]



    def combineSyst(self,averageEffData,averageEffMC):
        #print '------ Combining Systematics ---------'
        systAltBkg      = self.altEff[self.iAltBkgModel] - averageEffData
        systAltSig      = self.altEff[self.iAltSigModel] - averageEffData
        systAltMC       = self.altEff[self.iAltMCSignal] - averageEffMC
#        systAltMC       = self.altEff[self.iAltMCSignal] - averageEffData
#        systAltTagSelec = self.altEff[self.iAltTagSelec] - averageEffData
        systAltTagSelec = self.altEff[self.iAltTagSelec] - averageEffMC

        if self.altEff[self.iAltBkgModel] < 0:
            systAltBkg = 0

        if self.altEff[self.iAltSigModel] < 0:
            systAltSig = 0

        if self.altEff[self.iAltMCSignal] < 0:
            systAltMC = 0
        
        if self.altEff[self.iAltTagSelec] < 0:
            systAltTagSelec = 0

        self.syst[ 0                 ] = self.errEffData
        self.syst[ 1                 ] = self.errEffMC
        self.syst[self.iAltBkgModel+2] = systAltBkg
        self.syst[self.iAltSigModel+2] = systAltSig
        self.syst[self.iAltMCSignal+2] = systAltMC
        self.syst[self.iAltTagSelec+2] = systAltTagSelec
        
        self.systCombined = 0
        #stat. com suggestion, if stat unc > syst. unc use only stat.
        #for isyst in range(6):
        #    print 'Error syst: %s,%1.3f'%(isyst,self.syst[isyst])
        self.statunc = self.syst[0]*self.syst[0]+self.syst[1]*self.syst[1];
        self.systunc = self.syst[2]*self.syst[2]+self.syst[3]*self.syst[3]+self.syst[4]*self.syst[4]+self.syst[5]*self.syst[5];
        if math.sqrt(self.statunc) > math.sqrt(self.systunc):
            self.systCombined = math.sqrt(self.statunc);
        else:
            for isyst in range(6):
                self.systCombined += self.syst[isyst]*self.syst[isyst];
                #print 'Error syst: %s,%1.3f'%(isyst,self.syst[isyst])
            #print '**********************'
            #print 'systAltMC %1.3f, averageEffMC %1.3f'%(systAltMC, averageEffMC) 
            #print '**********************'
            #print 'errEffData      : %1.3f'%(self.syst[0])
            #print 'errEffMC        : %1.3f'%(self.syst[1])
            #print 'systAltBkg      : %1.3f'%(self.syst[2])
            #print 'systAltSig      : %1.3f'%(self.syst[3])
            #print '>>> systAltMC       : %1.3f'%(self.syst[4])
            #print 'systAltTagSelec : %1.3f'%(self.syst[5])
            
            self.systCombined = math.sqrt(self.systCombined)
        print 'Combined error: %1.3f, averageEffData %1.3f, averageEffMC, %1.3f'%(self.systCombined,averageEffData,averageEffMC)
        print 'Stat unc.: %1.5f, syst. unc. %1.5f '%( math.sqrt(self.statunc),  math.sqrt(self.systunc))


    def __add__(self,eff):
        if self.effData < 0 :
            return eff.deepcopy()
        if eff.effData < 0 :
            return self.deepcopy()
        
        ptbin  = self.ptBin
        etabin = self.etaBin
        errData2 = 1.0 / (1.0/(self.errEffData*self.errEffData)+1.0/(eff.errEffData*eff.errEffData))
        wData1   = 1.0 / (self.errEffData * self.errEffData) * errData2
        wData2   = 1.0 / (eff .errEffData * eff .errEffData) * errData2
        newEffData      = wData1 * self.effData + wData2 * eff.effData;
        newErrEffData   = math.sqrt(errData2)
        
        #        errMC2 = 1.0 / (1.0/(self.errEffMC*self.errEffMC)+1.0/(eff.errEffMC*eff.errEffMC))
        #wMC1   = 1.0 / (self.errEffMC * self.errEffMC) * errMC2
        #wMC2   = 1.0 / (eff .errEffMC * eff .errEffMC) * errMC2
        newEffMC      = wData1 * self.effMC + wData2 * eff.effMC;
        newErrEffMC   = 0.00001#math.sqrt(errMC2)

        newEffAltBkgModel = wData1 * self.altEff[self.iAltBkgModel] + wData2 * eff.altEff[self.iAltBkgModel]
        newEffAltSigModel = wData1 * self.altEff[self.iAltSigModel] + wData2 * eff.altEff[self.iAltSigModel]
        newEffAltMCSignal = wData1 * self.altEff[self.iAltMCSignal] + wData2 * eff.altEff[self.iAltMCSignal]
        newEffAltTagSelec = wData1 * self.altEff[self.iAltTagSelec] + wData2 * eff.altEff[self.iAltTagSelec]

        effout = efficiency(ptbin,etabin,newEffData,newErrEffData,newEffMC,newErrEffMC,newEffAltBkgModel,newEffAltSigModel,newEffAltMCSignal,newEffAltTagSelec)
        return effout
    


import ROOT as rt
import numpy as np
from array import array

def makeTGraphFromList( listOfEfficiencies , keyMin, keyMax ):
    grOut = rt.TGraphErrors(len(listOfEfficiencies))
    
    ip = 0
    for point in listOfEfficiencies:
        grOut.SetPoint(     ip, (point[keyMin]+point[keyMax])/2. , point['val'] )
        grOut.SetPointError(ip, (point[keyMax]-point[keyMin])/2. , point['err'] )
        ip = ip + 1

    #    print "###########################"
    #    print listOfEff
    #    grOut.Print()
    return grOut



class efficiencyList: 
    effList = {}

    def __init__(self):
        self.effList = {}

    
    def __str__(self):
        outStr = ''
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                outStr += str(self.effList[ptBin][etaBin])
                outStr += '\n'
        return outStr

    
    def addEfficiency( self, eff ):
        if not self.effList.has_key(eff.ptBin):
            self.effList[eff.ptBin] = {}
        self.effList[eff.ptBin][eff.etaBin] = eff

    def combineSyst(self):
        #print '**** inside  combineSyst ****'
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if etaBin[0] >= 0 and etaBin[1] >= 0:
                    etaBinPlus  = etaBin
                    #print 'etaBin[0] = ',etaBin[0], ' etaBin[1] = ', etaBin[1], ' etaBinPlus ', etaBinPlus 
                    #etaBinMinus = (-etaBin[1],-etaBin[0])
                    
                    effPlus  = self.effList[ptBin][etaBinPlus]
                    effMinus = None
                    #if self.effList[ptBin].has_key(etaBinMinus):
                    #    effMinus =  self.effList[ptBin][etaBinMinus] 
                    
                    if effMinus is None:
                        #print " ---- efficiencyList: I did not find MINUS eta bin!!!"
                        pass
                        
                    else:                        
                        #averageData = (effPlus.effData + effMinus.effData)/2.
                        #averageMC   = (effPlus.effMC   + effMinus.effMC  )/2.
                        averageData = effPlus.effData
                        averageMC   = effPlus.effMC
                        #self.effList[ptBin][etaBinMinus].combineSyst(averageData,averageMC)
                        self.effList[ptBin][etaBinPlus ].combineSyst(averageData,averageMC)
#                        self.effList[ptBin][etaBinMinus].combineSyst(effMinus.effData,effMinus.effMC)
#                        self.effList[ptBin][etaBinPlus ].combineSyst(effPlus.effData,effPlus.effMC)
                        print 'syst 1 [-] (etaBin: %1.3f,%1.3f) ; (ptBin: %3.0f,%3.0f): %f '% (etaBin[0],etaBin[1],ptBin[0],ptBin[1],self.effList[ptBin][etaBinMinus].syst[1])
                        print 'syst 1 [+] (etaBin: %1.3f,%1.3f) ; (ptBin: %3.0f,%3.0f): %f '% (etaBin[0],etaBin[1],ptBin[0],ptBin[1],self.effList[ptBin][etaBinPlus] .syst[1])
                        

                        
    def symmetrizeSystVsEta(self):
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if etaBin[0] >= 0 and etaBin[1] > 0:
                    etaBinPlus  = etaBin
                    #etaBinMinus = (-etaBin[1],-etaBin[0])
                    
                    effPlus  = self.effList[ptBin][etaBinPlus]
                    effMinus = None
                    #if self.effList[ptBin].has_key(etaBinMinus):
                    #    effMinus =  self.effList[ptBin][etaBinMinus] 

                    if effMinus is None:
                        #self.effList[ptBin][etaBinMinus] = effPlus
                        #print " ---- efficiencyList: I did not find -eta bin!!!"
                        pass
                    else:
                        #### fix statistical errors if needed
                        if    effPlus.errEffData <= 0.00001 and effMinus.errEffData > 0.00001: 
                            self.effList[ptBin][etaBinPlus ].errEffData = effMinus.errEffData
                        #elif effMinus.errEffData <= 0.00001 and effPlus .errEffData > 0.00001: 
                        #    self.effList[ptBin][etaBinMinus].errEffData = effPlus.errEffData
                        else:
                        #    self.effList[ptBin][etaBinMinus].errEffData = (effMinus.errEffData+effPlus.errEffData)/2.
                            self.effList[ptBin][etaBinPlus ].errEffData = (effPlus.errEffData)

                        #if   effPlus.errEffMC <= 0.00001 and effMinus.errEffMC > 0.00001: 
                        #    self.effList[ptBin][etaBinPlus ].errEffMC = effMinus.errEffMC
                        #elif effMinus.errEffMC <= 0.00001 and effPlus.errEffMC > 0.00001: 
                        #    self.effList[ptBin][etaBinMinus].errEffMC = effPlus.errEffMC
                        #else:
                            #self.effList[ptBin][etaBinMinus].errEffMC = (effMinus.errEffMC+effPlus.errEffMC)/2.
                            #self.effList[ptBin][etaBinPlus ].errEffMC = (effPlus.errEffMC)
                        self.effList[ptBin][etaBinPlus ].errEffMC = (effPlus.errEffMC)

                            
                        for isyst in range(4):
                            #if abs(effPlus.altEff[isyst] - effMinus.altEff[isyst]) < 0.10:
                            if abs(effPlus.altEff[isyst]) < 0.10:
                                #averageSyst = (effPlus.altEff[isyst] +  effMinus.altEff[isyst]) / 2
                                averageSyst = (effPlus.altEff[isyst])
                                self.effList[ptBin][etaBinPlus ].altEff[isyst] = averageSyst
                                #self.effList[ptBin][etaBinMinus].altEff[isyst] = averageSyst
                            else:
                                #averageSyst = (effPlus.altEff[isyst] +  effMinus.altEff[isyst]) / 2
                                averageSyst = (effPlus.altEff[isyst])
                                print "issue, I am averaging but the efficiencies are quite different in 2 etaBins"
                                print " --- syst: ", isyst
                                print str(self.effList[ptBin][etaBinPlus ])
                                #print str(self.effList[ptBin][etaBinMinus])
                                print "   eff[+] = ",  self.effList[ptBin][etaBinPlus ].altEff[isyst]
                                #print "   eff[-] = ",  self.effList[ptBin][etaBinMinus].altEff[isyst]                                
                                self.effList[ptBin][etaBinPlus ].altEff[isyst] = averageSyst
                                #self.effList[ptBin][etaBinMinus].altEff[isyst] = averageSyst

    def ptEtaScaleFactor_2DHisto(self, onlyError, relError = False):
        print 'Entering the function...'
#        self.symmetrizeSystVsEta()
        #self.combineSyst()

        ### first define bining
        xbins = []
        ybins = []
        for ptBin in self.effList.keys():
            if not ptBin[0] in ybins:
                ybins.append(ptBin[0])                
            if not ptBin[1] in ybins:
                ybins.append(ptBin[1])

            for etaBin in self.effList[ptBin].keys():
                if not etaBin[0] in xbins:
                    xbins.append(etaBin[0])                
                if not etaBin[1] in xbins:
                    xbins.append(etaBin[1])

        xbins.sort()
        ybins.sort()
        print 'xbins ', xbins
        print 'ybins ', ybins
        ## transform to numpy array for ROOT
        xbinsTab = np.array(xbins)
        ybinsTab = np.array(ybins)
        #xbinsTab = array('f',xbins)
        #ybinsTab = array('f',ybins)
        #xbinsTab = xbins
        #ybinsTab = ybins

        htitle = '#mu scale factors'
        hname  = 'h2_scaleFactorsMuon' 
        if onlyError >= 0:
            htitle = 'uncertainties'
            hname  = 'h2_uncertaintiesMuon'             
        if onlyError == -3:
            htitle = 'Data eff'
            hname  = 'h2_dataeff' 
        if onlyError == -2:
            htitle = 'MC eff'
            hname  = 'h2_MCeff' 
        if onlyError == -1:
            htitle = 'Scale Factors'
            hname  = 'h2_scaleFactors' 


        #import os
        print 'hname = ', hname
        print 'htitle = ', htitle
        print 'xbinsTab = ', xbinsTab
        print 'ybinsTab = ', ybinsTab
        print 'xbins = ', xbins
        print 'ybins = ', ybins
        print 'xxxx len(xbinsTab) = ',len(xbinsTab)-1
        print 'xxxx len(ybinsTab) = ',len(ybinsTab)-1
        print 'xxxx len(xbins) = ',len(xbins)
        print 'xxxx len(ybins) = ',len(ybins)
        #h2dd = rt.TH2F(hname,htitle,xbinsTab.size-1,xbinsTab,ybinsTab.size-1,ybinsTab)
        #h2 = rt.TH2F(hname,htitle,xbinsTab.size-1,xbinsTab,ybinsTab.size-1,ybinsTab)
        h2 = rt.TH2F(hname,htitle,  len(xbinsTab)-1 , xbinsTab, len(ybinsTab)-1,ybinsTab)
        #h2 = rt.TH2F(hname,htitle,  len(xbins)-1 , xbins[0], xbins[len(xbins)-1], len(ybins)-1,ybins[0], ybins[len(ybins)-1])

        print 'Llega!!!'
        ## init histogram efficiencies and errors to 100%
        for ix in range(1,h2.GetXaxis().GetNbins()+1):
            for iy in range(1,h2.GetYaxis().GetNbins()+1):
                h2.SetBinContent(ix,iy, 1)
                h2.SetBinError  (ix,iy, 1)
        
        for ix in range(1,h2.GetXaxis().GetNbins()+1):
            for iy in range(1,h2.GetYaxis().GetNbins()+1):
                print 'Checking Bins (ix, iy: %1.3f,%1.3f))'% (ix,iy)
                for ptBin in self.effList.keys():
                    if h2.GetYaxis().GetBinLowEdge(iy) < ptBin[0] or h2.GetYaxis().GetBinUpEdge(iy) > ptBin[1]:
                        #print '>>> pT Values: %1.3f,%1.3f,%1.3f,%1.3f '%(h2.GetYaxis().GetBinLowEdge(iy), ptBin[0], h2.GetYaxis().GetBinUpEdge(iy), ptBin[1])
                        continue
                    for etaBin in self.effList[ptBin].keys():
                        if h2.GetXaxis().GetBinLowEdge(ix) < etaBin[0] or h2.GetXaxis().GetBinUpEdge(ix) > etaBin[1]:
                            #print '>>> eta Values: %1.3f,%1.3f,%1.3f,%1.3f '%(h2.GetXaxis().GetBinLowEdge(ix), etaBin[0], h2.GetXaxis().GetBinUpEdge(ix), etaBin[1])
                            continue

                        #print '   Survive checks (ix, iy: %1.3f,%1.3f))'% (ix,iy)

                        ## average MC efficiency
                        etaBinPlus  = etaBin
                        #etaBinMinus = (-etaBin[1],-etaBin[0])
                    
                        effPlus  = self.effList[ptBin][etaBinPlus]
                        effMinus = None
                        #if self.effList[ptBin].has_key(etaBinMinus):
                        #    effMinus =  self.effList[ptBin][etaBinMinus] 

                        averageMC = None
                        #if effMinus is None:
                        averageMC = effPlus.effMC
                        if averageMC== 0:
                            continue
                        if self.effList[ptBin][etaBin].effMC== 0:
                            continue

                        #print " ---- efficiencyList: I did not find -eta bin!!!"
                        #else:                        
                        #    averageMC   = (effPlus.effMC   + effMinus.effMC  )/2.
                        ### so this is h2D bin is inside the bining used by mu POG
                        h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].effData      / self.effList[ptBin][etaBin].effMC)
                        h2.SetBinError  (ix,iy, self.effList[ptBin][etaBin].systCombined / averageMC )
                        if onlyError   == 0 :
                            h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].systCombined      / averageMC  )
                        if   onlyError == -3 :
                            h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].effData      )
                            h2.SetBinError  (ix,iy, self.effList[ptBin][etaBin].systCombined * self.effList[ptBin][etaBin].effMC / averageMC )
                        elif onlyError == -2 :
                            h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].effMC)
                            h2.SetBinError  (ix,iy, 0 )
                        elif onlyError == -1 :
                            h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].effData      / self.effList[ptBin][etaBin].effMC)
                            print 'BinContent (ix, iy: %1.3f,%1.3f) ; (effData, effMC: %1.3f,%1.3f)'% (ix,iy,self.effList[ptBin][etaBin].effData,self.effList[ptBin][etaBin].effMC)
                            h2.SetBinError  (ix,iy, self.effList[ptBin][etaBin].systCombined / averageMC )
                            print 'Error BinContent (ix, iy: %1.3f,%1.3f) ; (systCombined/averageMC: %1.3f)'% (ix,iy,self.effList[ptBin][etaBin].systCombined/averageMC)

                        if onlyError   == 0 :
                                h2.SetBinContent(ix,iy, self.effList[ptBin][etaBin].systCombined      / averageMC  )
                        elif onlyError >= 1 and onlyError <= 6:
                            denominator = averageMC
                            if relError:
                                denominator = self.effList[ptBin][etaBin].systCombined
                            h2.SetBinContent(ix,iy, abs(self.effList[ptBin][etaBin].syst[onlyError-1]) / denominator )

        #h2.GetXaxis().SetTitle("|#eta_{SC}|") #for electrons
        h2.GetXaxis().SetTitle("|#eta|")
        h2.GetYaxis().SetTitle("p_{T} [GeV]")
        return h2
        
                                
    def pt_1DGraph_list(self,  typeGR = 0):
#        self.symmetrizeSystVsEta()
        #print ' --- combinesyst from pt_1DGraph_list --- '
        #self.combineSyst()
        listOfGraphs = {}

        print ' --- loop over pt and eta bins --- '
        loop = 0
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if etaBin[0] >= 0 and etaBin[1] > 0:
                    etaBinPlus  = etaBin
                    #etaBinMinus = (-etaBin[1],-etaBin[0])
                    effPlus  = self.effList[ptBin][etaBinPlus]
                    effMinus = None
                    loop += 1
                    #print ' >>>  Bin Number --- %1.2f'%loop
                    #if self.effList[ptBin].has_key(etaBinMinus):
                    #    effMinus =  self.effList[ptBin][etaBinMinus] 

                    effAverage = effPlus
                    #print ' ---  effAverage effData, %1.2f'%effAverage.effData
                    if effAverage.effMC == 0: 
                        continue
                    if not effMinus is None:
                        effAverage = effPlus + effMinus

                        
                    if not listOfGraphs.has_key(etaBin):                        
                        ### init average efficiency 
                        listOfGraphs[etaBin] = []


                    #print ' --- combinesyst(effAverage.effData,effAverage.effMC) from pt_1DGraph_list --- '
                    effAverage.combineSyst(effAverage.effData,effAverage.effMC)
                    aValue  = effAverage.effData
                    anError = effAverage.systCombined 
                    if typeGR == 1:
                        aValue  = effAverage.effData      / effAverage.effMC
                        anError = effAverage.systCombined / effAverage.effMC  
                    if typeGR == -1:
                        aValue  = effAverage.effMC
                        anError = 0#effAverage.errEffMC
                    
                    listOfGraphs[etaBin].append( {'min': ptBin[0], 'max': ptBin[1],
                                                  'val': aValue  , 'err': anError } ) 
                                                  
                    #print ' ---  typeGR, %1.3f'%typeGR
                    #print ' ---  aValue, %1.3f'%aValue

        return listOfGraphs

    def pt_1DGraph_list_customEtaBining(self, etaBining, doScaleFactor):
#        self.symmetrizeSystVsEta()
        #self.combineSyst()
        listOfGraphs = {}

        for abin in etaBining:
            listOfGraphs[abin] = []
            for ptBin in self.effList.keys():
                for etaBin in self.effList[ptBin].keys():
                    if etaBin[0] >= 0 and etaBin[1] > 0:
                        etaBinPlus  = etaBin
                        #etaBinMinus = (-etaBin[1],-etaBin[0])

                        if abin[0] < etaBin[0] or abin[1] > etaBin[1]:
                            continue
                        #                        if abin[0] >= etaBin[0] and abin[1] <= etaBin[1]:
                        #                            continue
                        effPlus  = self.effList[ptBin][etaBinPlus]
                        effMinus = None
                        #if self.effList[ptBin].has_key(etaBinMinus):
                        #    effMinus =  self.effList[ptBin][etaBinMinus] 

                        effAverage = effPlus
                        if not effMinus is None:
                            effAverage = effPlus + effMinus

                        effAverage.combineSyst(effAverage.effData,effAverage.effMC)
                        aValue  = effAverage.effData
                        anError = effAverage.systCombined 
                        if doScaleFactor :
                            aValue  = effAverage.effData      / effAverage.effMC
                            anError = effAverage.systCombined / effAverage.effMC  
                        listOfGraphs[abin].append( {'min': ptBin[0], 'max': ptBin[1],
                                                    'val': aValue  , 'err': anError } ) 
                                                  
        return listOfGraphs


    
    def eta_1DGraph_list(self, typeGR = 0 ):
#        self.symmetrizeSystVsEta()
        #self.combineSyst()
        listOfGraphs = {}
        
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if not listOfGraphs.has_key(ptBin):                        
                    ### init average efficiency 
                    listOfGraphs[ptBin] = []

                effAverage = self.effList[ptBin][etaBin]
                if effAverage.effMC == 0: 
                    continue

                aValue  = effAverage.effData
                anError = effAverage.systCombined 
                if typeGR == 1:
                    aValue  = effAverage.effData      / effAverage.effMC
                    anError = effAverage.systCombined / effAverage.effMC  
                if typeGR == -1:
                    aValue  = effAverage.effMC
                    anError = 0#effAverage.errEffMC
                    
                listOfGraphs[ptBin].append( {'min': etaBin[0], 'max': etaBin[1],
                                             'val': aValue  , 'err': anError } )

        return listOfGraphs





    
