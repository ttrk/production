#!/bin/bash

hltGetConfiguration /users/cfmcginn/RefPP5TeV2017/PPRef2017MasterCopy/V6  --full --offline --mc --unprescale --process TEST  --l1-emulator FullMC --l1Xml L1Menu_Collisions2017_dev_r9_HIppRefMODv3_20171028.xml  --globaltag 92X_upgrade2017_realistic_v11 --output none --max-events 10 --input root://cms-xrd-global.cern.ch//store/user/gsfs/Pythia8_Photon300_pp_CUETP8M1_5020GeV/RAW_20171002/171002_194612/0000/step2_pp_DIGI_L1_DIGI2RAW_HLT_1.root --setup /dev/CMSSW_9_2_0/GRun > hlt.py

echo '' >> hlt.py
echo 'process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)' >> hlt.py
echo 'process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)' >> hlt.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> hlt.py
echo 'process.hltbitanalysis.HLTProcessName = cms.string("TEST")' >> hlt.py
echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )' >> hlt.py
echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","TEST")' >> hlt.py
echo 'process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag("gctDigis","","TEST")' >> hlt.py
echo 'process.hltbitanalysis.l1GctHFRingSums = cms.InputTag("gctDigis","","TEST")' >> hlt.py
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> hlt.py
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> hlt.py
echo 'process.TFileService = cms.Service("TFileService",' >> hlt.py
echo '                                  fileName=cms.string("openHLT.root"))' >> hlt.py
