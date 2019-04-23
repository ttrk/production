from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIHardProbes_HIRun2018A_04Apr2019_v1_Cert_326381_327564_filterHLT_Photon3040_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/232631a89aea5f2b7a5b43ffc22a2f99d642b1ae
# runForestAOD_pponAA_DATA_103X.py commit + activate l1object + HLT photon filter
# https://github.com/CmsHI/cmssw/commit/50a89ae749941e27ce6cb21ab64bd5d3a1e19224
# relevant DAS query : summary dataset=/HIHardProbes/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.04.18 : Number of blocks: 96 Number of events: 40342328 Number of files: 7031 Number of lumis: 38169 sum(file_size): 68424128694593 (68.4TB) 

config.section_("Data")
config.Data.inputDataset = "/HIHardProbes/HIRun2018A-04Apr2019-v1/AOD"
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = 5000
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-04Apr2019-v1-Cert-326381-327564-filterHLT-Photon3040-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
