from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "MinBias_Hydjet_Drum5F_2018_5p02TeV_HINPbPbAutumn18DR-NoPUmva98-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MB_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/3cd61293c9e92e4969db28899364949a9119f328
## runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object
# https://github.com/CmsHI/cmssw/commit/3cd61293c9e92e4969db28899364949a9119f328
# relevant DAS query : summary dataset=/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18DR-NoPUmva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM
#   output on 2019.06.22 : Number of blocks: 83 Number of events: 960824 Number of files: 296 Number of lumis: 8143 sum(file_size): 1011380689276 (1.0TB)

config.section_("Data")
config.Data.inputDataset = "/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18DR-NoPUmva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-NoPUmva98_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
