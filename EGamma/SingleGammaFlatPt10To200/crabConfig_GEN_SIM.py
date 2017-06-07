from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_GEN_SIM" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "SingleGammaFlatPt10To200_pythia8_GEN_SIM.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_7_5_7_patch3
## gen fragment : https://github.com/cms-sw/cmssw/blob/CMSSW_8_1_X/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py
## modify it to SingleGammaFlatPt10To200_pythia8_cfi.py

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 500
config.Data.totalUnits = 100000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "SingleGammaFlatPt10To200_pythia8_GEN_SIM"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
