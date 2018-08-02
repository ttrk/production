from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To100_pythia8_FOREST_extendEC"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X_particleGun.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/526e9291788c0b172f349f04bbdc37f472735f8b
# runForestAOD_PbPb_MIX_75X.py commit
# https://github.com/CmsHI/cmssw/commit/336108879815bf68a856f23a7a47254ef87347fd

# runForestAOD_PbPb_MIX_75X_particleGun.py is a modified version of runForestAOD_PbPb_MIX_75X.py where
# 1. process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
#    process.ggHiNtuplizer.doRecHitsEB = cms.bool(True)   # see https://github.com/CmsHI/cmssw/commit/526e9291788c0b172f349f04bbdc37f472735f8b
#    process.ggHiNtuplizer.doRecHitsEE = cms.bool(True)
# 2. removing some Njettiness sequences

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SingleGammaFlatPt10To100_pythia8_RAW2DIGI_L1Reco_RECO_extendEC-326bb9c314693b96d5f8d2242ec00957/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "SingleGammaFlatPt10To100_pythia8_FOREST_extendEC"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

