from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "L1Ntuple_HIMinimumBias2_egBypassFGBit1ShapeBit1ExtHOverE1_egHOverEcut_EB1_EE1_BypassPt30_egCap24"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "l1Ntuple_RAW2DIGI.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2750 # request longer runtime, ~47 hours. 2750 is the maximum guaranteed number.
# CMSSW_9_4_0_pre3, l1t-integration-v97.9
# Instructions : https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=16#Offline_SW_setup
# generic L1 Stage2 instructions : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=123
# modify Stage2Layer2EGammaAlgorithmFirmwareImp1.cc as described in README
# l1Ntuple_RAW2DIGI.py is created after calling ./createConfigs.sh

config.section_("Data")
config.Data.userInputFiles = open('inputFiles.txt').readlines()
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1

config.Data.outputPrimaryDataset = "L1T"
config.Data.outputDatasetTag = "L1Ntuple_HIRun2015_HIMinimumBias2_egBypassFGBit1ShapeBit1ExtHOverE1_egHOverEcut_EB1_EE1_BypassPt30_egCap24"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
