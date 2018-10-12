from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "XeXeRun2017_HIMinimumBias8_hltPbPb2018Photons_V11"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hltConfig.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26
# software : CMSSW_10_3_0_pre5
# L1 tag : no tag

config.section_("Data")
config.Data.inputDataset = "/HIMinimumBias8/XeXeRun2017-v1/RAW"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "XeXeRun2017_hltPbPb2018Photons_V11"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/HLT/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

