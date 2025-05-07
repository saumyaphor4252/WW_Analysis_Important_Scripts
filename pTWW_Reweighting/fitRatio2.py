import ROOT
import argparse
import os
import shutil
import glob
import math
import array 

# python fitRatio.py
ROOT.gROOT.SetBatch(True) 
ROOT.gStyle.SetOptStat(0);
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Receive the parameters")
    args = parser.parse_args()

    canvas = ROOT.TCanvas("c1","c1",50,50,800,600)
    canvas.cd()
    
    rfile = ROOT.TFile.Open("histograms_postfit/rootFiles__WWCR_0j__ptll__patched.root", "READ")   

    histoDATA = rfile.Get("WWCR_0j/ptll/histo_DATA")
    histoDY = rfile.Get("WWCR_0j/ptll/histo_DY")
    histoWW = rfile.Get("WWCR_0j/ptll/histo_WW")
    histoqqHSBI = rfile.Get("WWCR_0j/ptll/histo_qqH_sand_off")
    histoggHSBI = rfile.Get("WWCR_0j/ptll/histo_ggH_sand_off")
    histoVg = rfile.Get("WWCR_0j/ptll/histo_Vg")
    histoWZ = rfile.Get("WWCR_0j/ptll/histo_WZ")
    histoZZ = rfile.Get("WWCR_0j/ptll/histo_ZZ")
    histoVVV = rfile.Get("WWCR_0j/ptll/histo_VVV")
    histoHiggs = rfile.Get("WWCR_0j/ptll/histo_Higgs")
    histotop = rfile.Get("WWCR_0j/ptll/histo_top")
    histoFake_em = rfile.Get("WWCR_0j/ptll/histo_Fake_em")
    histoFake_me = rfile.Get("WWCR_0j/ptll/histo_Fake_me")
    
    # subtract other processes than EE
    histoDATA.Add(histoDY, -1)
    histoDATA.Add(histoqqHSBI, -1)
    histoDATA.Add(histoggHSBI, -1)
    histoDATA.Add(histoVg, -1)
    histoDATA.Add(histoWZ, -1)
    histoDATA.Add(histoZZ, -1)
    histoDATA.Add(histoVVV, -1)
    histoDATA.Add(histoHiggs, -1)
    histoDATA.Add(histotop, -1)
    histoDATA.Add(histoFake_em, -1)
    histoDATA.Add(histoFake_me, -1)


    # merge bins
    binning = array.array('d', [30, 43.5, 57, 70.5, 84, 151.5, 300])
    histoDATA_rebinned = histoDATA.Rebin(6,"histoDATA_rebinned",binning)
    histoWW_rebinned = histoWW.Rebin(6,"histoWW_rebinned",binning)
    
    # normalize to 1.
    histoDATA_rebinned.Scale(1./histoDATA_rebinned.Integral())
    histoWW_rebinned.Scale(1./histoWW_rebinned.Integral())

    
    histoWW_rebinned.GetXaxis().SetTitle("ptll [GeV]")
    histoWW_rebinned.GetYaxis().SetTitle("Fraction of events")
    histoWW_rebinned.SetStats(0)

    histoDATA_rebinned.SetMarkerStyle(20)
    histoDATA_rebinned.SetLineColor(ROOT.kBlack)
    histoWW_rebinned.SetLineWidth(3)
    histoWW_rebinned.SetLineColor(2)



    histoDATA_rebinned.SetMaximum(2)
    histoDATA_rebinned.SetMinimum(1e-6)
    histoWW_rebinned.SetMaximum(2)
    histoWW_rebinned.SetMinimum(1e-6)

    histoDATA_rebinned.Divide(histoWW_rebinned)


    tf1 = ROOT.TF1("tf1","pol3",30,300)
    histoDATA_rebinned.Fit("tf1", "", "", 30, 300)
    histoDATA_rebinned.Draw()
    tf1.Draw("same")
    canvas.SaveAs('ratio_ptll.png')
