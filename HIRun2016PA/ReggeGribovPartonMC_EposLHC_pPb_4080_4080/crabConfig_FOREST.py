from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "ReggeGribovPartonMC_EposLHC_pPb_4080_4080_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_9
# https://github.com/CmsHI/cmssw/commit/2abaab0e60ca2bb5e009f2199868afa06dabd9fd
# runForestAOD_pPb_MC_80X.py commit
# https://github.com/CmsHI/cmssw/commit/2abaab0e60ca2bb5e009f2199868afa06dabd9fd

config.section_("Data")
config.Data.inputDataset = "/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/gsfs-EPOS_MinBias_pPb_RECO25ns_10272016-0ca207214751b2984db5b350cd35fce5/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = 500
config.Data.publication = False
config.Data.outputDatasetTag = "ReggeGribovPartonMC_EposLHC_pPb_4080_4080_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2016PA/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

