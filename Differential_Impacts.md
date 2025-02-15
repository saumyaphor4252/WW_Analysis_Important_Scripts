```

#######################
####### jetpt0 ########
#######################
cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/macros/Datacards_13thFeb2025/datacards/input/differential_DF/jetpt0/Impacts/FullRunII

combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 --doInitialFit --saveFitResult
combineTool.py -M Impacts -d ../../FullRunII_jetpt0.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1 --setParameterRanges CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --X-rtd MINIMIZER_analytic --robustFit=1 -n jetpt0 --doFits --job-mode condor --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,0:0.2 --stepSize 0.01 --cminPreScan
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

#######################
####### dphijj ########
#######################
combineTool.py -M Impacts -d ../../FullRunII_dphijj.root -m 125 --setParameters r_0=1,r_1=1,r_2=1,r_3=1,r_4=1,r_5=1,r_6=1,r_7=1,r_8=1,r_9=1,r_10=1,r_11=1,r_12=1,r_13=1 --setParameterRanges CMS_SMP24008_Topnorm_2j=-5,5 --X-rtd MINIMIZER_analytic --robustFit=1 -n dphijj --doInitialFit  --saveFitResult --job-mode condor


```
