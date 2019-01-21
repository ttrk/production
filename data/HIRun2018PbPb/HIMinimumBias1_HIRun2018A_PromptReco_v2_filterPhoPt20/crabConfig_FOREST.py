from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIMinimumBias1_HIRun2018A_PromptReco_v2_Cert_326381_327489_filterPhoPt20_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1 + https://github.com/CmsHI/cmssw/pull/181
# https://github.com/CmsHI/cmssw/commit/c7f3965701a3c003397ae76e6cfc8b6d4b2e13c8
# runForestAOD_pponAA_DATA_103X.py commit + reco photon filter
# https://github.com/CmsHI/cmssw/commit/2e95972ab40f47896de9c650f9e370b264c02319
# relevant DAS query : summary run between [326381, 327489] dataset=/HIMinimumBias1/HIRun2018A-PromptReco-v2/AOD
#   output on 2019.01.18 : Number of blocks: 74 Number of events: 117183101 Number of files: 18218 Number of lumis: 20667 sum(file_size): 53536043144572 (53.5TB)

config.section_("Data")
config.Data.inputDataset = "/HIMinimumBias1/HIRun2018A-PromptReco-v2/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327489_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327489_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-PromptReco-v2-Cert-326381-327489-filterPhoPt20-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
