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
# https://github.com/CmsHI/cmssw/commit/99526cd91246ee1085f59b9db49d74fd91be865a
# runForestAOD_PbPb_MIX_75X.py commit
# https://github.com/CmsHI/cmssw/commit/448b24612bc06222aa8979fc5ee3165d463f1408

# runForestAOD_PbPb_MIX_75X_particleGun.py is a modified version of runForestAOD_PbPb_MIX_75X.py where
# 1. process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
# 2. removing some Njettiness sequences

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

