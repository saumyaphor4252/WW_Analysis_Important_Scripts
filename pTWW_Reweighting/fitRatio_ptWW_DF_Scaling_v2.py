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
    
    histo2018DY = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DY")
    histo2018DATA = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DATA")
    histo2018WW = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_B0")
    histo2018WWnf = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_nonfid")
    histo2018ggWW = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_B0")
    histo2018ggWWnf = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2018WWewk = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WWewk")
    histo2018Vg = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Vg")
    histo2018WZ = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WZ")
    histo2018ZZ = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ZZ")
    histo2018VVV = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_VVV")
    histo2018Higgs = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Higgs")
    histo2018top = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_top")
    histo2018Fake_em = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_em")
    histo2018Fake_me = rfile2018.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_me")

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
    histoMC_Bg = histo2018DY.Clone("MC - Bacground")
#    histoMC_Bg.Add(histo2018WW)
    histoMC_Bg.Add(histo2018WWnf)
#    histoMC_Bg.Add(histo2018ggWW)
    histoMC_Bg.Add(histo2018ggWWnf)
    histoMC_Bg.Add(histo2018WWewk)
    histoMC_Bg.Add(histo2018Vg)
    histoMC_Bg.Add(histo2018WZ)
    histoMC_Bg.Add(histo2018ZZ)
    histoMC_Bg.Add(histo2018VVV)
    histoMC_Bg.Add(histo2018Higgs)
    histoMC_Bg.Add(histo2018top)
    histoMC_Bg.Add(histo2018Fake_em)
    histoMC_Bg.Add(histo2018Fake_me)

    # 2017
    rfile2017 = ROOT.TFile.Open("../../Full2017_v9/inclusive/rootFile/plots_WW2017_v9_incl.root", "READ")   
    
    histo2017DY = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DY")
    histo2017DATA = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DATA")
    histo2017WW = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_B0")
    histo2017WWnf = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_nonfid")
    histo2017ggWW = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_B0")
    histo2017ggWWnf = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2017WWewk = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WWewk")
    histo2017Vg = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Vg")
    histo2017WZ = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WZ")
    histo2017ZZ = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ZZ")
    histo2017VVV = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_VVV")
    histo2017Higgs = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Higgs")
    histo2017top = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_top")
    histo2017Fake_em = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_em")
    histo2017Fake_me = rfile2017.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2017top.Scale(0.859)
    if args.jet == "1j":
        histo2017top.Scale(0.919)
    if args.jet == "2j":
        histo2017top.Scale(1.037)

    # subtract other processes than top
    histo2018DATA.Add(histo2017DATA)
    histoMC_Bg.Add(histo2017DY)
#    histoMC_Bg.Add(histo2017WW)
    histoMC_Bg.Add(histo2017WWnf)
#   histoMC_Bg.Add(histo2017ggWW)
    histoMC_Bg.Add(histo2017ggWWnf)
    histoMC_Bg.Add(histo2017WWewk)
    histoMC_Bg.Add(histo2017Vg)
    histoMC_Bg.Add(histo2017WZ)
    histoMC_Bg.Add(histo2017ZZ)
    histoMC_Bg.Add(histo2017VVV)
    histoMC_Bg.Add(histo2017Higgs)
    histoMC_Bg.Add(histo2017top)
    histoMC_Bg.Add(histo2017Fake_em)
    histoMC_Bg.Add(histo2017Fake_me)

    # 2016_HIPM
    rfile2016HIPM = ROOT.TFile.Open("../../Full2016_HIPM_v9/inclusive/rootFile/plots_WW2016_HIPM_v9_incl.root", "READ")   
    
    histo2016HIPMDY = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DY")
    histo2016HIPMDATA = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DATA")
    histo2016HIPMWW = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_B0")
    histo2016HIPMWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_nonfid")
    histo2016HIPMggWW = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_B0")
    histo2016HIPMggWWnf = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2016HIPMWWewk = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WWewk")
    histo2016HIPMVg = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Vg")
    histo2016HIPMWZ = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WZ")
    histo2016HIPMZZ = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ZZ")
    histo2016HIPMVVV = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_VVV")
    histo2016HIPMHiggs = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Higgs")
    histo2016HIPMtop = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_top")
    histo2016HIPMFake_em = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_em")
    histo2016HIPMFake_me = rfile2016HIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2016HIPMtop.Scale(0.836)
    if args.jet == "1j":
        histo2016HIPMtop.Scale(0.917)
    if args.jet == "2j":
        histo2016HIPMtop.Scale(0.987)
    
    # subtract other processes than top
    histo2018DATA.Add(histo2016HIPMDATA)
    histoMC_Bg.Add(histo2016HIPMDY)
#    histoMC_Bg.Add(histo2016HIPMWW)
    histoMC_Bg.Add(histo2016HIPMWWnf)
#    histoMC_Bg.Add(histo2016HIPMggWW)
    histoMC_Bg.Add(histo2016HIPMggWWnf)
    histoMC_Bg.Add(histo2016HIPMWWewk)
    histoMC_Bg.Add(histo2016HIPMVg)
    histoMC_Bg.Add(histo2016HIPMWZ)
    histoMC_Bg.Add(histo2016HIPMZZ)
    histoMC_Bg.Add(histo2016HIPMVVV)
    histoMC_Bg.Add(histo2016HIPMHiggs)
    histoMC_Bg.Add(histo2016HIPMtop)
    histoMC_Bg.Add(histo2016HIPMFake_em)
    histoMC_Bg.Add(histo2016HIPMFake_me)


    # 2016_noHIPM
    rfile2016noHIPM = ROOT.TFile.Open("../../Full2016_noHIPM_v9/inclusive/rootFile/plots_WW2016_noHIPM_v9_incl.root", "READ")   
    
    histo2016noHIPMDY = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DY")
    histo2016noHIPMDATA = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_DATA")
    histo2016noHIPMWW = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_B0")
    histo2016noHIPMWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WW_nonfid")
    histo2016noHIPMggWW = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_B0")
    histo2016noHIPMggWWnf = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ggWW_nonfid")
    histo2016noHIPMWWewk = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WWewk")
    histo2016noHIPMVg = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Vg")
    histo2016noHIPMWZ = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_WZ")
    histo2016noHIPMZZ = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_ZZ")
    histo2016noHIPMVVV = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_VVV")
    histo2016noHIPMHiggs = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Higgs")
    histo2016noHIPMtop = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_top")
    histo2016noHIPMFake_em = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_em")
    histo2016noHIPMFake_me = rfile2016noHIPM.Get("ww2l2v_13TeV_sr_" + args.jet + "_B0/" + ptWW_bin + "/histo_Fake_me")

    if args.jet == "0j":
        histo2016noHIPMtop.Scale(0.890)
    if args.jet == "1j":
        histo2016noHIPMtop.Scale(0.912)
    if args.jet == "2j":
        histo2016noHIPMtop.Scale(1.007)
    
    # subtract other processes than top
    histo2018DATA.Add(histo2016noHIPMDATA)
    histoMC_Bg.Add(histo2016noHIPMDY)
#    histoMC_Bg.Add(histo2016noHIPMWW)
    histoMC_Bg.Add(histo2016noHIPMWWnf)
#    histoMC_Bg.Add(histo2016noHIPMggWW)
    histoMC_Bg.Add(histo2016noHIPMggWWnf)
    histoMC_Bg.Add(histo2016noHIPMWWewk)
    histoMC_Bg.Add(histo2016noHIPMVg)
    histoMC_Bg.Add(histo2016noHIPMWZ)
    histoMC_Bg.Add(histo2016noHIPMZZ)
    histoMC_Bg.Add(histo2016noHIPMVVV)
    histoMC_Bg.Add(histo2016noHIPMHiggs)
    histoMC_Bg.Add(histo2016noHIPMtop)	
    histoMC_Bg.Add(histo2016noHIPMFake_em)
    histoMC_Bg.Add(histo2016noHIPMFake_me)

    # merge bins
    new_binning = array.array('d', [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 200])
    histo2018DATA_rebinned = histo2018DATA.Rebin(6,"histoDATA_rebinned",new_binning)
    histoMC_Bg_rebinned = histoMC_Bg.Rebin(6,"histoMC_Bg_rebinned",new_binning)

    # normalize to 1.
    histo2018DATA.Scale(1./histo2018DATA.Integral())
    histoMC_Bg.Scale(1./histoMC_Bg.Integral())
    
    histoMC_Bg.GetXaxis().SetTitle("pTWW [GeV]")
    histoMC_Bg.GetYaxis().SetTitle("Fraction of events")
    histoMC_Bg.SetStats(0)

    histo2018DATA.SetMarkerStyle(20)
    histo2018DATA.SetLineColor(ROOT.kBlack)
    histoMC_Bg.SetLineWidth(3)
    histoMC_Bg.SetLineColor(2)

    histo2018DATA.SetMaximum(2)
    histo2018DATA.SetMinimum(1e-6)
    histoMC_Bg.SetMaximum(2)
    histoMC_Bg.SetMinimum(1e-6)

    histo2018DATA.Divide(histoMC_Bg)

    #    tf1 = ROOT.TF1("tf1","pol11",30,700) # 1j
    if args.jet in ("0j","1j","2j"):
        tf1 = ROOT.TF1("tf1","pol1",0,200) # 0j pol6
        histo2018DATA.Fit("tf1", "", "", 0, 200)
        tf2 = ROOT.TF1("tf2","pol2",0,200) # 0j pol10
        histo2018DATA.Fit("tf2", "", "", 0, 200)
        tf3 = ROOT.TF1("tf3","pol3",0, 200) # 0j pol1
        histo2018DATA.Fit("tf3", "", "", 0, 200)
        tf4 = ROOT.TF1("tf4","pol4",0, 200) # 0j pol1
        histo2018DATA.Fit("tf4", "", "", 0, 200)
        tf5 = ROOT.TF1("tf5","pol5",0, 200) # 0j pol1
        histo2018DATA.Fit("tf5", "", "", 0, 200)
        tf6 = ROOT.TF1("tf6","pol6",0, 200) # 0j pol1
        histo2018DATA.Fit("tf6", "", "", 0, 200)
        tf7 = ROOT.TF1("tf7","pol7",0, 200) # 0j pol1
        histo2018DATA.Fit("tf7", "", "", 0, 200)
        tf8 = ROOT.TF1("tf8","pol8",0, 200) # 0j pol1
        histo2018DATA.Fit("tf8", "", "", 0, 200)
        tf9 = ROOT.TF1("tf9","pol9",0, 200) # 0j pol1
        histo2018DATA.Fit("tf9", "", "", 0, 200)		
        histo2018DATA.Draw()
        tf1.SetLineColor(ROOT.kRed)
        tf1.Draw("same")
        tf2.SetLineColor(ROOT.kGreen)
        tf2.Draw("same")
        tf3.SetLineColor(ROOT.kBlue)
        tf3.Draw("same")
        tf4.SetLineColor(ROOT.kPink)
        tf4.Draw("same")
        tf5.SetLineColor(ROOT.kOrange)
        tf5.Draw("same")
        tf6.SetLineColor(ROOT.kViolet)
        tf6.Draw("same")
        tf7.SetLineColor(ROOT.kYellow)
        tf7.Draw("same")
        tf8.SetLineColor(ROOT.kCyan)
        tf8.Draw("same")
        tf9.SetLineColor(ROOT.kMagenta)
        tf9.Draw("same")
        canvas.SaveAs('ratio_plots/ratio_' + args.jet  +  '.png')
        canvas.SaveAs('ratio_plots/ratio_' + args.jet  +  '.C')

    rfile2018.Close()
    rfile2017.Close()
    rfile2016HIPM.Close()
    rfile2016noHIPM.Close()
