from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_DIGI_L1_DIGI2RAW_HLT_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_7_5_8_patch3

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SingleGammaFlatPt10To200_pythia8_GEN_SIM-1a7d8a1241e5328134aaa68e6e9a0633/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "SingleGammaFlatPt10To200_pythia8_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
