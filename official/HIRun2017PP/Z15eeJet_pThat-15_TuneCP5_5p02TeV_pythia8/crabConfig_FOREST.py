from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Z15eeJet_pThat-15_TuneCP5_5p02TeV_pythia8_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_94X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_9_4_10
## forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/a06e2f34edb4997ec9d7c9363d511d5eecac00ce
## runForestAOD_pp_MC_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object + HiGenParticleAna.etaMax = 5, ptMin = 0.4
# https://github.com/CmsHI/cmssw/commit/13ef2e83536987c958abeb141988de347620152e
# dataset summary on DAS
# Number of blocks: 7 Number of events: 998438 Number of files: 30 Number of lumis: 1001 sum(file_size): 77166282156 (77.2GB)

config.section_("Data")
config.Data.inputDataset = "/Z15eeJet_pThat-15_TuneCP5_5p02TeV_pythia8/RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v1/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV_v1-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

