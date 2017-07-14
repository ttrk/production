from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/99526cd91246ee1085f59b9db49d74fd91be865a
# runForestAOD_PbPb_MIX_75X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/448b24612bc06222aa8979fc5ee3165d463f1408
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3838.html
# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeVOfficialMC?rev=178#Available_Samples

config.section_("Data")
config.Data.inputDataset = "/Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v14-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v14-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

