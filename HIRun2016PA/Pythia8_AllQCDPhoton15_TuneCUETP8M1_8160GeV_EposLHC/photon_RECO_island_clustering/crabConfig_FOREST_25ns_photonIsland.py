from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns_photonIsland"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_9
# https://github.com/CmsHI/cmssw/commit/2abaab0e60ca2bb5e009f2199868afa06dabd9fd
# runForestAOD_pPb_MC_80X.py with commit
# https://github.com/CmsHI/cmssw/commit/8eb76699d997f6bb8e1b85891417b3c53a537d7d

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_RAW2DIGI_L1Reco_RECO_25ns_photonIsland-e77d462890f14d8857bea10d7fcd52db/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_FOREST_25ns_photonIsland"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

