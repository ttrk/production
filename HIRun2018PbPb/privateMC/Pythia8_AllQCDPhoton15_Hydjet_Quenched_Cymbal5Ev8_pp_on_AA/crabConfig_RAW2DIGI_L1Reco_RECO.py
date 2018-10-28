from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8_103X_RAW2DIGI_L1Reco_RECO"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## software : CMSSW_10_3_0_pre5

config.section_("Data")
config.Data.inputDataset = "/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/katatar-Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8_DIGI_L1_DIGI2RAW_HLT_PU-c269713c668aa4d7b49bd0c3c5d5dcad/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "103X_RAW2DIGI_L1Reco_RECO"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
