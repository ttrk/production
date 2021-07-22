from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIMinimumBias0_HIRun2018A_04Apr2019_v1_Run326381_326800_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/e057db28daa87a62700fbf5ec88235a858bce602
# runForestAOD_pponAA_DATA_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, doEleERegression, and doSuperClusters + activate l1object + add event plane info
# https://github.com/CmsHI/cmssw/commit/063ee4bc563cb393c2cfb407a5bb5f62c78c2763
# relevant DAS query : summary dataset=/HIMinimumBias0/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.06.28 : Number of blocks: 151 Number of events: 217186463 Number of files: 35179 Number of lumis: 41315 sum(file_size): 103737399247774 (103.7TB)
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
config.Data.inputDataset = "/HIMinimumBias0/HIRun2018A-04Apr2019-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
config.Data.runRange = "326381-326800"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-04Apr2019-v1-Run326381-326800-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_Vanderbilt"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
