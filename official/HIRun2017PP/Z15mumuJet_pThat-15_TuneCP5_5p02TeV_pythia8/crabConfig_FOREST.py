from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Z15mumuJet_pThat-15_TuneCP5_5p02TeV_pythia8_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_94X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_9_4_10
## forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/4da4ff7aa28955bd63082e473397eacc0e28d2ac
## runForestAOD_pp_MC_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object + HiGenParticleAna.etaMax = 5, ptMin = 0.4
# https://github.com/CmsHI/cmssw/commit/5de23a5b4ecfbe46f852c502ad5e1956fe9442b5
# dataset summary on DAS
# Number of blocks: 4 Number of events: 980356 Number of files: 31 Number of lumis: 1001 sum(file_size): 96530883531 (96.5GB)

config.section_("Data")
config.Data.inputDataset = "/Z15mumuJet_pThat-15_TuneCP5_5p02TeV_pythia8/RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

