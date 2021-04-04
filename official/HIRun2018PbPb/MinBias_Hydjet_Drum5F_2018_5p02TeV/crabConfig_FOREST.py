from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "MinBias_Hydjet_Drum5F_2018_5p02TeV_HINPbPbAutumn18DR-NoPU-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MB_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/419b0eb45d6fc64bf427dcc668c46ebf2aa33921
## runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object
# https://github.com/CmsHI/cmssw/commit/a7368e9ee00017993af087b6265f97023d98c14b
# relevant DAS query : summary dataset=/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18DR-NoPU_103X_upgrade2018_realistic_HI_v11-v1/AODSIM
#   output on 2019.05.24 : Number of blocks: 8 Number of events: 999111 Number of files: 248 Number of lumis: 7868 sum(file_size): 1060981783565 (1.1TB)

config.section_("Data")
config.Data.inputDataset = "/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18DR-NoPU_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = 10
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-NoPU_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
