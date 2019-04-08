from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "RelValPyquen_GammaJet_pt20_2760GeV_CMSSW_10_3_2_HI_v11-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/232631a89aea5f2b7a5b43ffc22a2f99d642b1ae
## runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/232631a89aea5f2b7a5b43ffc22a2f99d642b1ae

## Sample is pp_on_AA reco and not embedded.
config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-30_TuneCP5_PbPb_5p02TeV_pythia8_103X_upgrade2018_realistic_HI_v11/ikucher-crab_QCDPhoton_pThat-30_TuneCP5_PbPb_5p02TeV_pythia8_103X_upgrade2018_realistic_HI_v11_RECO-d2c80626fee9f1a8e69409e960d0a051/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

