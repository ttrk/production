from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "L1Ntuple_XeXeRun2017_HIMinimumBias7_PhiRingPPTower"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "l1Ntuple_RAW2DIGI.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2750 # request longer runtime, ~47 hours. 2750 is the maximum guaranteed number.
# CMSSW_10_0_0, l1t-integration-v97.17-v2
# Instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=15#L1_Sample_Workflow
# generic L1 Stage2 instructions : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=126#Environment_Setup_with_Integrati
# l1Ntuple_RAW2DIGI.py is created after calling ./createConfigs.sh

config.section_("Data")
config.Data.userInputFiles = open('inputFiles.txt').readlines()
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1

config.Data.outputPrimaryDataset = "L1T"
config.Data.outputDatasetTag = "L1Ntuple_XeXeRun2017_HIMinimumBias7_PhiRingPPTower"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
