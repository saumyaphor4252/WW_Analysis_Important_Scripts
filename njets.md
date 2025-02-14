# Impacts (Unblinding)

```
###############################
2016 HIPM Expected {Observed}
###############################



combineTool.py -M Impacts -d ../../../Full2016_HIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doInitialFit --saveFitResult
combineTool.py -M Impacts -d ../../../Full2016_HIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../../Full2016_HIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet -o impacts_2016_HIPM.json

plotImpacts.py -i impacts_2016_HIPM.json --POI r_0 -o impacts_nj0
plotImpacts.py -i impacts_2016_HIPM.json --POI r_1 -o impacts_nj1
plotImpacts.py -i impacts_2016_HIPM.json --POI r_2 -o impacts_nj2
plotImpacts.py -i impacts_2016_HIPM.json --POI r_3 -o impacts_nj3		

###############################
2016 noHIPM Expected {Observed}
###############################

cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/MyScripts/28thJan/Upload/datacards/input/differential_DF/njets/Unblinding/2016_noHIPM/Expected{Observed}

combineTool.py -M Impacts -d ../../../Full2016_noHIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doInitialFit --saveFitResult


   
combineTool.py -M Impacts -d ../../../Full2016_noHIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../../Full2016_noHIPM_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet -o impacts_2016_noHIPM.json

plotImpacts.py -i impacts_2016_noHIPM.json --POI r_0 -o impacts_nj0
plotImpacts.py -i impacts_2016_noHIPM.json --POI r_1 -o impacts_nj1
plotImpacts.py -i impacts_2016_noHIPM.json --POI r_2 -o impacts_nj2
plotImpacts.py -i impacts_2016_noHIPM.json --POI r_3 -o impacts_nj3


###############################
2017 Expected {Observed}
###############################

cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/MyScripts/28thJan/Upload/datacards/input/differential_DF/njets/Unblinding/2017/Expected{Observed}

combineTool.py -M Impacts -d ../../../Full2017_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doInitialFit --saveFitResult



combineTool.py -M Impacts -d ../../../Full2017_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../../Full2017_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet -o impacts_2017_Expected{Observed}.json

plotImpacts.py -i impacts_2017_Expected{Observed}.json --POI r_0 -o impacts_nj0
plotImpacts.py -i impacts_2017_Expected{Observed}.json --POI r_1 -o impacts_nj1
plotImpacts.py -i impacts_2017_Expected{Observed}.json --POI r_2 -o impacts_nj2
plotImpacts.py -i impacts_2017_Expected{Observed}.json --POI r_3 -o impacts_nj3


###############################
2018 Expected {Observed}
###############################

cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/MyScripts/28thJan/Upload/datacards/input/differential_DF/njets/Unblinding/2018/Expected{Observed}

combineTool.py -M Impacts -d ../../Full2018_njet.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doInitialFit --saveFitResult

   r_0 :    +1.101   -0.049/+0.052 (68%)
   r_1 :    +0.871   -0.098/+0.104 (68%)
   r_2 :    +0.723   -0.226/+0.244 (68%)
   r_3 :    -0.108   -0.416/+0.421 (68%)
   
combineTool.py -M Impacts -d ../../Full2018_njet.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../../Full2018_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.8,1.2:CMS_SMP24008_Topnorm_1j=0.8,1.2:CMS_SMP24008_Topnorm_2j=0.8,1.2 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet -o impacts_2018_Expected{Observed}.json

plotImpacts.py -i impacts_2018_Expected{Observed}.json --POI r_0 -o impacts_nj0
plotImpacts.py -i impacts_2018_Expected{Observed}.json --POI r_1 -o impacts_nj1
plotImpacts.py -i impacts_2018_Expected{Observed}.json --POI r_2 -o impacts_nj2
plotImpacts.py -i impacts_2018_Expected{Observed}.json --POI r_3 -o impacts_nj3

###############################
FullRunII Expected {Observed}
###############################

cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/MyScripts/28thJan/Upload/datacards/input/differential_DF/njets/Unblinding//FullRunII/Expected{Observed}

combineTool.py -M Impacts -d ../../FullRunII_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doInitialFit --saveFitResult
   r_0 :    +1.120   -0.028/+0.029 (68%)
   r_1 :    +1.048   -0.076/+0.079 (68%)
   r_2 :    +1.075   -0.193/+0.204 (68%)
   r_3 :    +0.546   -0.340/+0.363 (68%)
combineTool.py -M Impacts -d ../../FullRunII_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet --doFits --job-mode condor --sub-opts='+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../FullRunII_njet.root -m 125 {-t -1} --setParameters r_0=1,r_1=1,r_2=1,r_3=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n njet -o impacts_2018_Expected{Observed}.json

plotImpacts.py -i impacts_FullRunII_Expected{Observed}.json --POI r_0 -o impacts_nj0
plotImpacts.py -i impacts_FullRunII_Expected{Observed}.json --POI r_1 -o impacts_nj1
plotImpacts.py -i impacts_FullRunII_Expected{Observed}.json --POI r_2 -o impacts_nj2
plotImpacts.py -i impacts_FullRunII_Expected{Observed}.json --POI r_3 -o impacts_nj3

```
