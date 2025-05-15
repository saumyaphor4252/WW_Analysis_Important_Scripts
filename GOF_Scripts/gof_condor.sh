#!/bin/bash

WORKSPACE="/afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/macros/Datacards_13thFeb2025/datacards/input/inclusive_SF_DF/FullRunII_incl_SF_DF.root"
NTOYS=1

# Setup CMSSW Base
export SCRAM_ARCH=el9_amd64_gcc12
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /afs/cern.ch/work/s/ssaumya/private/Projects/HiggsCombine/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/macros/Datacards_13thFeb2025/datacards/input/inclusive_SF_DF/GOF_Revision/FullRunII_v2/
eval `scramv1 runtime -sh`

cmsenv
ulimit -s unlimited

# Run 10 toys per job
combine -M GoodnessOfFit --algo=saturated -t 10 --toysFreq -s -1 -m 125 -d $WORKSPACE -n WW --setParameterRanges CMS_SMP24008_Topnorm_0j=-5,5:CMS_SMP24008_Topnorm_1j=-5,5:CMS_SMP24008_Topnorm_2j=-5,5
