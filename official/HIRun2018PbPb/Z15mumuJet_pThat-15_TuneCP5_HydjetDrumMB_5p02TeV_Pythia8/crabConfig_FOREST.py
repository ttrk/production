from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Z15mumuJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/d16813f245999c268ec3122c2d5d075615a026f0
## runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object + HiGenParticleAna.etaMax = 3
# https://github.com/CmsHI/cmssw/commit/3cd61293c9e92e4969db28899364949a9119f328
# dataset summary on DAS
# Number of blocks: 8 Number of events: 981692 Number of files: 336 Number of lumis: 1000 sum(file_size): 1111706307849 (1.1TB)

config.section_("Data")
config.Data.inputDataset = "/Z15mumuJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v1/AODSIM"
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

