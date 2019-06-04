from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleMuon_Run2017G_17Nov2017_v1_Cert_306546_306826_filterZMM_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_94X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/d6552e407f413e64561cf9a2e8126c69419933f5
# runForestAOD_pp_DATA_94X.py commit + Z->mu+mu filter
# https://github.com/CmsHI/cmssw/commit/d6552e407f413e64561cf9a2e8126c69419933f5
# relevant DAS query : summary dataset=/SingleMuon/Run2017G-17Nov2017-v1/AOD
#   output on 2019.05.22 : Number of blocks: 218 Number of events: 803534397 Number of files: 12114 Number of lumis: 26517 sum(file_size): 37808141380608 (37.8TB)

config.section_("Data")
config.Data.inputDataset = "/SingleMuon/Run2017G-17Nov2017-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 50
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017G-17Nov2017-v1-Cert-306546-306826-filterZMM-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_ES_CIEMAT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
