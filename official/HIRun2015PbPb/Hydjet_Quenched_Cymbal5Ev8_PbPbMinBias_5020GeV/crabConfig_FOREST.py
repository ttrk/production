from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
config.JobType.maxMemoryMB = 2750    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2880    # request longer runtime, 48 hours.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/f61094f7a81de65dc1f9796236b8ed94fca888a6
# runForestAOD_PbPb_MIX_75X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/336108879815bf68a856f23a7a47254ef87347fd
# related : 
# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeVOfficialMC?rev=186#Available_Samples

config.section_("Data")
config.Data.inputDataset = "/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v14-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

