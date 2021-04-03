from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat-30_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_HINPbPbAutumn18DR-mva98_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/e057db28daa87a62700fbf5ec88235a858bce602
# runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, doEleERegression, and doSuperClusters + activate l1object + add event plane info
# https://github.com/CmsHI/cmssw/commit/063ee4bc563cb393c2cfb407a5bb5f62c78c2763
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-30_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

