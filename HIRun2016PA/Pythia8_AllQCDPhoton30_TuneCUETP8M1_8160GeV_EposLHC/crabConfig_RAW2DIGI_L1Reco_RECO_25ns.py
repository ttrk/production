from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_RAW2DIGI_L1Reco_RECO_25ns" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO_25ns.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_8_0_20_patch1
## PR is merged with this release : https://github.com/cms-sw/cmssw/pull/15573

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_DIGI_L1_DIGI2RAW_HLT_PU-ff2ced84ff07ed758c83b2190318e9b0/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_EposLHC_RAW2DIGI_L1Reco_RECO_25ns"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
