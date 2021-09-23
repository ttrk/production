from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIHardProbes_HIRun2018A_PbPb18_MiniAODv1_Cert_326381_327564_filterZEE_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "forest_miniAOD_112X_DATA.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_11_2_1_patch2
## forest_miniAOD_CMSSW_11_2_0
# https://github.com/CmsHI/cmssw/commit/a8be0f3b6c320da651cf10abad3556591890f829
# forest_miniAOD_112X_DATA.py commit + enable ggHi.doSuperClusters + Z->e+e filter
# https://github.com/CmsHI/cmssw/commit/a8be0f3b6c320da651cf10abad3556591890f829
# relevant DAS query : summary dataset=/HIHardProbes/HIRun2018A-PbPb18_MiniAODv1-v1/MINIAOD
#   output on 2021.09.21 : Number of blocks: 34 Number of events: 43596953 Number of files: 1637 Number of lumis: 41346 sum(file_size): 6100045076937 (6.1TB)

config.section_("Data")
config.Data.inputDataset = "/HIHardProbes/HIRun2018A-PbPb18_MiniAODv1-v1/MINIAOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 50
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-PbPb18_MiniAODv1-Cert-326381-327564-filterZEE-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
