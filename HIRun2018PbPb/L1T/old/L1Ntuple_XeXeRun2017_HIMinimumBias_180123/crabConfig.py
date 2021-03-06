from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "L1Ntuple_XeXeRun2017_HIMinimumBias"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "l1Ntuple_RAW2DIGI_FULL.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2750 # request longer runtime, ~47 hours. 2750 is the maximum guaranteed number.
# CMSSW_9_4_0_pre3
# L1 Stage2 instructions : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=123
# Specific instructions for running on XeXeRun2017 data : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=3#L1_Sample_Workflow
# l1Ntuple_RAW2DIGI_FULL.py is created after calling ./createConfigs.sh

config.section_("Data")
config.Data.userInputFiles = open('inputFiles.txt').readlines()
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 3
config.Data.totalUnits = -1

config.Data.outputPrimaryDataset = "L1Trigger"
config.Data.outputDatasetTag = "L1Ntuple_XeXeRun2017_HIMinimumBias"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
