from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_PbPb2018_GEN_SIM"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "step_GEN_SIM.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## CMSSW_10_3_0
## gen fragment : https://github.com/cms-sw/cmssw/blob/master/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 2500
config.Data.totalUnits = 500000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_PbPb2018_GEN_SIM"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
