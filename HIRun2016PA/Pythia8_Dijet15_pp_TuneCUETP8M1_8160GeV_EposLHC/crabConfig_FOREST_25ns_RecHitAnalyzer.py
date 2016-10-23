from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns_RecHitAnalyzer"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X_RecHitAnalyzer.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_9 + modified RecHitTreeProducer.cc 
# https://github.com/CmsHI/cmssw/commit/69069ccfd82aca7a9c03b1d99621ddb50e1120b2
# https://github.com/ttrk/cmssw/commit/901090ed57a1cb421ada9ddfc78d6493c71e4a6b
# runForestAOD_pPb_MC_80X.py commit
# https://github.com/CmsHI/cmssw/commit/766cbfe8be482ee772f88f74c736d4973c2f7ef7

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_EposLHC_RAW2DIGI_L1Reco_RECO_25ns-a359d74308cab7409ddd3a416f029652/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns_RecHitAnalyzer"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

