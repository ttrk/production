from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat-15_TuneCP5_PbPb_5p02TeV_pythia8-HINPbPbAutumn18DR-NoPU_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/2a535687ab6f7dc031360cb15f8782782a0124a3
## runForestAOD_pponAA_MIX_103X.py commit + enable ggHiNtuplizerGED.doEffectiveAreas
# https://github.com/CmsHI/cmssw/commit/2a535687ab6f7dc031360cb15f8782782a0124a3

## Sample is pp_on_AA reco and not embedded.
config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-15_TuneCP5_PbPb_5p02TeV_pythia8/HINPbPbAutumn18DR-NoPU_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-NoPU_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

