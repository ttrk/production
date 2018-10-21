#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtRecoValidation2018?rev=88#To_be_produced_Restart_from_GEN
inputFile="/store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root"

## Software
# CMSSW_10_3_0_pre6, l1t-integration-CMSSW_10_2_1
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
## Driver
# derived by updating the L1 workflow to match the latest HLT setup. Current L1 setup was probably obsolete
# (probably obsolete) L1 instructions : https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=42#Offline_SW_setup
# HLT instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=32#Instructions_as_of_2018_10_14_in
ERA="Run2_2018"
GLOBALTAG="103X_upgrade2018_realistic_HI_v6"
nEvents=100
configPrefix="l1Ntuple"

### modify input for calo digi collection
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=141#Workflows_AN1
#--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP
# https://github.com/cms-sw/cmssw/blob/master/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254
# https://github.com/cms-sw/cmssw/blob/71741cd7aea763fce2c07ca50370cd14b7edd261/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254

$runCmd cmsDriver.py $configPrefix -s RAW2DIGI --era=$ERA \
--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN \
--customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo \
--customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 \
--customise_commands="process.simTwinMuxDigis.DTDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.RPC_Source = cms.InputTag('muonRPCDigis')\n" \
--conditions=$GLOBALTAG -n $nEvents --mc --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log

config_l1Ntuple=$configPrefix"_RAW2DIGI.py"

#muon customization (via Emilien)
echo "" >> $config_l1Ntuple
echo "process.simEmtfDigis.CSCInputBXShift = cms.int32(-6)" >> $config_l1Ntuple

#Jet customization (via Chris)
echo "" >> $config_l1Ntuple
echo "process.caloStage2Params.hiMode = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.jetPUSType = cms.string('PhiRing2')" >> $config_l1Ntuple
echo "process.caloStage2Params.jetPUSUseChunkySandwich = cms.uint32(False)" >> $config_l1Ntuple

# Centrality customization (via Jing)
echo "" >> $config_l1Ntuple
echo "process.caloStage2Params.etSumCentralityLower = cms.vdouble(0.0, 1.35, 7.15, 71.0, 219.5, 583.4, 1310.6, 65535.0)" >> $config_l1Ntuple
echo "process.caloStage2Params.etSumCentralityUpper = cms.vdouble(4.15, 13.6, 110.95, 302.1, 713.35, 1464.35, 2664.05, 65535.0)" >> $config_l1Ntuple

# process.caloStage2Params is somehow not seen. needed to use customiseSettings.L1TSettingsToCaloStage2Params_XXX to make it appear
#echo "process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egBypassShape = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egBypassECALFG = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egEtaCut = cms.int32(24)" >> $config_l1Ntuple  # ignore all the EGs with ieta > 24

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

