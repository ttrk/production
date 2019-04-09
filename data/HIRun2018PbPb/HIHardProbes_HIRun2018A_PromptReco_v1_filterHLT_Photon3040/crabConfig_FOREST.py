from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIHardProbes_HIRun2018A_PromptReco_v1_Cert_326381_327564_filterHLT_Photon3040_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/99e9e5d12c52f8607c1fd432b1397f3cfb29fb42
# runForestAOD_pponAA_DATA_103X.py commit + activate l1object + HLT photon filter
# https://github.com/CmsHI/cmssw/commit/50a89ae749941e27ce6cb21ab64bd5d3a1e19224
# relevant DAS query : summary dataset=/HIHardProbes/HIRun2018A-PromptReco-v1/AOD
#   output on 2019.03.04 : Number of blocks: 68 Number of events: 11524334 Number of files: 5205 Number of lumis: 17083 sum(file_size): 19448265801545 (19.4TB)

config.section_("Data")
config.Data.inputDataset = "/HIHardProbes/HIRun2018A-PromptReco-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 6
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-PromptReco-v1-Cert-326381-327564-filterHLT-Photon3040-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
