from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HISingleMuon_HIRun2018A_04Apr2019_v1_Cert_326381_327564_filterZMM_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/ba8faf19f2c60adc8318182a386eb8ffa3dea9b2
# runForestAOD_pponAA_DATA_103X.py commit + Z->mu+mu filter
# https://github.com/CmsHI/cmssw/commit/a7368e9ee00017993af087b6265f97023d98c14b
# relevant DAS query : summary dataset=/HISingleMuon/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.05.21 : Number of blocks: 112 Number of events: 56204863 Number of files: 10357 Number of lumis: 41725 sum(file_size): 58311315642652 (58.3TB)

config.section_("Data")
config.Data.inputDataset = "/HISingleMuon/HIRun2018A-04Apr2019-v1/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 50
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HIRun2018A-04Apr2019-v1-Cert-326381-327564-filterZMM-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
