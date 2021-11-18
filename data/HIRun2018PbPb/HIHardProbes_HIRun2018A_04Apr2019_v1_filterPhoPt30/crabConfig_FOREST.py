from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIHardProbes_HIRun2018A_04Apr2019_v1_Cert_326381_327564_filterPhoPt30_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/48abfe59b0007693a8fa385abe45064a34abdcca
# runForestAOD_pponAA_DATA_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, doEleERegression, doSuperClusters, and doEvtPlane + activate l1object + use the original (not "cleaned") PF cand collection + add event plane info + photon filter
# https://github.com/CmsHI/cmssw/commit/48abfe59b0007693a8fa385abe45064a34abdcca
# relevant DAS query : summary dataset=/HIHardProbes/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.06.17 : Number of blocks: 108 Number of events: 43654157 Number of files: 7747 Number of lumis: 41396 sum(file_size): 74107362626557 (74.1TB)
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
config.Data.inputDataset = "/HIHardProbes/HIRun2018A-04Apr2019-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = 3000
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-04Apr2019-v1-Cert-326381-327564-filterPhoPt30-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
