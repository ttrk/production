#!/bin/bash

inputFile="root://cms-xrd-global.cern.ch//store/user/mnguyen/Hydjet_Quenched_MB_1000/Hydjet_Quenched_MB_1000/crab_Hydjet_Quenched_MB_5020GeV_DIGI_1000/180201_190937/0000/step2_1.root"
# step3 command for wf150. Remove VALIDATION and DQM steps. Remove MINIAODSIM event content.
cmsDriver.py step3 --conditions auto:phase1_2018_realistic -s RAW2DIGI,L1Reco,RECO --era Run2_2018 --eventcontent RECOSIM --runUnscheduled --scenario HeavyIons --datatier GEN-SIM-RECO -n 50 --no_exec --filein=$inputFile &> cmsDriver_wf150_step3_RAW2DIGI_L1Reco_RECO.log 

configFile="step3_RAW2DIGI_L1Reco_RECO.py"
echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(False), useJobReport = cms.untracked.bool(True))" >> $configFile

