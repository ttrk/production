from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIRun2018PbPb_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_102X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## Sample listed at https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=70#To_be_produced
## software : CMSSW_10_3_0_pre5
## forest_CMSSW_10_2_0_mergeable_103X
# https://github.com/bi-ran/cmssw/commit/d80e9a4aa39abb264d54d1751b96d5f7ac8d55fd
## runForestAOD_pponAA_MIX_102X.py commit
# https://github.com/bi-ran/cmssw/commit/d80e9a4aa39abb264d54d1751b96d5f7ac8d55fd

config.section_("Data")
config.Data.inputDataset = "/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/rbi-crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_RECO_PU_1030_v2-f3d99479d440e0ea703da4f927d6c1fe/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_0-103X_upgrade2018_realistic_HI_v7-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

