from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU.py"
config.JobType.pyCfgParams=["maxEventsOutput=50"]
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_8_0_15 + manually merged PR : https://github.com/cms-sw/cmssw/pull/15573
## gen fragment : https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/pPb8TeV/Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_cff.py

config.section_("Data")
config.Data.outputPrimaryDataset = "HIRun2016PA"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 125000
config.Data.totalUnits = 125000000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
