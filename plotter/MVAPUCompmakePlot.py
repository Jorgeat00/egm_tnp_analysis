import ROOT as r 
import collections
import math 
import os
wp='Tight' #'Tight', 'Medium'
folder='full'
#run='run3_golden'
run='run3_2023'
flag='results/withData/%s/%s/eta_pu/passMVAId%s'%(run,folder,wp)
flag2='results/withData/%s/%s/eta_pu/pass%sId'%(run,folder,wp)
#results=open("finalresults/TnP_ttH_muon_2018_2lss/passttH/egammaEffi.txt").readlines()
results=open("%s/egammaEffi.txt"%flag).readlines()
results2=open("%s/egammaEffi.txt"%flag2).readlines()
results_dict=collections.defaultdict(list)
results_dict2=collections.defaultdict(list)

r.gROOT.ProcessLine(".x tdrstyle.cc")
r.gStyle.SetOptStat(0)
r.gStyle.SetOptTitle(0)
r.gROOT.SetBatch(True)

_noDelete={}
def doSpam(text,x1,y1,x2,y2,align=12,fill=False,textSize=0.033,_noDelete={}):
    cmsprel = r.TPaveText(x1,y1,x2,y2,"NDC");
    cmsprel.SetTextSize(textSize);
    cmsprel.SetFillColor(0);
    cmsprel.SetFillStyle(1001 if fill else 0);
    cmsprel.SetLineStyle(2);
    cmsprel.SetLineColor(0);
    cmsprel.SetTextAlign(align);
    cmsprel.SetTextFont(42);
    cmsprel.AddText(text);
    cmsprel.Draw("same");
    _noDelete[text] = cmsprel; ## so it doesn't get deleted by PyROOT                                                                                                   
    return cmsprel


def hypot(a,b):
    return math.sqrt(a**2+b**2)

for lin in results:
    fields= lin.rstrip().split()
    if len(fields) == 4: continue
    eta1=float(fields[0])
    eta2=float(fields[1])
    pt1 =float(fields[2])
    pt2 =float(fields[3])
    eff_data = float(fields[4])
    eff_data_err = float(fields[5])
    eff_mc = float(fields[6])
    eff_mc_err = float(fields[7])

    results_dict[('%2.1f-%2.1f'%(eta1, eta2))].append( (pt1, pt2, eff_data, eff_data_err, eff_mc, eff_mc_err))

for lin in results2:
    fields= lin.rstrip().split()
    if len(fields) == 4: continue
    eta1=float(fields[0])
    eta2=float(fields[1])
    pt1 =float(fields[2])
    pt2 =float(fields[3])
    eff_data = float(fields[4])
    eff_data_err = float(fields[5])
    eff_mc = float(fields[6])
    eff_mc_err = float(fields[7])

    results_dict2[('%2.1f-%2.1f'%(eta1, eta2))].append( (pt1, pt2, eff_data, eff_data_err, eff_mc, eff_mc_err))


for plot in results_dict:
    tokeep=[]
    topSpamSize=1.2
    plotformat = (600,600) 
    height = plotformat[1]+150
    c1 = r.TCanvas("_canvas", '', plotformat[0], height)
    c1.SetWindowSize(plotformat[0] + (plotformat[0] - c1.GetWw()), (plotformat[1]+150 + (plotformat[1]+150 - c1.GetWh())));
    p1 = r.TPad("pad1","pad1",0,0.30,1,1);
    p1.SetTopMargin(p1.GetTopMargin()*topSpamSize);
    p1.SetBottomMargin(0.017)
    p1.SetTopMargin(0.05);
    p1.SetLeftMargin(0.17)
    p1.SetRightMargin(0.05)
    p1.Draw();
    p2 = r.TPad("pad2","pad2",0,0,1,0.3);
    p2.SetTopMargin(p1.GetTopMargin()*topSpamSize)
    p2.SetBottomMargin(0.3);
    p2.SetRightMargin(0.05)
    p2.SetLeftMargin(0.17)
    p2.SetFillStyle(0);
    p2.Draw();
    p1.cd();


    frame=r.TH1F("frame","",1, 0, 70)
    #frame=r.TH1F("frame","",1, 25, 70)
    print(folder)
    if folder == 'full' or folder == '2022' or folder == '2022EE' or folder == 'BPix' or folder == '2023': frame.GetYaxis().SetRangeUser(0.955,1.01)
    #else: frame.GetYaxis().SetRangeUser(0.8,1.1)
    else: frame.GetYaxis().SetRangeUser(0.955,1.01)
    if plot == '0.9-2.4' and wp == 'Tight': frame.GetYaxis().SetRangeUser(0.945,1.01)
    if wp == 'Tight': frame.GetYaxis().SetRangeUser(0.945,1.01)
    frame.GetXaxis().SetTitleFont(42)
    frame.GetXaxis().SetTitleSize(0.06)
    frame.GetXaxis().SetTitleOffset(1.1)
    frame.GetXaxis().SetLabelFont(42)
    frame.GetXaxis().SetLabelSize(0.06)
    frame.GetXaxis().SetLabelOffset(0.007)
    frame.GetYaxis().SetTitleFont(42)
    frame.GetYaxis().SetTitleSize(0.12)
    frame.GetYaxis().SetTitleOffset(2.0)
    frame.GetYaxis().SetLabelFont(42)
    frame.GetYaxis().SetLabelSize(0.12)
    frame.GetYaxis().SetLabelOffset(0.007)
    frame.GetYaxis().SetTitle("Efficiency")
    frame.GetXaxis().SetTitle("Number of vertices")
    frame.GetXaxis().SetNdivisions(510)
    frame.GetYaxis().SetNdivisions(510)
    #frame.GetYaxis().SetNdivisions(2*1000000 + (510%1000000))

    frame.Draw()

    latex=r.TLatex()
    latex.SetTextSize(0.033*1.4);
    latex.SetTextFont(42);

    if plot == '0.0-0.9':
        #latex.DrawLatex(56.,1.003,"Muon |#eta| < 0.9");#56 if the axis begin in 25, 48 otherwise
        latex.DrawLatex(48.,1.003,"Muon |#eta| < 0.9");
    elif plot == '0.9-2.4':
        latex.DrawLatex(48.,1.002,"Muon |#eta| > 0.9");
        #latex.DrawLatex(56.,1.003,"Muon |#eta| > 0.9");
    p2.cd();
    frameratio=r.TH1F("ratioframe","",1, 0, 70)
    #frameratio=r.TH1F("ratioframe","",1, 25, 70)
    frameratio.GetXaxis().SetTitle("Number of vertices")
    frameratio.SetBinError(1,0)
    frameratio.SetBinContent(1,1)
    frameratio.GetYaxis().SetRangeUser(0.98,1.02)
    #frameratio.GetYaxis().SetRangeUser(0.96,1.04)
    if plot == '0.9-2.4' and wp == 'Tight': frameratio.GetYaxis().SetRangeUser(0.96,1.04)
    if plot == '0.9-2.4': frameratio.GetYaxis().SetRangeUser(0.96,1.04)
    frameratio.GetXaxis().SetTitleFont(42)
    frameratio.GetXaxis().SetTitleSize(0.14)
    frameratio.GetXaxis().SetTitleOffset(1.0)
    frameratio.GetXaxis().SetLabelFont(42)
    frameratio.GetXaxis().SetLabelSize(0.12)
    frameratio.GetXaxis().SetLabelOffset(0.015)
    frameratio.GetYaxis().SetNdivisions(502)
    frameratio.GetYaxis().SetTitleFont(42)
    frameratio.GetYaxis().SetTitleSize(0.14)
    #offset = 0.62
    offset = 0.62
    frameratio.GetYaxis().SetTitleOffset(offset)
    frameratio.GetYaxis().SetLabelFont(42)
    frameratio.GetYaxis().SetLabelSize(0.12)#0.14)
    frameratio.GetYaxis().SetLabelOffset(0.01)
    frameratio.GetYaxis().SetDecimals(True) 
    frameratio.GetYaxis().SetTitle("Data/MC")
    frame.GetXaxis().SetLabelOffset(999) ## send them away
    frame.GetXaxis().SetTitleOffset(999) ## in outer space
    frame.GetYaxis().SetTitleSize(0.06)
    #frame.GetYaxis().SetTitleOffset(1.4)
    frame.GetYaxis().SetTitleOffset(1.35)
    frame.GetYaxis().SetLabelSize(0.05)
    frame.GetYaxis().SetLabelOffset(0.007)
    leg=r.TLegend(0.45,0.03,0.94,0.23)
    if wp=='Tight': leg=r.TLegend(0.2,0.770,0.65,0.935)#0.895
    leg.SetLineColor(0)
    leg.SetFillColor(0)
    leg.SetShadowColor(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.05)#45)
    leg.SetFillStyle(0)
    leg.SetLineStyle(0)
    leg2=r.TLegend(0.45,0.03,0.94,0.23)
    if wp=='Tight': leg2=r.TLegend(0.2,0.770,0.65,0.935)
    leg2.SetLineColor(0)
    leg2.SetFillStyle(0)
    leg2.SetLineStyle(0)
    leg2.SetFillColor(0)
    leg2.SetShadowColor(0)
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.05)#45)


    frameratio.Draw()

    gr_data =r.TGraphErrors(len(results_dict[plot]))
    gr_mc   =r.TGraphErrors(len(results_dict[plot]))
    gr_data2 =r.TGraphErrors(len(results_dict[plot]))
    gr_mc2   =r.TGraphErrors(len(results_dict[plot]))
    gr_mc3   =r.TGraphErrors(len(results_dict[plot]))
    gr_mc4   =r.TGraphErrors(len(results_dict[plot]))
    gr_ratio=r.TGraphErrors(len(results_dict[plot]))
    gr_ratio2=r.TGraphErrors(len(results_dict[plot]))
    for point, (pt1, pt2, eff_data, eff_data_err, eff_mc, eff_mc_err) in enumerate(results_dict[plot]):
        gr_data. SetPoint( point, (pt1+pt2)/2, eff_data)
        gr_data. SetPointError(point, (-pt1+pt2)/2, eff_data_err)
        gr_data2. SetPoint( point, (pt1+pt2)/2, results_dict2[plot][point][2])
        gr_data2. SetPointError(point, (-pt1+pt2)/2, results_dict2[plot][point][3])
        gr_mc  . SetPoint( point, (pt1+pt2)/2, eff_mc)
        gr_mc  . SetPointError(point, (-pt1+pt2)/2, eff_mc_err)
        gr_mc2  . SetPoint( point, (pt1+pt2)/2, results_dict2[plot][point][4])
        gr_mc2  . SetPointError(point, (-pt1+pt2)/2, results_dict2[plot][point][5])
        gr_mc3  . SetPoint( point, (pt1+pt2)/2, results_dict2[plot][point][4])
        gr_mc3  . SetPointError(point, (-pt1+pt2)/2, results_dict2[plot][point][5])

        if eff_mc:
            gr_ratio.SetPoint( point, (pt1+pt2)/2, eff_data/eff_mc)
            gr_ratio.SetPointError(point, (-pt1+pt2)/2, hypot( eff_data_err/eff_mc, eff_mc_err * eff_data /eff_mc**2))
            gr_ratio2.SetPoint( point, (pt1+pt2)/2, results_dict2[plot][point][2]/results_dict2[plot][point][4])
            gr_ratio2.SetPointError(point, (-pt1+pt2)/2, hypot( results_dict2[plot][point][3]/results_dict2[plot][point][4], results_dict2[plot][point][5] * results_dict2[plot][point][2] /results_dict2[plot][point][4]**2))

        else:
            gr_ratio.SetPoint( point, (pt1+pt2)/2,0)
            gr_ratio.SetPointError(point, 0, 0)
            gr_ratio2.SetPoint( point, (pt1+pt2)/2,0)
            gr_ratio2.SetPointError(point, 0, 0)
    tokeep.extend([gr_data,gr_mc, gr_ratio,gr_data2,gr_mc2,gr_ratio2])
    p1.cd()
    gr_data.Draw("p,EZ,same")
    gr_mc.Draw("p,EZ,same")
    gr_data2.Draw("p,EZ,same")
    gr_mc2.Draw("p,EZ,same")
    gr_mc.SetLineColor(r.kBlue)
    #gr_mc.SetLineColor(r.kMagenta)
    gr_mc.SetMarkerColor(r.kBlue)
    gr_mc.SetMarkerStyle(24)
    gr_mc.SetMarkerSize(1.5)
    gr_mc2.SetLineColor(r.kRed)
    #gr_mc2.SetLineWidth(2)
    gr_mc2.SetMarkerColor(r.kRed)
    gr_mc2.SetMarkerStyle(26)
    gr_mc2.SetMarkerSize(1.5)

    gr_mc3.SetLineColor(r.kRed)
    gr_mc3.SetMarkerColor(r.kWhite)
    gr_mc3.SetMarkerStyle(22)
    gr_mc3.SetMarkerSize(1.4)
    gr_mc3.Draw("p,EZ,same")
    gr_mc4.SetLineColor(r.kBlue)
    gr_mc4.SetMarkerColor(r.kWhite)
    gr_mc4.SetMarkerSize(1.4)
    gr_mc4.Draw("p,EZ,same")
    
    gr_data.SetLineColor(r.kBlue)
    gr_data.SetMarkerColor(r.kBlue)
    gr_data.SetMarkerStyle(20)
    gr_data.SetMarkerSize(1.5)
    gr_data2.SetLineColor(r.kRed)
    gr_data2.SetMarkerColor(r.kRed)
    gr_data2.SetMarkerStyle(22)
    gr_data2.SetMarkerSize(1.5)

    leg.AddEntry(gr_mc  , 'Muon MVA ID - MC',"lep")
    leg.AddEntry(gr_data, 'Muon MVA ID - Data','lep')
    leg.AddEntry(gr_mc2  , 'Cut-based ID - MC',"lep")
    leg.AddEntry(gr_data2, 'Cut-based ID - Data','lep')
    leg.Draw('same')
    leg2.AddEntry(gr_mc4  , ' ',"lep")
    leg2.AddEntry(gr_data, ' ','')
    leg2.AddEntry(gr_mc3  , ' ',"lep")
    leg2.AddEntry(gr_data2, ' ','')
    leg.Draw('same')
    leg2.Draw('same')
    
    #doSpam('#scale[1.1]{#bf{CMS Preliminary}}',  0.16, .955,0.6, .995, align=12, textSize=0.033*1.5)
    #doSpam('#scale[1.1]{#bf{CMS} #it{Preliminary}}',  0.16, .955,0.6, .995, align=12, textSize=0.033*1.5)
    doSpam('#scale[1.1]{#bf{CMS}} #scale[0.9]{#it{Preliminary}}',  0.16, .955,0.6, .995, align=12, textSize=0.033*1.4)
    if '2022' == folder.split("_")[-1]: doSpam('7.97 fb^{-1} (13.6 TeV)',  0.61, .955,0.99, .995, align=12, textSize=0.033*1.5)
    elif '2022EE' == folder.split("_")[-1]: doSpam('26.3 fb^{-1} (13.6 TeV)',  0.61, .955,0.99, .995, align=12, textSize=0.033*1.5)
    elif folder=='BPix' or 'BPix' == folder.split("_")[0]: doSpam('9.52 fb^{-1} (13.6 TeV)',  0.61, .955,0.99, .995, align=12, textSize=0.033*1.5)
    elif folder == '2023': doSpam('18.0 fb^{-1} (13.6 TeV)',  0.61, .955,0.99, .995, align=12, textSize=0.033*1.5)#17.98
    else: doSpam('27.5 fb^{-1} (13.6 TeV)',  0.61, .955,0.99, .995, align=12, textSize=0.033*1.5)#35.1, 8.62, 26.92 #new 34.3 26.3 7.97
    if wp=='Medium': doSpam('%s WP'%wp,  0.72, .885,0.99, .915, align=12, textSize=0.033*1.5)
    #else: doSpam('%s WP'%wp,  0.77, .855,0.99, .895, align=12, textSize=0.033*1.5)
    else: doSpam('%s WP'%wp,  0.77, .885,0.99, .915, align=12, textSize=0.033*1.5)    

    p2.cd()
    
    gr_ratio.SetLineColor(r.kBlue)
    gr_ratio.SetMarkerColor(r.kBlue)
    gr_ratio.SetMarkerStyle(20)
    gr_ratio.SetMarkerSize(1.5)
    gr_ratio2.SetLineColor(r.kRed)
    gr_ratio2.SetMarkerColor(r.kRed)
    gr_ratio2.SetMarkerStyle(22)
    gr_ratio2.SetMarkerSize(1.5)
    gr_ratio.Draw('p,EZ,same')
    gr_ratio2.Draw('p,EZ,same')
    #folder='BPix_tight_binning'
    if not os.path.exists('./results/%s/%s/'%(run,folder)):
       os.makedirs('./results/%s/%s/'%(run,folder))
       os.makedirs('/eos/user/j/jayllont/www/%s/%s/'%(run,folder))
       os.system('cp /eos/user/j/jayllont/www/index.php /eos/user/j/jayllont/www/%s/%s/'%(run,folder))
    #c1.SaveAs('./results/run3/full_eta/eff_%s_comp%s_MVA_afterAppPr_FR.png'%(plot.replace('.','p'), wp)) #prueba_pos
    #c1.SaveAs('./results/run3/2022/eff_%s_comp%s_MVA_afterAppPr_FR.pdf'%(plot.replace('.','p'), wp))
    c1.SaveAs('./results/%s/%s/eff_%s_comp%s_MVA_PU.png'%(run,folder,plot.replace('.','p'), wp))
    c1.SaveAs('/eos/user/j/jayllont/www/%s/%s/eff_%s_comp%s_MVA_PU.png'%(run,folder,plot.replace('.','p'), wp))
    c1.SaveAs('./results/%s/%s/eff_%s_comp%s_MVA_PU.pdf'%(run,folder,plot.replace('.','p'), wp))

    #folder='BPix' 
                            
