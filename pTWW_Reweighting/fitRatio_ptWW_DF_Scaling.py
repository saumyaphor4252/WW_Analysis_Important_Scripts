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
    
    if args.jet in ("0j","1j","2j"):
        ptWW_bin = "pTWW"

    rfile2018 = ROOT.TFile.Open("../../Full2018_v9/inclusive/rootFile/plots_WW2018_v9_incl.root", "READ")   
    
    histo2018DY = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DY")
    histo2018DATA = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DATA")
    histo2018WW = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_B0")
    histo2018WWnf = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_nonfid")
    histo2018ggWW = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_B0")
    histo2018ggWWnf = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2018WWewk = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WWewk")
    histo2018Vg = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Vg")
    histo2018WZ = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WZ")
    histo2018ZZ = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ZZ")
    histo2018VVV = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_VVV")
    histo2018Higgs = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Higgs")
    histo2018top = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_top")
    histo2018Fake_em = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_em")
    histo2018Fake_me = rfile2018.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_me")

    #if not histo2018DATA:
    #    print("ERROR: Data histogram not found.")
    #    exit(1)
    print("Before scaling:", histo2018top.Integral())
	
    if args.jet == "0j":
        histo2018top.Scale(0.995)
    if args.jet == "1j":
        histo2018top.Scale(0.940)
    if args.jet == "2j":
        histo2018top.Scale(1.028)

    print("After scaling:", histo2018top.Integral())

    # subtract other processes than top
    histo2018DATA.Add(histo2018DY, -1)
    histo2018DATA.Add(histo2018WW, -1)
    histo2018DATA.Add(histo2018WWnf, -1)
    histo2018DATA.Add(histo2018ggWW, -1)
    histo2018DATA.Add(histo2018ggWWnf, -1)
    histo2018DATA.Add(histo2018WWewk, -1)
    histo2018DATA.Add(histo2018Vg, -1)
    histo2018DATA.Add(histo2018WZ, -1)
    histo2018DATA.Add(histo2018ZZ, -1)
    histo2018DATA.Add(histo2018VVV, -1)
    histo2018DATA.Add(histo2018Higgs, -1)
    histo2018DATA.Add(histo2018Fake_em, -1)
    histo2018DATA.Add(histo2018Fake_me, -1)

    # 2017
    rfile2017 = ROOT.TFile.Open("../../Full2017_v9/inclusive/rootFile/plots_WW2017_v9_incl.root", "READ")   
    
    histo2017DY = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DY")
    histo2017DATA = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DATA")
    histo2017WW = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_B0")
    histo2017WWnf = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_nonfid")
    histo2017ggWW = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_B0")
    histo2017ggWWnf = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2017WWewk = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WWewk")
    histo2017Vg = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Vg")
    histo2017WZ = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WZ")
    histo2017ZZ = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ZZ")
    histo2017VVV = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_VVV")
    histo2017Higgs = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Higgs")
    histo2017top = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_top")
    histo2017Fake_em = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_em")
    histo2017Fake_me = rfile2017.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2017top.Scale(0.859)
    if args.jet == "1j":
        histo2017top.Scale(0.919)
    if args.jet == "2j":
        histo2017top.Scale(1.037)

    # subtract other processes than top
    histo2018DATA.Add(histo2017DATA)
    histo2018top.Add(histo2017top)
    histo2018DATA.Add(histo2017DY, -1)
    histo2018DATA.Add(histo2017WW, -1)
    histo2018DATA.Add(histo2017WWnf, -1)
    histo2018DATA.Add(histo2017ggWW, -1)
    histo2018DATA.Add(histo2017ggWWnf, -1)
    histo2018DATA.Add(histo2017WWewk, -1)
    histo2018DATA.Add(histo2017Vg, -1)
    histo2018DATA.Add(histo2017WZ, -1)
    histo2018DATA.Add(histo2017ZZ, -1)
    histo2018DATA.Add(histo2017VVV, -1)
    histo2018DATA.Add(histo2017Higgs, -1)
    histo2018DATA.Add(histo2017Fake_em, -1)
    histo2018DATA.Add(histo2017Fake_me, -1)

    # 2016_HIPM
    rfile2016HIPM = ROOT.TFile.Open("../../Full2016_HIPM_v9/inclusive/rootFile/plots_WW2016_HIPM_v9_incl.root", "READ")   
    
    histo2016HIPMDY = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DY")
    histo2016HIPMDATA = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DATA")
    histo2016HIPMWW = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_B0")
    histo2016HIPMWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_nonfid")
    histo2016HIPMggWW = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_B0")
    histo2016HIPMggWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2016HIPMWWewk = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WWewk")
    histo2016HIPMVg = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Vg")
    histo2016HIPMWZ = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WZ")
    histo2016HIPMZZ = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ZZ")
    histo2016HIPMVVV = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_VVV")
    histo2016HIPMHiggs = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Higgs")
    histo2016HIPMtop = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_top")
    histo2016HIPMFake_em = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_em")
    histo2016HIPMFake_me = rfile2016HIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2016HIPMtop.Scale(0.836)
    if args.jet == "1j":
        histo2016HIPMtop.Scale(0.917)
    if args.jet == "2j":
        histo2016HIPMtop.Scale(0.987)
    
    # subtract other processes than top
    histo2018DATA.Add(histo2016HIPMDATA)
    histo2018top.Add(histo2016HIPMtop)
    histo2018DATA.Add(histo2016HIPMDY, -1)
    histo2018DATA.Add(histo2016HIPMWW, -1)
    histo2018DATA.Add(histo2016HIPMWWnf, -1)
    histo2018DATA.Add(histo2016HIPMggWW, -1)
    histo2018DATA.Add(histo2016HIPMggWWnf, -1)
    histo2018DATA.Add(histo2016HIPMWWewk, -1)
    histo2018DATA.Add(histo2016HIPMVg, -1)
    histo2018DATA.Add(histo2016HIPMWZ, -1)
    histo2018DATA.Add(histo2016HIPMZZ, -1)
    histo2018DATA.Add(histo2016HIPMVVV, -1)
    histo2018DATA.Add(histo2016HIPMHiggs, -1)
    histo2018DATA.Add(histo2016HIPMFake_em, -1)
    histo2018DATA.Add(histo2016HIPMFake_me, -1)


    # 2016_noHIPM
    rfile2016noHIPM = ROOT.TFile.Open("../../Full2016_noHIPM_v9/inclusive/rootFile/plots_WW2016_noHIPM_v9_incl.root", "READ")   
    
    histo2016noHIPMDY = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DY")
    histo2016noHIPMDATA = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_DATA")
    histo2016noHIPMWW = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_B0")
    histo2016noHIPMWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WW_nonfid")
    histo2016noHIPMggWW = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_B0")
    histo2016noHIPMggWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2016noHIPMWWewk = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WWewk")
    histo2016noHIPMVg = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Vg")
    histo2016noHIPMWZ = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_WZ")
    histo2016noHIPMZZ = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_ZZ")
    histo2016noHIPMVVV = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_VVV")
    histo2016noHIPMHiggs = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Higgs")
    histo2016noHIPMtop = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_top")
    histo2016noHIPMFake_em = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_em")
    histo2016noHIPMFake_me = rfile2016noHIPM.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2016noHIPMtop.Scale(0.890)
    if args.jet == "1j":
        histo2016noHIPMtop.Scale(0.912)
    if args.jet == "2j":
        histo2016noHIPMtop.Scale(1.007)
    
    # subtract other processes than top
    histo2018DATA.Add(histo2016noHIPMDATA)
    histo2018top.Add(histo2016noHIPMtop)
    histo2018DATA.Add(histo2016noHIPMDY, -1)
    histo2018DATA.Add(histo2016noHIPMWW, -1)
    histo2018DATA.Add(histo2016noHIPMWWnf, -1)
    histo2018DATA.Add(histo2016noHIPMggWW, -1)
    histo2018DATA.Add(histo2016noHIPMggWWnf, -1)
    histo2018DATA.Add(histo2016noHIPMWWewk, -1)
    histo2018DATA.Add(histo2016noHIPMVg, -1)
    histo2018DATA.Add(histo2016noHIPMWZ, -1)
    histo2018DATA.Add(histo2016noHIPMZZ, -1)
    histo2018DATA.Add(histo2016noHIPMVVV, -1)
    histo2018DATA.Add(histo2016noHIPMHiggs, -1)
    histo2018DATA.Add(histo2016noHIPMFake_em, -1)
    histo2018DATA.Add(histo2016noHIPMFake_me, -1)


    # normalize to 1.
    histo2018DATA.Scale(1./histo2018DATA.Integral())
    histo2018top.Scale(1./histo2018top.Integral())
    
    histo2018top.GetXaxis().SetTitle("pTWW [GeV]")
    histo2018top.GetYaxis().SetTitle("Fraction of events")
    histo2018top.SetStats(0)

    histo2018DATA.SetMarkerStyle(20)
    histo2018DATA.SetLineColor(ROOT.kBlack)
    histo2018top.SetLineWidth(3)
    histo2018top.SetLineColor(2)

    histo2018DATA.SetMaximum(2)
    histo2018DATA.SetMinimum(1e-6)
    histo2018top.SetMaximum(2)
    histo2018top.SetMinimum(1e-6)

    histo2018DATA.Divide(histo2018top)

    #    tf1 = ROOT.TF1("tf1","pol11",30,700) # 1j
    if args.jet in ("0j","1j","2j"):
        tf1 = ROOT.TF1("tf1","pol6",0,200) # 0j pol6
        histo2018DATA.Fit("tf1", "", "", 0, 200)	
        tf2 = ROOT.TF1("tf2","pol6",0,150) # 0j pol10
        histo2018DATA.Fit("tf2", "", "", 0, 150)
        tf3 = ROOT.TF1("tf3","[0]*x+[1]",0, 100) # 0j pol1
        histo2018DATA.Fit("tf3", "", "", 0, 100)
        histo2018DATA.Draw()
        tf1.SetLineColor(ROOT.kRed)
        tf1.Draw("same")
        tf2.SetLineColor(ROOT.kGreen)
        tf2.Draw("same")
        tf3.SetLineColor(ROOT.kBlue)
        tf3.Draw("same")
        canvas.SaveAs('ratio_plots/ratio_' + args.jet  +  '.png')
        canvas.SaveAs('ratio_plots/ratio_' + args.jet  +  '.C')

    rfile2018.Close()
    rfile2017.Close()
    rfile2016HIPM.Close()
    rfile2016noHIPM.Close()
