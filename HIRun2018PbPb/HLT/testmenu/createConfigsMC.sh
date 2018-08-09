#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=15
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_163544/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_1.root"

menu="/users/katatar/HI2018PbPb/hltTestEgamma/V26"
configMenu="menu_hltTestEgamma_MC.py"
nEvents="100"
#customizations="FWCore/ParameterSet/MassReplace.massReplaceInputTag"

hltGetConfiguration $menu --globaltag auto:run2_mc_GRun --input $inputFile --setup /dev/CMSSW_10_1_0/GRun --process MyHLT --full --offline --mc --unprescale --l1-emulator FullMC --max-events $nEvents > $configMenu
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

# Add hltBitAnalyzer
echo '' >> $configMenu
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configMenu
echo 'process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configMenu
echo 'process.hltbitanalysis.RunParameters = cms.PSet(' >> $configMenu
echo '   isData = cms.untracked.bool(False))' >> $configMenu
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configMenu
echo 'process.TFileService = cms.Service("TFileService",' >> $configMenu
echo '   fileName=cms.string("openHLT_MC.root"))' >> $configMenu

configMenuLOG="${configMenu/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configMenu &> $configMenuLOG &"
#echo "myRun cmsRun $configMenu 2>&1 | tee $configMenuLOG &"

## dump the full config
configMenuFULL="${configMenu/.py/_FULL.py}"
edmConfigDump $configMenu > $configMenuFULL
echo "# Full config is also created : $configMenuFULL"

cp $configMenuFULL "${configMenuFULL/.py/.BACKUP.py}"
## need to fix some lines in the full config
sed -i "s/L1T INFO/#L1T INFO/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives = cms.Sequence/#process.hgcalTriggerPrimitives = cms.Sequence/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives_reproduce = cms.Sequence/#process.hgcalTriggerPrimitives_reproduce = cms.Sequence/g" $configMenuFULL

configMenuFULLLOG="${configMenuFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configMenuFULL &> $configMenuFULLLOG &"

