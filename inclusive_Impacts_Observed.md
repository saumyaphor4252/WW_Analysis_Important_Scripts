```
#########################
####### Inclusive #######
#########################

### FullRunII ###

combineTool.py -M Impacts -d ../../FullRunII_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../FullRunII_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../FullRunII_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_DF_FullRunII_Observed

combineTool.py -M Impacts -d ../../FullRunII_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../FullRunII_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../FullRunII_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_FullRunII_Observed

combineTool.py -M Impacts -d ../../FullRunII_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../FullRunII_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../FullRunII_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_DF_FullRunII_Observed

### Full2018 ###

combineTool.py -M Impacts -d ../../Full2018_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2018_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2018_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_DF_Full2018_Observed

combineTool.py -M Impacts -d ../../Full2018_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2018_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2018_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_Full2018_Observed

combineTool.py -M Impacts -d ../../Full2018_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2018_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2018_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_DF_Full2018_Observed

### Full2017 ###

combineTool.py -M Impacts -d ../../Full2017_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2017_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2017_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_DF_Full2017_Observed

combineTool.py -M Impacts -d ../../Full2017_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2017_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2017_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_Full2017_Observed

combineTool.py -M Impacts -d ../../Full2017_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2017_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2017_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_DF_Full2017_Observed

### Full2016 HIPM ###

combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_DF_Full2016_HIPM_Observed

combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_Full2016_HIPM_Observed

combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_HIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_DF_Full2016_HIPM_Observed

### Full2016 noHIPM ###

combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_DF_Full2016_noHIPM_Observed

combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_Full2016_noHIPM_Observed

combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --doInitialFit --expectSignal 1 --robustFit 1 --saveFitResult
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --doFits --job-mode condor --task-name impacts --sub-opts '+JobFlavour = "microcentury"'
combineTool.py -M Impacts -d ../../Full2016_noHIPM_incl_SF_DF.root -m 125 --setParameterRanges CMS_SMP24008_Topnorm_0j=0.5,1.5:CMS_SMP24008_Topnorm_1j=0.5,1.5:CMS_SMP24008_Topnorm_2j=0.5,1.5 --expectSignal 1 --task-name impacts --sub-opts '+JobFlavour = "microcentury"' -o impacts.json 
plotImpacts.py -i impacts.json -o impacts_WW_inclusive_SF_DF_Full2016_noHIPM_Observed
```
