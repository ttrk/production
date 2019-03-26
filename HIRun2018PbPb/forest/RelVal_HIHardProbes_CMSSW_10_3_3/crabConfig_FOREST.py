from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIHardProbes_CMSSW_10_3_3_103X_dataRun2_Prompt_v2_RelVal_hi2018hardprobes_v1_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/c5058c956d1bb5cc638843508c0911e3585d1f2f
# runForestAOD_pponAA_DATA_103X.py commit
# https://github.com/CmsHI/cmssw/commit/50a89ae749941e27ce6cb21ab64bd5d3a1e19224
## related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5731.html

config.section_("Data")
config.Data.inputDataset = "/HIHardProbes/CMSSW_10_3_3-103X_dataRun2_Prompt_v2_RelVal_hi2018hardprobes-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_3-103X_dataRun2_Prompt_v2_RelVal_hi2018hardprobes-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/relval/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_Vanderbilt"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
