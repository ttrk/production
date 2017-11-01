from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrDijet30_pp_CUETP8M1_5020GeV_RAW2DIGI_L1Reco_RECO_phoIso"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_pp_RAW2DIGI_L1Reco_RECO_phoIso.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2880    # request longer runtime, 48 hours.
# CMSSW_9_2_12_patch1
# cmsDriver commands : https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017PrivateMC?rev=13#cmsDriver_Commands
# default RECO + add photonIsolationHIProducer objects
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/4386.html
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017PrivateMC?rev=13#Available_Semi_Private_Samples

config.section_("Data")
config.Data.inputDataset = "/Pythia8_EmEnrDijet30_pp_CUETP8M1_5020GeV/gsfs-RAW_20171002-f5c51db4d3712eae044fcbfa9ecb19c0/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "RAW2DIGI_L1Reco_RECO"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
