from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_PbPb2018_RAW2DIGI_L1Reco_RECO_extendEC"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO_extendEC.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## CMSSW_10_3_0

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SingleGammaFlatPt10To100_pythia8_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU-fa171a86177d1547bc3842dad7f76662/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_PbPb2018_RAW2DIGI_L1Reco_RECO_extendEC"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
