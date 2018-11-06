from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SinglePi0FlatPt10To100_pythia8_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## CMSSW_10_3_0

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SinglePi0FlatPt10To100_pythia8_PbPb2018_GEN_SIM-40a7c11ccc74fe2240dbdcdae1c06b59/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "SinglePi0FlatPt10To100_pythia8_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
