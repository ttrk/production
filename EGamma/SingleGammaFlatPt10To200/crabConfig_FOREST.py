from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_FOREST"
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X_particleGun.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/53af260105556aefb496772cdf7e7fe2bb65e328
# runForestAOD_PbPb_MIX_75X.py commit
# https://github.com/CmsHI/cmssw/commit/28f9801376cd4663c0580d76c2e8c98fde0a744a

# runForestAOD_PbPb_MIX_75X_particleGun.py is a modified version of runForestAOD_PbPb_MIX_75X.py where
# 1. process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
# 2. removing some jet sequences

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SingleGammaFlatPt10To200_pythia8_RAW2DIGI_L1Reco_RECO-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "SingleGammaFlatPt10To200_pythia8_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

