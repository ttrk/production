from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_DIGI_L1_DIGI2RAW_HLT_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_8_0_15 + manually merged PR : https://github.com/cms-sw/cmssw/pull/15573

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU-653656c9f5cc1d0d4767337f1da7cfc8/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_EposLHC_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
