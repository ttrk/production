from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "MinimumBias1_Run2015E_PromptReco_v1_Run262163_262328_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_75X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/526e9291788c0b172f349f04bbdc37f472735f8b
# runForestAOD_pp_DATA_75X.py commit
# https://github.com/CmsHI/cmssw/commit/e1ce10c3e81078b446dd22d37a0f37f24bbf00c5
# relevant DAS query : summary run between [262163, 262328] dataset=/MinimumBias1/Run2015E-PromptReco-v1/AOD
# output : Number of blocks: 20 Number of events: 125349140 Number of files: 1409 Number of lumis: 6824 sum(file_size): 1448511114411 (1.4TB)

config.section_("Data")
config.Data.inputDataset = "/MinimumBias1/Run2015E-PromptReco-v1/AOD"
config.Data.inputDBS = "global"
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/2761.html
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt
config.Data.lumiMask = "Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt"
config.Data.runRange = "262163-262328"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2015E-PromptReco-v1-Run262163-262328-Cert-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2015PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
