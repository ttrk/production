from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIMinimumBias1_HIRun2018A_PromptReco_v1_Run326500_326886_filterElePt2_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/6617c6a002b380365be9a585d5979c0d39715d69
# runForestAOD_pponAA_DATA_103X.py commit + reco electron filter
# https://github.com/CmsHI/cmssw/commit/6617c6a002b380365be9a585d5979c0d39715d69
# relevant DAS query : summary run between [326500, 326886] dataset=/HIMinimumBias1/HIRun2018A-PromptReco-v1/AOD
#   output on 18.11.24 : Number of files: 6395 Number of lumis: 9330 Number of blocks: 47 Number of events: 38214824 sum(file_size): 18140909688885 (18.1TB)

config.section_("Data")
config.Data.inputDataset = "/HIMinimumBias1/HIRun2018A-PromptReco-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "json_DCSONLY_HI.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/DCSOnly/json_DCSONLY_HI.txt
config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 30
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-PromptReco-v1-Run326500-326886-filterElePt2-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
