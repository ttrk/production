from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_9
# https://github.com/CmsHI/cmssw/commit/69069ccfd82aca7a9c03b1d99621ddb50e1120b2
# runForestAOD_pPb_MC_80X.py commit
# https://github.com/CmsHI/cmssw/commit/766cbfe8be482ee772f88f74c736d4973c2f7ef7

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_RAW2DIGI_L1Reco_RECO_25ns-8903f9f070d6a6d315ca9abbd5d692c3/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

