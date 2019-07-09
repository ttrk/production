from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "ParkingL1MinimumBias6_Run2017G_17Nov2017_v1_Cert_306546_306826_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_94X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/46971e47aff6f52f6b4eb4ec5a2d5351a3f81271
# runForestAOD_pp_DATA_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object
# https://github.com/CmsHI/cmssw/commit/46971e47aff6f52f6b4eb4ec5a2d5351a3f81271
# relevant DAS query : summary dataset=/ParkingL1MinimumBias6/Run2017G-17Nov2017-v1/AOD
#   output on 2019.07.02 : Number of blocks: 27 Number of events: 108674509 Number of files: 410 Number of lumis: 1376 sum(file_size): 1328771861437 (1.3TB)

config.section_("Data")
config.Data.inputDataset = "/ParkingL1MinimumBias6/Run2017G-17Nov2017-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017G-17Nov2017-v1-Cert-306546-306826-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
