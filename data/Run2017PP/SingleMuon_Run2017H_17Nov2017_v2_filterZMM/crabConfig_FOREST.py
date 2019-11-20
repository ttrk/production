from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleMuon_Run2017H_17Nov2017_v2_Cert_306896_307082_filterZMM_FOREST"
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
# relevant DAS query : summary dataset=/SingleMuon/Run2017H-17Nov2017-v2/AOD
# Number of blocks: 28 Number of events: 138683027 Number of files: 2731 Number of lumis: 12675 sum(file_size): 10014140903843 (10.0TB)

config.section_("Data")
config.Data.inputDataset = "/SingleMuon/Run2017H-17Nov2017-v2/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_306896-307082_13TeV_EOY2017ReReco_Collisions17_JSON_LowPU.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_306896-307082_13TeV_EOY2017ReReco_Collisions17_JSON_LowPU.txt
#config.Data.runRange = "306896-307082"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 40
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017H-17Nov2017-v2-Cert-306896-307082-filterZMM-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/Run2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_ES_CIEMAT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
