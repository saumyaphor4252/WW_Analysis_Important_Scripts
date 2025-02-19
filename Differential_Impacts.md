```

#######################
####### jetpt0 ########
#######################
cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/macros/Datacards_13thFeb2025/datacards/input/differential_DF/jetpt0/Impacts/FullRunII

combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 --doInitialFit --saveFitResult
combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 --doFits --job-mode condor --sub-opts '+JobFlavour = "longlunch"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan
combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 -o impacts_jetpt0.json
plotImpacts.py -i impacts_jetpt0.json --POI r_0 -o impacts_r0
plotImpacts.py -i impacts_jetpt0.json --POI r_1 -o impacts_r1
plotImpacts.py -i impacts_jetpt0.json --POI r_2 -o impacts_r2
plotImpacts.py -i impacts_jetpt0.json --POI r_3 -o impacts_r3
plotImpacts.py -i impacts_jetpt0.json --POI r_4 -o impacts_r4
plotImpacts.py -i impacts_jetpt0.json --POI r_5 -o impacts_r5
plotImpacts.py -i impacts_jetpt0.json --POI r_6 -o impacts_r6
plotImpacts.py -i impacts_jetpt0.json --POI r_7 -o impacts_r7
plotImpacts.py -i impacts_jetpt0.json --POI r_8 -o impacts_r8
plotImpacts.py -i impacts_jetpt0.json --POI r_9 -o impacts_r9
plotImpacts.py -i impacts_jetpt0.json --POI r_10 -o impacts_r10

combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan

#######################
####### jetpt1 ########
#######################
### Impacts
combineTool.py -M Impacts -d ../../FullRunII_jetpt1.root -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt1 --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan 
#combineTool.py -M Impacts -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.9,1.2 -d FullRunII_jetpt1.root --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt1 --doFits --job-mode condor
#combineTool.py -M Impacts -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.9,1.2 -d FullRunII_jetpt1.root --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt1 -o impacts_jetpt1.json
#plotImpacts.py -i impacts_jetpt1.json --POI r_0 -o impacts_r0
#plotImpacts.py -i impacts_jetpt1.json --POI r_1 -o impacts_r1
#plotImpacts.py -i impacts_jetpt1.json --POI r_2 -o impacts_r2
#plotImpacts.py -i impacts_jetpt1.json --POI r_3 -o impacts_r3
#plotImpacts.py -i impacts_jetpt1.json --POI r_4 -o impacts_r4
#plotImpacts.py -i impacts_jetpt1.json --POI r_5 -o impacts_r5


#######################
####### dphijj ########
#######################
combineTool.py -M Impacts -d ../../FullRunII_dphijj.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=-5,5 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj --doInitialFit  --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan
combineTool.py -M Impacts -d ../../FullRunII_dphijj.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=-5,5 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj --doFits --job-mode condor --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan
combineTool.py -M Impacts -d ../../FullRunII_dphijj.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj -o impacts_dphijj.json


#######################
######### mjj #########
#######################

combineTool.py -M Impacts -d ../../FullRunII_mjj.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n mjj --doInitialFit --saveFitResult --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'
#combineTool.py -M Impacts -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.9,1.2 -d FullRunII_mjj.root --X-rtd MINIMIZER_analytic --robustFit=1 -n mjj --doFits --job-mode condor
#combineTool.py -M Impacts -m 125 -t -1 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=0.9,1.2 -d FullRunII_mjj.root --X-rtd MINIMIZER_analytic --robustFit=1 -n mjj -o impacts_mjj.json
#plotImpacts.py -i impacts_mjj.json --POI r_0 -o impacts_r0
#plotImpacts.py -i impacts_mjj.json --POI r_1 -o impacts_r1
#plotImpacts.py -i impacts_mjj.json --POI r_2 -o impacts_r2
#plotImpacts.py -i impacts_mjj.json --POI r_3 -o impacts_r3
#plotImpacts.py -i impacts_mjj.json --POI r_4 -o impacts_r4
#plotImpacts.py -i impacts_mjj.json --POI r_5 -o impacts_r5
#plotImpacts.py -i impacts_mjj.json --POI r_6 -o impacts_r6
#plotImpacts.py -i impacts_mjj.json --POI r_7 -o impacts_r7
#plotImpacts.py -i impacts_mjj.json --POI r_8 -o impacts_r8
#plotImpacts.py -i impacts_mjj.json --POI r_9 -o impacts_r9
#plotImpacts.py -i impacts_mjj.json --POI r_10 -o impacts_r10

##################################
####### leading lepton pT ########
##################################

combineTool.py -M Impacts -d ../../FullRunII_leadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n leadinglepPT --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'
combineTool.py -M Impacts -d ../../FullRunII_leadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n leadinglepPT --doFits --job-mode condor --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan

#####################################
####### subleading lepton pT ########
#####################################

combineTool.py -M Impacts -d ../../FullRunII_subleadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n subleadinglepPT --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'
combineTool.py -M Impacts -d ../../FullRunII_subleadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n subleadinglepPT --doFits --job-mode condor --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan

####################
####### mll ########
####################

combineTool.py -M Impacts -d ../../FullRunII_mll.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1  --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n mll --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'
combineTool.py -M Impacts -d ../../FullRunII_subleadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n mll --doFits --job-mode condor --sub-opts '+JobFlavour = "longlunch"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan

####################
####### ptll #######
####################

combineTool.py -M Impacts -d ../../FullRunII_ptll.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n ptll --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'
combineTool.py -M Impacts -d ../../FullRunII_subleadinglepPT.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n mll --doFits --job-mode condor --sub-opts '+JobFlavour = "longlunch"' --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan

#####################
####### ptWW ########
#####################

combineTool.py -M Impacts -d ../../FullRunII_ptWW.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n ptWW --doInitialFit --saveFitResult --job-mode condor --sub-opts '+JobFlavour = "tomorrow"'




```
