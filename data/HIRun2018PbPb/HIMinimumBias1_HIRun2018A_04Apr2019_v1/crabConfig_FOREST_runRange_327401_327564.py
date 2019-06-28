from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIMinimumBias1_HIRun2018A_04Apr2019_v1_Run327401_327564_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/419b0eb45d6fc64bf427dcc668c46ebf2aa33921
# runForestAOD_pponAA_DATA_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits and doPhoERegression + activate l1object + HLT photon filter
# https://github.com/CmsHI/cmssw/commit/a7368e9ee00017993af087b6265f97023d98c14b
# relevant DAS query : summary dataset=/HIMinimumBias1/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.06.18 : Number of blocks: 265 Number of events: 217067743 Number of files: 35184 Number of lumis: 41293 sum(file_size): 103672587054982 (103.7TB)

config.section_("Data")
config.Data.inputDataset = "/HIMinimumBias1/HIRun2018A-04Apr2019-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
config.Data.runRange = "327401-327564"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-04Apr2019-v1-Run327401-327564-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_Vanderbilt"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
