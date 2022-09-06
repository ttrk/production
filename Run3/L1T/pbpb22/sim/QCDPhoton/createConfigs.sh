#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce2022?rev=68#Instructions_to_run_the_L1Emulat
#inputFile="root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root"
inputFile="/store/user/mnguyen/Run3MC/QCDPhoton_pThat15_Run3_HydjetEmbedded/QCDPhoton_pThat15_Run3_HydjetEmbedded_DIGI/220301_130050/0001/step2_DIGI_L1_DIGI2RAW_HLT_PU_1275.root"

## Setup
#cmsrel cmsrel CMSSW_12_4_0
#cd CMSSW_12_4_0/src
#cmsenv
#git cms-init
#git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
#git fetch cms-l1t-offline l1t-integration-CMSSW_12_4_0
#git cms-merge-topic -u cms-l1t-offline:l1t-integration-v132.0
#git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data
#git cms-merge-topic -u kakwok:CLCT_thresholds

#git cms-checkdeps -A -a

#scram b -j 8
# L1T emulation relevant GlobalTags in CMSSW_12_4_0 are:

#    for run2 data reprocessing '124X_dataRun2_v2'
#    for run2 mc '123X_mcRun2_asymptotic_v1' (to be updated)
#    for run3 mc '124X_mcRun3_2022_realistic_v10'

#git cms-addpkg L1Trigger/L1TCommon
#git cms-addpkg L1Trigger/L1TGlobal
#mkdir -p L1Trigger/L1TGlobal/data/Luminosity/startup/
#cd L1Trigger/L1TGlobal/data/Luminosity/startup/
#wget https://raw.githubusercontent.com/mitaylor/HIMenus/main/Menus/L1Menu_CollisionsHeavyIons2022_v0_0_5.xml
#cd ../../../../../
#scram b -j 8
# Edit the file L1Trigger/Configuration/python/customiseUtils.py by changing the L1TriggerMenuFile: process.TriggerMenu.L1TriggerMenuFile = cms.string('L1Menu_Collisions2022_v1_0_1.xml') → process.TriggerMenu.L1TriggerMenuFile = cms.string('L1Menu_CollisionsHeavyIons2022_v0_0_5.xml')

ERA="Run3_pp_on_PbPb"
GLOBALTAG="124X_mcRun3_2022_realistic_v10" # "124X_mcRun3_2022_realistic_v8"
nEvents=100
configPrefix="l1Ntuple"
config_l1Ntuple=$configPrefix"_RAW2DIGI.py"

${runCmd} cmsDriver.py ${configPrefix} -s RAW2DIGI --no_exec --python_filename=${config_l1Ntuple} \
-n ${nEvents} --no_output --era=${ERA} --mc --conditions=${GLOBALTAG} \
--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU \
--customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParamsHI_2022_v0_3 \
--customise=L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML \
--filein=${inputFile} &> cmsDriver_l1Ntuple_RAW2DIGI.log

echo '
process.hcalDigis.saveQIE10DataNSamples = cms.untracked.vint32(10) 
process.hcalDigis.saveQIE10DataTags = cms.untracked.vstring( "MYDATA" )
process.HcalTPGCoderULUT.FG_HF_thresholds = cms.vuint32(14, 19)
' >> ${config_l1Ntuple}

##Jet customization (via Chris)
#echo "" >> $config_l1Ntuple
#echo "process.caloStage2Params.hiMode = cms.uint32(1)" >> $config_l1Ntuple

## process.caloStage2Params is somehow not seen. needed to use customiseSettings.L1TSettingsToCaloStage2Params_XXX to make it appear
##echo "process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)" >> $config_l1Ntuple
##echo "process.caloStage2Params.egBypassShape = cms.uint32(1)" >> $config_l1Ntuple
##echo "process.caloStage2Params.egBypassECALFG = cms.uint32(1)" >> $config_l1Ntuple
##echo "process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)" >> $config_l1Ntuple
##echo "process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egEtaCut = cms.int32(24)" >> $config_l1Ntuple  # ignore all the EGs with ieta > 24

# where Spike Killer is activated :
# https://github.com/cms-sw/cmssw/blob/master/SimCalorimetry/EcalTrigPrimAlgos/src/EcalFenixTcpFormat.cc#L72-L75
# https://github.com/cms-sw/cmssw/blob/edb9f982c877bb0c568704d3383ede9ea099ec3a/SimCalorimetry/EcalTrigPrimAlgos/src/EcalFenixTcpFormat.cc#L72-L75
# change Spike Killer WP
# WP 12_12 : EcalTPGFineGrainStrip_12, EcalTPGSpike_12
# WP 12_7  : EcalTPGFineGrainStrip_7 , EcalTPGSpike_12
# WP 16_16 : EcalTPGFineGrainStrip_16, EcalTPGSpike_16
mod_ECAL_SK=0
TPG_FG=7
TPG_Spike=12
if [ ${mod_ECAL_SK} -gt 0 ]; then
  echo "
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
             tag = cms.string('EcalTPGFineGrainStrip_"${TPG_FG}"'),
             connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
                                                                 ),

    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),
             tag = cms.string('EcalTPGSpike_"${TPG_Spike}"'),
             connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
                                                                 )
    )" >> ${config_l1Ntuple}
fi

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

