from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleMuon_Run2017F_17Nov2017_v1_Run_305902_306462_filterZMM_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_94X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/f734148787e379e524698e08403ef10bfff29eab
# runForestAOD_pp_DATA_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doEleERegression + activate l1object + Z->mu+mu filter
# https://github.com/CmsHI/cmssw/commit/a8d60116be530d597489d9dbdaa6c7418ff29432
# relevant DAS query : summary dataset=/SingleMuon/Run2017F-17Nov2017-v1/AOD
# Number of blocks: 266 Number of events: 242135500 Number of files: 25921 Number of lumis: 60684 sum(file_size): 79439134132157 (79.4TB)

config.section_("Data")
config.Data.inputDataset = "/SingleMuon/Run2017F-17Nov2017-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
config.Data.runRange = "305902-306462"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017F-17Nov2017-v1-Run-305902-306462-filterZMM-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/Run2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_ES_CIEMAT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
