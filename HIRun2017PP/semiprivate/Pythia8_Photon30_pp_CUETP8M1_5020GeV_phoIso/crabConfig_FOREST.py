from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Photon30_pp_CUETP8M1_5020GeV_FOREST_phoIso"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_92X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# forest_CMSSW_9_2_13
# https://github.com/CmsHI/cmssw/commit/1747f0107244afe808523f316e21ebd08271f1f2
# runForestAOD_pp_MC_92X.py commit
# https://github.com/CmsHI/cmssw/commit/0256ffde25a7c62c11cbafe09cedeea743bea303
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/4386.html
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017PrivateMC?rev=13#Available_Semi_Private_Samples

config.section_("Data")
config.Data.inputDataset = "/Pythia8_Photon300_pp_CUETP8M1_5020GeV/katatar-RAW2DIGI_L1Reco_RECO-529ccce99e7757edd946324107b3e873/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "FOREST_phoIso"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

