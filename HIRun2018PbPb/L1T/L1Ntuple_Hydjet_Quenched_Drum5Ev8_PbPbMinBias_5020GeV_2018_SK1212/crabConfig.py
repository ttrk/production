from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "L1Ntuple_Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_SK1212"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "l1Ntuple_RAW2DIGI.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2750 # request longer runtime, ~47 hours. 2750 is the maximum guaranteed number.
## Software
# CMSSW_10_2_1, l1t-integration-v99.0
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=140#Environment_Setup_with_Integrati
## Driver
# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=42#Offline_SW_setup
# l1Ntuple_RAW2DIGI.py is created after calling ./createConfigs.sh

# Samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=15#Available_Samples_AN1
config.section_("Data")
config.Data.allowNonValidInputDataset = True    # because the dataset is not 'VALID' but 'PRODUCTION'.
config.Data.inputDataset = "/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18DR-NoPU_100X_upgrade2018_realistic_v10_ext1-v1/GEN-SIM-RAW"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "L1Ntuple_egHOverEcut_EB1_EE1_egEtaCut24_SK1212"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/L1T/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
