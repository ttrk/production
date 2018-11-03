from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "RelValPyquen_GammaJet_pt20_2760GeV_CMSSW_10_3_0_HI_v6"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_102X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_0_pre5
## forest_CMSSW_10_2_0_mergeable_103X
# https://github.com/bi-ran/cmssw/commit/881f735e47737d71e9888562d909e84a80371161
## runForestAOD_pponAA_MIX_102X.py commit
# https://github.com/bi-ran/cmssw/commit/63f2698a3718a1a4835359b52014c6ee42b54a7a

## Sample is pp_on_AA reco and embedded.
config.section_("Data")
config.Data.inputDataset = "/RelValPyquen_GammaJet_pt20_2760GeV/CMSSW_10_3_0-PU_103X_upgrade2018_realistic_HI_v6-v1/GEN-SIM-RECO"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_0-PU_103X_upgrade2018_realistic_HI_v6-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/relval/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

