from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "SingleMuon_Run2018D_22Jan2019_v2_Run_324878_325175_filterZMM_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/5c5ccb4013e2ebecfbca0ca433cb14bb36b9f1d3
# runForestAOD_pponAA_DATA_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doSuperClusters + activate l1object + add event plane info + Z->mu+mu filter + remove module that do not work in pp
# https://github.com/CmsHI/cmssw/commit/4d7967c0beee30ae2573fa9108ae9925d620c9e5
# relevant DAS query : summary dataset=/SingleMuon/Run2018D-22Jan2019-v2/AOD
# Number of blocks: Number of blocks: 231 Number of events: 514116477 Number of files: 21855 Number of lumis: 141552 sum(file_size): 149127627943882 (149.1TB)

config.section_("Data")
config.Data.inputDataset = "/SingleMuon/Run2018D-22Jan2019-v2/AOD"
config.Data.inputDBS = "global"
#config.Data.lumiMask = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt
config.Data.runRange = "324878-325175"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 25
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2018D-22Jan2019-v2-Run-324878-325175-filterZMM-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/Run2018PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_Vanderbilt"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
