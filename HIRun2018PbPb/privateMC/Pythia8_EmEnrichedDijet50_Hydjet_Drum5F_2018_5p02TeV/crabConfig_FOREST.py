from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/22232ae3424ac51071eb534473185eb39fbb57ec
## runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas
# https://github.com/CmsHI/cmssw/commit/a7368e9ee00017993af087b6265f97023d98c14b

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_RAW2DIGI_L1Reco_RECO-0734d2cedcdb448045aea7690e4fbf8b/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 3
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

