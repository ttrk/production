from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_EPOS_pPb_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_MC_80X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# forest_CMSSW_8_0_28
# https://github.com/CmsHI/cmssw/commit/2a98de4fd42df8939abf6f285f3194264be008cc
# runForestAOD_pPb_MC_80X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/dba39702f3d92502b5dcc68f820b09ec5d21190a
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/4162.html
# https://twiki.cern.ch/twiki/bin/view/CMS/PPb8TeVOfficialMC?rev=77#Available_Samples

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-30_pPb-EmbEPOS_8p16_Pythia8/pPb816Summer16DR-pPbEmb_80X_mcRun2_pA_v4-v3/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "pPb816Summer16DR-pPbEmb_80X_mcRun2_pA_v4-v3-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

