from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "AllQCDPhoton_pThat30_pPb816_Pythia8_EPOS_pPb816Summer16DR_80X_mcRun2_asymptotic_v17_v1"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_8_0_22
# https://github.com/CmsHI/cmssw/commit/6f5fea4e7325cbdf38aafbae5aeb6177a8d158b5
# runForestAOD_pPb_MC_80X.py with commit + commented out "centralityBin" and "hiFJRhoAnalyzer"
# https://github.com/CmsHI/cmssw/commit/5f80b18a63a6006b1e2d2773baa213c88705a5d0
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3587.html
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3561.html

config.section_("Data")
config.Data.inputDataset = "/AllQCDPhoton_pThat30_pPb816_Pythia8_EPOS/pPb816Summer16DR-80X_mcRun2_asymptotic_v17-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "AllQCDPhoton_pThat30_pPb816_Pythia8_EPOS_pPb816Summer16DR_80X_mcRun2_asymptotic_v17_v1"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

