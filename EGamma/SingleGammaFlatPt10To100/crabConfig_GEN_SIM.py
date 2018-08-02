from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_GEN_SIM" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "SingleGammaFlatPt10To100_pythia8_GEN_SIM.py"
config.JobType.maxMemoryMB = 2750    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

## CMSSW_7_5_8_patch7
## gen fragment : https://github.com/cms-sw/cmssw/blob/CMSSW_10_3_X/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 400000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_GEN_SIM"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
