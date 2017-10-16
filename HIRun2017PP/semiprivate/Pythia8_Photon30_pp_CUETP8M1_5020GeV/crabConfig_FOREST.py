from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Photon30_pp_CUETP8M1_5020GeV_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_92X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# forest_CMSSW_9_2_13
# https://github.com/CmsHI/cmssw/commit/a273e5eed739441a59084ec674c0e52bff1b3cfb
# runForestAOD_pp_MC_92X.py commit + turn off recoPhotonHiIsolationMap
# https://github.com/CmsHI/cmssw/commit/0256ffde25a7c62c11cbafe09cedeea743bea303
# related : 
# https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/4386.html
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017PrivateMC?rev=11#Available_Semi_Private_Samples

config.section_("Data")
config.Data.inputDataset = "/Pythia8_Photon300_pp_CUETP8M1_5020GeV/gsfs-RECO__201711004-b3ceaa6c7c762fab18b245ad1faf35c4/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

