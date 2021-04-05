#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=29#DIGI_RECO
# software : CMSSW_10_3_2

inputFile="file:/eos/cms/store/group/phys_heavyions/katatar/run3/ECAL/mc/pbpb18_qcd_photon/step1_GEN_SIM.root"
globalTag="103X_upgrade2018_realistic_HI_v11"
step="DIGI:pdigi_hi,L1,DIGI2RAW,HLT:@fake2"
era="Run2_2018_pp_on_AA"
inputPU="dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM"
inputPULimit="--limit=200"  # limit is the number of files to fetch from the PU dataset, set "--limit=0" to fetch all files
nEvents=10
configFile="step2_DIGI.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step2_DIGI.log"

${runCmd} cmsDriver.py step2 --mc --pileup_input ${inputPU} --pileup_dasoption=${inputPULimit} --eventcontent RAWSIM --pileup HiMix --datatier GEN-SIM-DIGI-RAW --conditions ${globalTag} --step ${step} --scenario HeavyIons --geometry DB:Extended --era ${era} --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## To modify ECAL settings, copy the lines in digiExtraLines.txt into your config
#cat digiExtraLines.txt >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

## DB file which changes ECAL settings
#echo "import CondCore.DBCommon.CondDBSetup_cfi" >> $configFile
#echo "process.GlobalTag.toGet = cms.VPSet(" >> $configFile
#echo "  cms.PSet(record = cms.string(\"EcalSRSettingsRcd\")," >> $configFile
#echo "    tag = cms.string(\"EcalSRSettings_beam2018_option1_v00_mc\")," >> $configFile
#echo "    connect = cms.string(\"sqlite_file:EcalSRSettings_beam2018_option1_v00_mc.db\")" >> $configFile
#echo "    )" >> $configFile
#echo "  )" >> $configFile
