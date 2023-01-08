from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HighEGJet_Run2017G_17Nov2017_v2_Cert_306546_306826_filterPhoPt30_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_94X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_9_4_10
# https://github.com/CmsHI/cmssw/commit/b45c68ff0f371dc10e85baf99871134c3eb2732a
# runForestAOD_pp_DATA_94X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doEleERegression + activate l1object + photon filter
# https://github.com/CmsHI/cmssw/commit/34ab4584aca8c2e47327311629ad26cd5b31f430
# relevant DAS query : summary dataset=/HighEGJet/Run2017G-17Nov2017-v2/AOD
#   output on 2019.06.17 : Number of blocks: 87 Number of events: 371094499 Number of files: 6240 Number of lumis: 27057 sum(file_size): 21093018121328 (21.1TB)

config.section_("Data")
config.Data.inputDataset = "/HighEGJet/Run2017G-17Nov2017-v2/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = 3000
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017G-17Nov2017-v2-Cert-306546-306826-filterPhoPt30-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_BE_UCL"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
