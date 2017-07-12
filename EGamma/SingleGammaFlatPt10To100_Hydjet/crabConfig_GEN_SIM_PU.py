from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_7_5_8_patch7
## gen fragment : https://github.com/cms-sw/cmssw/blob/CMSSW_8_1_X/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py
## modify it to SingleGammaFlatPt10To100_pythia8_cfi.py

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 500
config.Data.totalUnits = 200000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
