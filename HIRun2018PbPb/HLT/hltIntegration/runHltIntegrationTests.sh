#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

## instructions : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT?rev=3121#Testing%20your%20HLT%20paths
inputFile="root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root,root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1653.root,root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1654.root"

# menu V23 was used in the jira ticket to change eta cut for Island photon paths in PbPb 2018 : https://its.cern.ch/jira/browse/CMSHLT-2060
menu="/users/katatar/HI2018PbPb/hltPbPb2018Photons/V23"
configFile="hltConfig.py"
GLOBALTAG=103X_upgrade2018_realistic_HI_v7
SETUP=/dev/CMSSW_10_3_0/GRun
PROCESS="MyHLT"
nEvents=100
DATAMC="--mc"
CUSTOMISE="--customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4"
CUSTOMISE_CMD="--customise_commands='process.caloStage2Params.hiMode = cms.uint32(1)'"
L1EMU="--l1-emulator FullMC"
## L1 menu v4 : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5380/2/1/1.html
L1XML="L1Menu_CollisionsHeavyIons2018_v4.xml"

hltIntegrationTests $menu -s $SETUP -i $inputFile --mc -x "--globaltag $GLOBALTAG --process $PROCESS --full --offline $DATAMC --no-output --unprescale $L1EMU --l1Xml $L1XML $CUSTOMISE --timing --max-events $nEvents"

## had to explicity add hiMode parameter, otherwise gives error on parameter not being found
#[katatar@lxplus024 src]$ git diff --unified=0  L1Trigger/L1TCalorimeter/python/caloParams_2018_v1_4_cfi.py
#diff --git a/L1Trigger/L1TCalorimeter/python/caloParams_2018_v1_4_cfi.py b/L1Trigger/L1TCalorimeter/python/caloParams_2018_v1_4_cfi.py
#index 3131f636415..d4ca5482670 100644
#--- a/L1Trigger/L1TCalorimeter/python/caloParams_2018_v1_4_cfi.py
#+++ b/L1Trigger/L1TCalorimeter/python/caloParams_2018_v1_4_cfi.py
#@@ -181,0 +182,2 @@ caloStage2Params.layer1HFScaleFactors = cms.vdouble([
#+
#+caloStage2Params.hiMode = cms.uint32(1)
