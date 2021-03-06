from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## CMSSW_10_3_3_patch1

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_GEN_SIM_PU-7ba5790c40aea395650685aeed09e1f3/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
