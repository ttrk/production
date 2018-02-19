#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeVOfficialMC?rev=179#cmsDriver_Commands
$runCmd cmsDriver.py step2 --pileup_input "dbs:/MinBias_TuneCUETP8M1_5p02TeV-pythia8/pp502Fall15-MCRUN2_71_V1-v1/GEN-SIM" --pileup_dasoption="--limit=0" --mc --eventcontent RAWSIM --pileup pp5TeV_Poisson_1p5 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions 75X_mcRun2_asymptotic_ppAt5TeV_v3 --step DIGI,L1,DIGI2RAW,HLT:PRef  -n 10 --no_exec --filein root://cms-xrd-global.cern.ch//store/himc/pp502Fall15/Pythia8_Ze10e10/GEN-SIM/MCRUN2_71_V1_ext1-v1/50000/0020CA3E-8C03-E611-B37D-44A842CFD5B1.root &> cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log

