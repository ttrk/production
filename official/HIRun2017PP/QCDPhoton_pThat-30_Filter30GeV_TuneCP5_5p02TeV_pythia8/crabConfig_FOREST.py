from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat-30_Filter30GeV_TuneCP5_5p02TeV_pythia8_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_94X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_9_4_10
## forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/beda10b3d36f74c3a7ef19916e3e7554b21b52e8
## runForestAOD_pp_MC_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doEleERegression + activate l1object + HiGenParticleAna.etaMax = 5, ptMin = 0.4
# https://github.com/CmsHI/cmssw/commit/beda10b3d36f74c3a7ef19916e3e7554b21b52e8
# dataset summary on DAS
# Number of blocks: 4 Number of events: 873235 Number of files: 24 Number of lumis: 10000 sum(file_size): 63889034111 (63.9GB)

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-30_Filter30GeV_TuneCP5_5p02TeV_pythia8/RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v2/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v2-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

