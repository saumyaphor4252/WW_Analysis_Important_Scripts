import ROOT
import argparse
from array import array

parser = argparse.ArgumentParser(description = "Receive the parameters")
parser.add_argument('--jet', action = 'store', type = str, dest = 'jet', help = '')
args = parser.parse_args()

ptWW_bin = "pTWW"

# Open input ROOT file
input_file = ROOT.TFile.Open("../../Full2018_v9/inclusive/rootFile/plots_WW2018_v9_incl.root", "READ")

# Output root file
output_file = ROOT.TFile.Open("rebinned_output_2018.root", "RECREATE")

samples = ["DY","DATA","WW_B0","WW_nonfid","ggWW_B0","ggWW_nonfid","WWewk","Vg","WZ","ZZ","VVV","Higgs","top","Fake_em","Fake_me"]

histo = {}
for sample in samples:
    # Get original histograms	
    histo = input_file.Get("ww2l2v_13TeV_top_" + args.jet + "/" + ptWW_bin + "/histo_" + sample)
    #print(type(histo))
    	
    # Define new bin edges (non-uniform binning)
    new_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 200]
    n_new_bins = len(new_bins) - 1

    # Create a new histogram with the desired binning
    rebinned_hist = ROOT.TH1F(histo.GetName(), histo.GetTitle(), n_new_bins, array('d', new_bins))

    # Rebin content from original histogram into the new one
    for i in range(1, histo.GetNbinsX() + 1):
        x = histo.GetBinCenter(i)
        content = histo.GetBinContent(i)
        error = histo.GetBinError(i)
        rebinned_hist.Fill(x, content)  # Fill content manually

    # Copy errors
    for i in range(1, histo.GetNbinsX() + 1):
        x = histo.GetBinCenter(i)
        bin = rebinned_hist.FindBin(x)
        rebinned_hist.SetBinError(bin, (rebinned_hist.GetBinError(bin)**2 + histo.GetBinError(i)**2)**0.5)

    # Save the new histogram
    output_file.cd()
    rebinned_hist.Write()
    print("Rebinning complete. New histogram saved as %s"%rebinned_hist.GetName())
    
input_file.Close()	
output_file.Close()
