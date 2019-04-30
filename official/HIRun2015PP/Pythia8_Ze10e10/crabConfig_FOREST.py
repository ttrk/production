from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Ze10e10_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_75X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/526e9291788c0b172f349f04bbdc37f472735f8b
# runForestAOD_pp_MC_75X.py commit + add hltobject info
# https://github.com/CmsHI/cmssw/commit/f7981699dcab77b081d6f67c24f833b640d0b4d5

# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeVOfficialMC#Available_Samples
config.section_("Data")
config.Data.inputDataset = "/Pythia8_Ze10e10/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

