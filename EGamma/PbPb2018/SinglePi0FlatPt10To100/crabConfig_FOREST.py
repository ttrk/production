from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SinglePi0FlatPt10To100_pythia8_PbPb2018_FOREST_extendEC"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/2c806f88506f7ef732b725142ae85750a31dc646
## runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/29f334a77a1ca0983af373ab84e6957078688734
# additional changes
# process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
# process.ggHiNtuplizer.doRecHitsEB = cms.bool(True)
# process.ggHiNtuplizer.doRecHitsEE = cms.bool(True)
# process.ggHiNtuplizerGED.runOnParticleGun = cms.bool(True)
# process.ggHiNtuplizerGED.doRecHitsEB = cms.bool(True)
# process.ggHiNtuplizerGED.doRecHitsEE = cms.bool(True)

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-SinglePi0FlatPt10To100_pythia8_PbPb2018_RAW2DIGI_L1Reco_RECO_extendEC-55149d7d7cb7f68a42078d6f788ccf93/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "SinglePi0FlatPt10To100_pythia8_PbPb2018_FOREST_extendEC"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

