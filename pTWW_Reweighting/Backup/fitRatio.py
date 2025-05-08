import ROOT
import argparse
import os
import shutil
import glob
import math

# python fitRatio.py --jet 1j
ROOT.gROOT.SetBatch(True) 
ROOT.gStyle.SetOptStat(0);
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--jet', action = 'store', type = str, dest = 'jet', help = '')
    args = parser.parse_args()

    canvas = ROOT.TCanvas("c1","c1",50,50,800,600)
    canvas.cd()
    
    if args.jet == "0j":
        ptllbin = "ptll1"
    elif args.jet == "1j":
        ptllbin = "ptll3"
    elif args.jet == "2j":
        ptllbin = "ptll5"

    rfile2018 = ROOT.TFile.Open("Full2018_v9/inclusive_SF_Zpt/rootFile/plots_WW2018_v9_incl_sf.root", "READ")   
    
    histo2018DY = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DY")
    histo2018DATA = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DATA")
    histo2018WW = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_B0")
    histo2018WWnf = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_nonfid")
    histo2018ggWW = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_B0")
    histo2018ggWWnf = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_nonfid")
    histo2018Vg = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Vg")
    histo2018WZ = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WZ")
    histo2018ZZ = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ZZ")
    histo2018VVV = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_VVV")
    histo2018Higgs = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Higgs")
    histo2018top = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_top")
    histo2018Fake_ee = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_ee")
    histo2018Fake_mm = rfile2018.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_mm")
    
    # subtract other processes than DY
    histo2018DATA.Add(histo2018WW, -1)
    histo2018DATA.Add(histo2018WWnf, -1)
    histo2018DATA.Add(histo2018ggWW, -1)
    histo2018DATA.Add(histo2018ggWWnf, -1)
    histo2018DATA.Add(histo2018Vg, -1)
    histo2018DATA.Add(histo2018WZ, -1)
    histo2018DATA.Add(histo2018ZZ, -1)
    histo2018DATA.Add(histo2018VVV, -1)
    histo2018DATA.Add(histo2018Higgs, -1)
    histo2018DATA.Add(histo2018top, -1)
    histo2018DATA.Add(histo2018Fake_ee, -1)
    histo2018DATA.Add(histo2018Fake_mm, -1)


    # 2017

    rfile2017 = ROOT.TFile.Open("Full2017_v9/inclusive_SF_Zpt/rootFile/plots_WW2017_v9_incl_sf.root", "READ")   
    
    histo2017DY = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DY")
    histo2017DATA = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DATA")
    histo2017WW = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_B0")
    histo2017WWnf = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_nonfid")
    histo2017ggWW = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_B0")
    histo2017ggWWnf = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_nonfid")
    histo2017Vg = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Vg")
    histo2017WZ = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WZ")
    histo2017ZZ = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ZZ")
    histo2017VVV = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_VVV")
    histo2017Higgs = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Higgs")
    histo2017top = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_top")
    histo2017Fake_ee = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_ee")
    histo2017Fake_mm = rfile2017.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_mm")
    
    # subtract other processes than DY
    histo2018DATA.Add(histo2017DATA)
    histo2018DY.Add(histo2017DY)
    histo2018DATA.Add(histo2017WW, -1)
    histo2018DATA.Add(histo2017WWnf, -1)
    histo2018DATA.Add(histo2017ggWW, -1)
    histo2018DATA.Add(histo2017ggWWnf, -1)
    histo2018DATA.Add(histo2017Vg, -1)
    histo2018DATA.Add(histo2017WZ, -1)
    histo2018DATA.Add(histo2017ZZ, -1)
    histo2018DATA.Add(histo2017VVV, -1)
    histo2018DATA.Add(histo2017Higgs, -1)
    histo2018DATA.Add(histo2017top, -1)
    histo2018DATA.Add(histo2017Fake_ee, -1)
    histo2018DATA.Add(histo2017Fake_mm, -1)


    # 2016_HIPM

    rfile2016HIPM = ROOT.TFile.Open("Full2016_HIPM_v9/inclusive_SF_Zpt/rootFile/plots_WW2016_HIPM_v9_incl_sf.root", "READ")   
    
    histo2016HIPMDY = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DY")
    histo2016HIPMDATA = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DATA")
    histo2016HIPMWW = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_B0")
    histo2016HIPMWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_nonfid")
    histo2016HIPMggWW = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_B0")
    histo2016HIPMggWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_nonfid")
    histo2016HIPMVg = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Vg")
    histo2016HIPMWZ = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WZ")
    histo2016HIPMZZ = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ZZ")
    histo2016HIPMVVV = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_VVV")
    histo2016HIPMHiggs = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Higgs")
    histo2016HIPMtop = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_top")
    histo2016HIPMFake_ee = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_ee")
    histo2016HIPMFake_mm = rfile2016HIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_mm")
    
    # subtract other processes than DY
    histo2018DATA.Add(histo2016HIPMDATA)
    histo2018DY.Add(histo2016HIPMDY)
    histo2018DATA.Add(histo2016HIPMWW, -1)
    histo2018DATA.Add(histo2016HIPMWWnf, -1)
    histo2018DATA.Add(histo2016HIPMggWW, -1)
    histo2018DATA.Add(histo2016HIPMggWWnf, -1)
    histo2018DATA.Add(histo2016HIPMVg, -1)
    histo2018DATA.Add(histo2016HIPMWZ, -1)
    histo2018DATA.Add(histo2016HIPMZZ, -1)
    histo2018DATA.Add(histo2016HIPMVVV, -1)
    histo2018DATA.Add(histo2016HIPMHiggs, -1)
    histo2018DATA.Add(histo2016HIPMtop, -1)
    histo2018DATA.Add(histo2016HIPMFake_ee, -1)
    histo2018DATA.Add(histo2016HIPMFake_mm, -1)


    # 2016_noHIPM

    rfile2016noHIPM = ROOT.TFile.Open("Full2016_noHIPM_v9/inclusive_SF_Zpt/rootFile/plots_WW2016_noHIPM_v9_incl_sf.root", "READ")   
    
    histo2016noHIPMDY = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DY")
    histo2016noHIPMDATA = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_DATA")
    histo2016noHIPMWW = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_B0")
    histo2016noHIPMWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WW_nonfid")
    histo2016noHIPMggWW = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_B0")
    histo2016noHIPMggWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ggWW_nonfid")
    histo2016noHIPMVg = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Vg")
    histo2016noHIPMWZ = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_WZ")
    histo2016noHIPMZZ = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_ZZ")
    histo2016noHIPMVVV = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_VVV")
    histo2016noHIPMHiggs = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Higgs")
    histo2016noHIPMtop = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_top")
    histo2016noHIPMFake_ee = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_ee")
    histo2016noHIPMFake_mm = rfile2016noHIPM.Get("ww2l2v_13TeV_DYCR_" + args.jet + "_B0/" + ptllbin + "/histo_Fake_mm")
    
    # subtract other processes than DY
    histo2018DATA.Add(histo2016noHIPMDATA)
    histo2018DY.Add(histo2016noHIPMDY)
    histo2018DATA.Add(histo2016noHIPMWW, -1)
    histo2018DATA.Add(histo2016noHIPMWWnf, -1)
    histo2018DATA.Add(histo2016noHIPMggWW, -1)
    histo2018DATA.Add(histo2016noHIPMggWWnf, -1)
    histo2018DATA.Add(histo2016noHIPMVg, -1)
    histo2018DATA.Add(histo2016noHIPMWZ, -1)
    histo2018DATA.Add(histo2016noHIPMZZ, -1)
    histo2018DATA.Add(histo2016noHIPMVVV, -1)
    histo2018DATA.Add(histo2016noHIPMHiggs, -1)
    histo2018DATA.Add(histo2016noHIPMtop, -1)
    histo2018DATA.Add(histo2016noHIPMFake_ee, -1)
    histo2018DATA.Add(histo2016noHIPMFake_mm, -1)









    # normalize to 1.
    histo2018DATA.Scale(1./histo2018DATA.Integral())
    histo2018DY.Scale(1./histo2018DY.Integral())

    
    histo2018DY.GetXaxis().SetTitle("ptll [GeV]")
    histo2018DY.GetYaxis().SetTitle("Fraction of events")
    histo2018DY.SetStats(0)

    histo2018DATA.SetMarkerStyle(20)
    histo2018DATA.SetLineColor(ROOT.kBlack)
    histo2018DY.SetLineWidth(3)
    histo2018DY.SetLineColor(2)



    histo2018DATA.SetMaximum(2)
    histo2018DATA.SetMinimum(1e-6)
    histo2018DY.SetMaximum(2)
    histo2018DY.SetMinimum(1e-6)

    histo2018DATA.Divide(histo2018DY)


    #    tf1 = ROOT.TF1("tf1","pol11",30,700) # 1j
    if args.jet == "0j":
        tf1 = ROOT.TF1("tf1","pol6",30,200) # 2j
        histo2018DATA.Fit("tf1", "", "", 30, 200)
        histo2018DATA.Draw()
        tf1.Draw("same")
    else:
        tf1 = ROOT.TF1("tf1","pol6",30,150) # 2j #pol10
        histo2018DATA.Fit("tf1", "", "", 30, 150)
        tf2 = ROOT.TF1("tf2","[0]*x+[1]",150,400) # 2j #pol10
        histo2018DATA.Fit("tf2", "", "", 150, 400)
        histo2018DATA.Draw()
        tf1.Draw("same")
        tf2.Draw("same")
    canvas.SaveAs('ratio_plots/ratio_' + args.jet  +  '.png')
