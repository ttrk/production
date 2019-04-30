from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Z30eeJet_Hydjet_MB_FOREST_ext"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
config.JobType.maxMemoryMB = 2500    # request high memory.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/526e9291788c0b172f349f04bbdc37f472735f8b
# runForestAOD_PbPb_MIX_75X.py commit + add hltobject info
# https://github.com/CmsHI/cmssw/commit/336108879815bf68a856f23a7a47254ef87347fd

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeVOfficialMC#Available_Samples
config.section_("Data")
config.Data.inputDataset = "/Pythia8_Z30eeJet_Hydjet_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13_ext1-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13_ext1-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

