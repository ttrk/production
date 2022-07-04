from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat_30_TuneCP5_5p02TeV_pythia8_RunIISummer20UL17pp_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_106X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_6_29
## forest_CMSSW_10_6_29
# https://github.com/CmsHI/cmssw/commit/6605d4e0cffbccbe8be3fffee9ee4f86bd1588a7
## runForestAOD_pp_MC_106X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doEleERegression + activate l1object + HiGenParticleAna.etaMax = 5, ptMin = 0.4
# https://github.com/CmsHI/cmssw/commit/6605d4e0cffbccbe8be3fffee9ee4f86bd1588a7
# dataset summary on DAS
# Number of blocks: 2 Number of events: 911014 Number of files: 24 Number of lumis: 1957 sum(file_size): 74724412440 (74.7GB)

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-30_TuneCP5_5p02TeV-pythia8/RunIISummer20UL17pp5TeVRECO-106X_mc2017_realistic_forppRef5TeV_v3-v2/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "RunIISummer20UL17pp5TeVRECO-106X_mc2017_realistic_forppRef5TeV_v3-v2-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/pp17/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

