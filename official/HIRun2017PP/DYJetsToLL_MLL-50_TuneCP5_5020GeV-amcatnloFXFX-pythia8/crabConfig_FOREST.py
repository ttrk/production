from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "DYJetsToLL_MLL-50_TuneCP5_5020GeV-amcatnloFXFX-pythia8-RunIIpp5Spring18DR-FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_94X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/2490dda4272fbc13f926d7a42e31c52fbed5bb6f
## runForestAOD_pp_MC_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits + activate l1object
# https://github.com/CmsHI/cmssw/commit/1b1218afdef53fbc11cbd5308b71b5be3d983aef
# relevant DAS query : summary dataset=/DYJetsToLL_MLL-50_TuneCP5_5020GeV-amcatnloFXFX-pythia8/RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV-v2/AODSIM
#   output on 2019.06.22 : Number of blocks: 14 Number of events: 9992985 Number of files: 143 Number of lumis: 10002 sum(file_size): 754314483531 (754.3GB)

config.section_("Data")
config.Data.inputDataset = "/DYJetsToLL_MLL-50_TuneCP5_5020GeV-amcatnloFXFX-pythia8/RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV-v2/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "RunIIpp5Spring18DR-94X_mc2017_realistic_forppRef5TeV-v2-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
