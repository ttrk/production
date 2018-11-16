from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "skim_HIHardProbes_RAW_run326622_userInputFiles"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "skim_RAW.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## software : CMSSW_10_3_1

config.section_("Data")
config.Data.userInputFiles = open('inputFiles_skim_RAW_326622.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.publication = False
config.Data.outputPrimaryDataset = "RAW"
config.Data.outputDatasetTag = '326622'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/HIRun2018A/HIHardProbes_skim_HLT_Photon40/'

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
#config.Site.whitelist = ["T2_CH_CERN"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
