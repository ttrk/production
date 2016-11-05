from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton15_EposLHC_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_22
# https://github.com/CmsHI/cmssw/commit/a84c4223643b17bf7b2a6d1f263793a0f8cd82db
# runForestAOD_pPb_MC_80X.py with commit
# https://github.com/CmsHI/cmssw/commit/8eb76699d997f6bb8e1b85891417b3c53a537d7d
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3438/1.html

config.section_("Data")
config.Data.inputDataset = "/AllQCDPhoton15_GEN_SIM_v2/gsfs-AllQCDPhoton15_pPb_RECO25ns_v2_11032016-0ca207214751b2984db5b350cd35fce5/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton15_EposLHC_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2016PA/semiprivate/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

