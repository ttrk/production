from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/99526cd91246ee1085f59b9db49d74fd91be865a
# runForestAOD_PbPb_MIX_75X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/448b24612bc06222aa8979fc5ee3165d463f1408
# add branches for more photon SuperCluster, shower shape, BasicCluster info. Remove branches for unused/inaccessible photon variables :
# https://github.com/ttrk/cmssw/commit/80d1ab0bfda5f2031a04f5d439581b29c0a8f106
# https://github.com/ttrk/cmssw/commit/1c59f5b3b8733c7edce9605cec6b18a13b05278a

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_RAW2DIGI_L1Reco_RECO-eef725472e9d7138234fbfd165e44059/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

