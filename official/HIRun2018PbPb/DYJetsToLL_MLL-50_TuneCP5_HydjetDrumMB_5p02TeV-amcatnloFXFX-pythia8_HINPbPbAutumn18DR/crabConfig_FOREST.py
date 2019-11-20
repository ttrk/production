from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "DYJetsToLL_MLL-50_TuneCP5_HydjetDrumMB_5p02TeV-amcatnloFXFX-pythia8-HINPbPbAutumn18DR-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/027aac74d5dc19779d2738d9930a54b94e79d531
## runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object + HiGenParticleAna.etaMax = 3 + add event plane info
# https://github.com/CmsHI/cmssw/commit/027aac74d5dc19779d2738d9930a54b94e79d531
# relevant DAS query : summary dataset=/DYJetsToLL_MLL-50_TuneCP5_HydjetDrumMB_5p02TeV-amcatnloFXFX-pythia8/HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM
#   output on 2019.06.22 : Number of blocks: 12 Number of events: 10135351 Number of files: 3357 Number of lumis: 9985 sum(file_size): 11475621577437 (11.5TB)
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
config.Data.inputDataset = "/DYJetsToLL_MLL-50_TuneCP5_HydjetDrumMB_5p02TeV-amcatnloFXFX-pythia8/HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
