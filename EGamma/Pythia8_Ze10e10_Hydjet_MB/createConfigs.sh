#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeVOfficialMC?rev=213#cmsDriver_Commands
$runCmd cmsDriver.py step2 --pileup_input "dbs:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM" --pileup_dasoption="--limit=0" --mc --eventcontent RAWSIM --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --datatier GEN-SIM-RAW --conditions 75X_mcRun2_HeavyIon_v13 --step DIGI:pdigi_hi,L1,DIGI2RAW,HLT:HIon --scenario HeavyIons -n 10 --no_exec --filein root://cms-xrd-global.cern.ch//store/himc/HiFall15/Pythia8_Ze10e10_Hydjet_MB/GEN-SIM/75X_mcRun2_HeavyIon_v1_ext1-v1/60000/00B93BC6-7203-E611-A4FF-141877411970.root &> cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log

# with command line options: step2 --pileup_input dbs:/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/HiFall15-75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/GEN-SIM --pileup_dasoption=--limit=0 --mc --eventcontent RAWSIM --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --datatier GEN-SIM-RAW --conditions 75X_mcRun2_HeavyIon_v14 --step DIGI:pdigi_hi,L1,DIGI2RAW,HLT:HIon --scenario HeavyIons -n 20 --no_exec --filein root://cms-xrd-global.cern.ch//store/himc/HiFall15/Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB/GEN-SIM/75X_mcRun2_HeavyIon_v14-v1/120000/005D04E2-57F4-E611-BAD4-02163E01A294.root

