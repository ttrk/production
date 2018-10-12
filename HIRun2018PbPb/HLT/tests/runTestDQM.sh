#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HLTValidationAndDQM
# code that adds HLT photon paths to DQM histograms : https://github.com/ttrk/cmssw/blob/3f421cc1bfa1e7abd8a655cdb410d944e2da33de/DQMOffline/Trigger/python/HILowLumiHLTOfflineSource_cfi.py
gen="file:/afs/cern.ch/work/r/rbi/public/Pythia8_Ze10e10_m60120_pthat0_TuneCUETP8M1_5020GeV_cff_py_GEN_SIM_PU_12.root"
menu=/users/katatar/HI2018PbPb/hltTestEgamma/V55
l1xml=L1Menu_CollisionsHeavyIons2018_v3_rmAsyCent.xml
nEvents="10"

hltGetConfiguration $menu --globaltag auto:run2_mc_GRun --input file:/afs/cern.ch/work/r/rbi/public/open/step1_DIGI_L1_DIGI2RAW_HLT_PU_12.root --setup /dev/CMSSW_10_1_0/GRun --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking --type GRun --cff --offline --mc --unprescale --l1-emulator FullMC --l1 $l1xml --max-events -1 > HLT_User_cff.py

sed -i 's/fragment.load("setup_dev_CMSSW_10_1_0_GRun_cff")/fragment.load("HLTrigger.Configuration.setup_dev_CMSSW_10_1_0_GRun_cff")/g' HLT_User_cff.py

mv HLT_User_cff.py HLTrigger/Configuration/python
mv setup_dev_CMSSW_10_1_0_GRun_cff.py HLTrigger/Configuration/python

# temporary process name change for dqm to pick up correct paths/filters
sed -i 's/processName = "HLT"/processName = "REHLT"/g' DQMOffline/Trigger/python/HILowLumiHLTOfflineSource_cfi.py

scram b -j8

cmsDriver.py step1 --conditions auto:phase1_2018_realistic_hi -s DIGI:pdigi_hi,L1,DIGI2RAW,HLT:@fake2 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup HiMixNoPU -n $nEvents --era Run2_2018_pp_on_AA --eventcontent FEVTDEBUGHLT --filein $gen --fileout file:step1.root > step1.log 2>&1

cmsDriver.py step2 --mc --conditions auto:phase1_2018_realistic_hi -s HLT:User -n $nEvents --hltProcess REHLT --processName REHLT --era Run2_2018_pp_on_AA --eventcontent FEVTDEBUGHLT --filein file:step1.root --fileout file:step2.root --no_exec

cat >> step2_HLT.py << @EOF
# override the GlobalTag's L1T menu from an Xml file
from HLTrigger.Configuration.CustomConfigs import L1XML
process = L1XML(process,"$l1xml")
@EOF

cmsRun step2_HLT.py > step2.log 2>&1

cmsDriver.py step3 --mc --runUnscheduled --conditions auto:phase1_2018_realistic_hi -s RAW2DIGI,L1Reco,RECO,ALCA:SiStripCalZeroBias+SiPixelCalZeroBias,EI,PAT,VALIDATION:@standardValidation+@miniAODValidation,DQM:offlineHLTSource4specialPhysicsPD --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO,ALCARECO -n $nEvents --era Run2_2018_pp_on_AA --eventcontent RECOSIM,MINIAODSIM,DQM,ALCARECO --filein file:step2.root --fileout file:step3.root > step3.log 2>&1

cmsDriver.py step4 --mc --conditions auto:phase1_2018_realistic_hi -s ALCA:TkAlMinBias+SiStripCalMinBias --datatier ALCARECO -n $nEvents --era Run2_2018_pp_on_AA --eventcontent ALCARECO --filein file:step3.root --fileout file:step4.root > step4.log 2>&1

cmsDriver.py step5 --conditions auto:phase1_2018_realistic_hi --filein file:step3_inDQM.root -s HARVESTING:validationHarvesting+dqmHarvesting --filetype DQM -n $nEvents --era Run2_2018_pp_on_AA --mc --fileout file:step5.root > step5.log 2>&1
