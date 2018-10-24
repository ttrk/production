from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "RelValPhotonJets_Pt_10_13_HI_CMSSW_10_3_0_pre4_PU_103X_upgrade2018_realistic_v4_v1"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_HI_MIX_102X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_0_pre5
## forest_CMSSW_10_2_0_mergeable_103X
# https://github.com/bi-ran/cmssw/commit/90846e5ec6882737e1a1d48c7b9ad0daabc3ed60
## runForestAOD_HI_MIX_102X.py commit
# https://github.com/bi-ran/cmssw/commit/3bdbe8578bfe01e9161fa84526b623b1a0d350ee

## Sample is HI reco and not embedded.
config.section_("Data")
config.Data.inputDataset = "/RelValPhotonJets_Pt_10_13_HI/CMSSW_10_3_0_pre4-PU_103X_upgrade2018_realistic_v4-v1/GEN-SIM-RECO"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_0_pre4-PU_103X_upgrade2018_realistic_v4-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/relval/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

