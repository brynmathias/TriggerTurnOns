#!/usr/bin/env python
# encoding: utf-8
"""
HTEffCombinErrorsUseTurnOnClass.py

Created by Bryn Mathias on 2011-12-12.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from TurnOn import *
import array
r.gROOT.SetBatch(True) # suppress the creation of canvases on the screen.. much much faster if over a remote connection

def main():
  text = ""

  sums ={


"HT275AlphaT":([
  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v12",
  
],"./HT275.root"),

"HT325AlphaT":([
  "HT325_HLT_HT300_AlphaT0p53_v1_HLT_IsoMu24_eta2p1_v11",
  "HT325_HLT_HT300_AlphaT0p53_v1_HLT_IsoMu24_eta2p1_v12",
  "HT325_HLT_HT300_AlphaT0p53_v2_HLT_IsoMu24_eta2p1_v11",
  "HT325_HLT_HT300_AlphaT0p53_v2_HLT_IsoMu24_eta2p1_v12",
  "HT325_HLT_HT300_AlphaT0p53_v3_HLT_IsoMu24_eta2p1_v11",
  "HT325_HLT_HT300_AlphaT0p53_v3_HLT_IsoMu24_eta2p1_v12",
  
],"./HT325.root"),

"HT375AlphaT":([
  "HT375_HLT_HT350_AlphaT0p52_v1_HLT_IsoMu24_eta2p1_v11",
  "HT375_HLT_HT350_AlphaT0p52_v1_HLT_IsoMu24_eta2p1_v12",
  "HT375_HLT_HT350_AlphaT0p52_v2_HLT_IsoMu24_eta2p1_v11",
  "HT375_HLT_HT350_AlphaT0p52_v2_HLT_IsoMu24_eta2p1_v12",
  "HT375_HLT_HT350_AlphaT0p52_v3_HLT_IsoMu24_eta2p1_v11",
  "HT375_HLT_HT350_AlphaT0p52_v3_HLT_IsoMu24_eta2p1_v12",
  
  
],"./HT375.root"),


"HT475AlphaT":([
  "HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v11",
  "HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
  "HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v11",
  "HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
  
],"./HT375.root"),


"HT575AlphaT":([
"HT575_HLT_HT450_AlphaT0p51_v7_HLT_IsoMu24_eta2p1_v11",
"HT575_HLT_HT450_AlphaT0p51_v7_HLT_IsoMu24_eta2p1_v12",
"HT575_HLT_HT450_AlphaT0p51_v8_HLT_IsoMu24_eta2p1_v11",
"HT575_HLT_HT450_AlphaT0p51_v8_HLT_IsoMu24_eta2p1_v12",
"HT575_HLT_HT450_AlphaT0p51_v9_HLT_IsoMu24_eta2p1_v11",
"HT575_HLT_HT450_AlphaT0p51_v9_HLT_IsoMu24_eta2p1_v12",
],"./HT375.root"),


"HTCurves":(sorted([
"HLT_HT750_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT750_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT750_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT650_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT650_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT650_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT750_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT750_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT750_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT650_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT650_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT650_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT650_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT650_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT650_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT450_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT450_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT450_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT450_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT450_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT450_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT450_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT450_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT450_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT200_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT200_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT200_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT200_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT200_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT200_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT200_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT200_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT200_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT500_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT500_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT500_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT500_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT500_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT500_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT500_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT500_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT500_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT350_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT350_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT350_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT350_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT350_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT350_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT350_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT350_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT350_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT300_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT300_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT300_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT300_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT300_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT300_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT300_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT300_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT300_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT400_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT400_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT400_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT400_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT400_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT400_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT400_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT400_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT400_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT550_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT550_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT550_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT550_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT550_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT550_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT550_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT550_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT550_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT250_v1_HLT_IsoMu24_eta2p1_v13",
"HLT_HT250_v1_HLT_IsoMu24_eta2p1_v12",
"HLT_HT250_v1_HLT_IsoMu24_eta2p1_v11",
"HLT_HT750_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT750_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT750_v2_HLT_IsoMu24_eta2p1_v11",
"HLT_HT250_v3_HLT_IsoMu24_eta2p1_v13",
"HLT_HT250_v3_HLT_IsoMu24_eta2p1_v12",
"HLT_HT250_v3_HLT_IsoMu24_eta2p1_v11",
"HLT_HT250_v2_HLT_IsoMu24_eta2p1_v13",
"HLT_HT250_v2_HLT_IsoMu24_eta2p1_v12",
"HLT_HT250_v2_HLT_IsoMu24_eta2p1_v11",

]),"HT375.root")


}



  NumsForFinalPlot = []
  for key,Dirs in sorted(sums.iteritems()):
    if"AlphaT" not in key: histList = ("HT_Nom","HT_Denom")
    if"AlphaT" in key: histList = ("AlphaT_Nom","AlphaT_Denom")

    if "AlphaT" in key:axisTitle = "#alpha_{T}"
    else:axisTitle="H_{T}"
    numeratorList = []
    denominatorList = []

    BinEdges = [ 0.3 + 0.01*i for i in range(23)] + [0.55,0.7]
    for Dir in Dirs[0]:
      print Dir
      aNom = GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      aNom.hObj.SetTitle(Dir)
      if "AlphaT" not in key:aNom.Rebin(10,None)
      if "AlphaT" in key: aNom.Rebin(len(BinEdges)-1,BinEdges)
      aNom.HideOverFlow()

      numeratorList.append(aNom)
      aDenom =  GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[1], Col = r.kRed, Norm = None, LegendText = "")
      aDenom.hObj.SetTitle(Dir)

      if "AlphaT" not in key:aDenom.Rebin(10,None)
      if "AlphaT" in key: aDenom.Rebin(len(BinEdges)-1,BinEdges)
      if aNom.hObj.Integral() > aDenom.hObj.Integral(): assert "ERROR You have more entries in your numerator histo than your denominator histogram!!!"
      aDenom.HideOverFlow()
      denominatorList.append(aDenom)
    c1 = Print("./%s_RunAtFNAL.pdf"%(key))
    c1.open()
    DiffNomList = []
    DiffDenomList = []
    CumuNomList = []
    CumuDenomList = []
    for nom,denom in zip(numeratorList,denominatorList):

      if denom.hObj.Integral() > 0.:
        DiffNomList.append(nom.hObj)
        DiffDenomList.append(denom.hObj)
        CumuNomList.append(MakeCumu(nom.hObj))
        CumuDenomList.append(MakeCumu(denom.hObj))
    for a in DiffNomList:

    DiffTurnOn = TurnOn(DiffNomList,DiffDenomList)
    for nom,denom in zip(DiffTurnOn.numerator,DiffTurnOn.denominator):
      if "alpha" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.4f"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,5.)
      if "H_" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.f GeV"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,1000.)

      denom.GetYaxis().SetLabelSize(0.035)
      denom.GetYaxis().SetTitleOffset(1.3)
      denom.Draw("h")
      nom.Draw("psame")
      c1.SetLog('y',True)
      c1.Print()
      c1.SetLog('y',False)
    DiffTurnOn.TotDenominator.SetTitle("Total Differential Hists for %s"%(key))
    if "alpha" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.4f"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,5.)
    if "H_" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.f GeV"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,1000.)
    DiffTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    DiffTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    c1.SetLog('y',True)
    DiffTurnOn.TotDenominator.Draw("h")
    DiffTurnOn.TotNumerator.Draw("psame")
    c1.Print()
    c1.SetLog('y',False)
    for curve in DiffTurnOn.listOfTurnOns:
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,5.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      print "="*25
      print "Differential Turn on for %s"%(Dir)
      print "="*25
      curve.SetTitle()
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetYaxis().SetTitle("Efficiency")
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitleOffset(1.15)
      curve.Draw("ap")
      c1.Print()
    FinalDiff = DiffTurnOn.SumOfTurnOns()
    FinalDiff.SetTitle("Total Differential Turn on for %s"%(key))
    FinalDiff.GetXaxis().SetTitle(axisTitle)
    if"AlphaT" in key: FinalDiff.GetXaxis().SetRangeUser(0.0,2.0)
    else: FinalDiff.GetXaxis().SetRangeUser(0.,1000.)
    FinalDiff.GetYaxis().SetTitle("Efficiency")
    FinalDiff.GetYaxis().SetTitleOffset(1.15)
    FinalDiff.GetXaxis().SetTitleSize(0.045)
    FinalDiff.Draw("ap")
    c1.Print()
    xVal = r.Double(0)
    yVal = r.Double(0)
    point = []
    for gPoint in range(FinalDiff.GetN()):
      FinalDiff.GetPoint(gPoint,xVal,yVal)
      if "AlphaT" in key:
        text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))
      else:text +=("%s at %3.0f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))

    CumuTurnOn = TurnOn(CumuNomList,CumuDenomList)
    for curve in CumuTurnOn.ListOfTurnOns():
      # curve.SetTitle("Cumulative Turn on for %s"%(Dir))
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitle("Cumulative Efficiency")
      curve.GetYaxis().SetTitleOffset(1.15)
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,5.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      curve.Draw("ap")
      c1.Print()
    CumuTurnOn.TotDenominator.SetTitle("Total Cumulative Hists for %s"%(key))
    if "alpha" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.4f"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
      CumuTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,5.)
    if "H_" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.f GeV"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
    CumuTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    CumuTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    CumuTurnOn.TotDenominator.Draw("h")
    CumuTurnOn.TotNumerator.Draw("psame")
    c1.SetLog('y',True)
    c1.Print()
    c1.SetLog('y',False)
    FinalCumu = CumuTurnOn.SumOfTurnOns()
    FinalCumu.SetTitle("Total Cumulative Turn on for %s"%(key))
    FinalCumu.GetXaxis().SetTitle(axisTitle)
    if "AlphaT" in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.4,1.)
        FinalCumu.GetXaxis().SetTitle("#alpha_{T}^{cut}")
    if "AlphaT" not in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.,1000.)
        FinalCumu.GetXaxis().SetTitle("H_{T}^{cut}")
    FinalCumu.GetYaxis().SetTitle("Cumulative Efficiency")
    FinalCumu.GetYaxis().SetTitleOffset(1.15)
    FinalCumu.GetXaxis().SetTitleSize(0.045)
    # c1.SetLog('y',True)
    FinalCumu.Draw("ap")
    c1.Print()
    # c1.SetLog('y',False)
    xVal = r.Double(0)
    yVal = r.Double(0)
    c1.close()

    point = []
    for Point in range(FinalCumu.GetN()):
      FinalCumu.GetPoint(Point,xVal,yVal)
      if "AlphaT" in key:
        if xVal > 0.60:# and xVal < 0.61:
          text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal-0.005,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))
      else:text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))
  textFile = open("text.txt",'w')
  textFile.write(text)

if __name__ == '__main__':
  main()

