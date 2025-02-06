# Signal Strengths

```
###############################
2016 HIPM Expected {Observed}
###############################
cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/MyScripts/28thJan/Upload/datacards/input/differential_DF/dphijj/Unblinding/2016_HIPM/Expected{Observed}

### Signal strengths
combine -M MultiDimFit --algo singles -d ../../../Full2016_HIPM_dphijj.root {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --X-rtd MINIMIZER_analytic > Full2016_HIPM_dphijj_Expected{Observed}.out
#### Expected
    r_8 :    +1.000   -0.729/+0.777 (68%)
    r_9 :    +1.000   -0.782/+0.823 (68%)
   r_11 :    +1.000   -0.793/+0.836 (68%)
    r_0 :    +1.000   -0.627/+0.666 (68%)
    r_1 :    +1.000   -0.708/+0.746 (68%)
    r_2 :    +1.000   -0.888/+0.934 (68%)
    r_3 :    +1.000   -0.776/+0.833 (68%)
    r_4 :    +1.000   -0.750/+0.813 (68%)
    r_5 :    +1.000   -0.716/+0.761 (68%)
    r_6 :    +1.000   -0.621/+0.655 (68%)
    r_7 :    +1.000   -0.611/+0.641 (68%)
   r_12 :    +1.000   -0.699/+0.739 (68%)
   r_13 :    +1.000   -0.717/+0.781 (68%)
   r_10 :    +1.000   -0.769/+0.825 (68%)

### Impacts
combineTool.py -M Impacts -d ../../../Full2016_HIPM_dphijj.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj --doInitialFit --saveFitResult

#### Expected
    r_8 :    +1.000   -0.725/+0.773 (68%)
    r_9 :    +1.000   -0.778/+0.819 (68%)
   r_11 :    +1.000   -0.788/+0.831 (68%)
    r_0 :    +1.000   -0.623/+0.662 (68%)
    r_1 :    +1.000   -0.704/+0.742 (68%)
    r_2 :    +1.000   -0.883/+0.929 (68%)
    r_3 :    +1.000   -0.771/+0.829 (68%)
    r_4 :    +1.000   -0.746/+0.809 (68%)
    r_5 :    +1.000   -0.712/+0.758 (68%)
    r_6 :    +1.000   -0.618/+0.652 (68%)
    r_7 :    +1.000   -0.608/+0.637 (68%)
   r_12 :    +1.000   -0.695/+0.734 (68%)
   r_13 :    +1.000   -0.714/+0.777 (68%)
   r_10 :    +1.000   -0.764/+0.820 (68%)

#### Observed
    r_8 :    +0.438   -0.693/+0.732 (68%)
    r_9 :    +1.092   -0.746/+0.780 (68%)
   r_11 :    +1.666   -0.801/+0.865 (68%)
    r_0 :    +2.153   -0.649/+0.705 (68%)
    r_1 :    +1.211   -0.690/+0.727 (68%)
    r_2 :    +2.468   -0.944/+1.007 (68%)
    r_3 :    +1.310   -0.783/+0.847 (68%)
    r_4 :    +1.259   -0.728/+0.774 (68%)
    r_5 :    +1.819   -0.727/+0.789 (68%)
    r_6 :    +1.432   -0.631/+0.674 (68%)
    r_7 :    +2.061   -0.630/+0.677 (68%)
   r_12 :    +1.889   -0.703/+0.752 (68%)
 Warning - No valid high-error found, will report difference to maximum of range for : r_13
   r_13 :    +1.110   -0.700/+8.890 (68%)
   r_10 :    +1.744   -0.780/+0.847 (68%)

combineTool.py -M Impacts -d ../../../Full2016_HIPM_dphijj.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../../Full2016_HIPM_dphijj.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj -o impacts_dphijj_2016_HIPM_Expected{Observed}.json

plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_0 -o impacts_r0
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_1 -o impacts_r1
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_2 -o impacts_r2
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_3 -o impacts_r3
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_4 -o impacts_r4
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_5 -o impacts_r5
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_6 -o impacts_r6
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_7 -o impacts_r7
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_8 -o impacts_r8
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_9 -o impacts_r9
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_10 -o impacts_r10
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_11 -o impacts_r11
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_12 -o impacts_r12
plotImpacts.py -i impacts_dphijj_2016_HIPM_Expected{Observed}.json --POI r_13 -o impacts_r13

### Posterior nuisance parameters / correlations
#combine -M FitDiagnostics -d ../../../Full2016_HIPM_dphijj.root -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --X-rtd MINIMIZER_analytic --skipBOnlyFit

```
