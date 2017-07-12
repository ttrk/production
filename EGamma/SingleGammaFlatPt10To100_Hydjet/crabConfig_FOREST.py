from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_Hydjet_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X_particleGun.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/3e925fd90c95e8cd01723a5580e721b7205cb3e9
# runForestAOD_PbPb_MIX_75X.py commit
# https://github.com/CmsHI/cmssw/commit/977c4ca9e06fe21aa7bb15bd564b24410d9e72dd

# runForestAOD_PbPb_MIX_75X_particleGun.py is a modified version of runForestAOD_PbPb_MIX_75X.py where
# 1. process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
# 2. removing some jet sequences

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SingleGammaFlatPt10To100_pythia8_Hydjet_RAW2DIGI_L1Reco_RECO-eef725472e9d7138234fbfd165e44059/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_Hydjet_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

