from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "RelValPyquen_GammaJet_pt20_2760GeV_CMSSW_10_3_0_patch1-HI_v7-v1-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/2c806f88506f7ef732b725142ae85750a31dc646
## runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/29f334a77a1ca0983af373ab84e6957078688734

## Sample is pp_on_AA reco and embedded.
config.section_("Data")
config.Data.inputDataset = "/RelValPyquen_GammaJet_pt20_2760GeV/CMSSW_10_3_0_patch1-PU_103X_upgrade2018_realistic_HI_v7_HS-v1/GEN-SIM-RECO"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_0_patch1-PU_103X_upgrade2018_realistic_HI_v7_HS-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/relval/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

