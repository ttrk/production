from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_DIGI_L1_DIGI2RAW_HLT_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_8_0_22

config.section_("Data")
config.Data.inputDataset = "/HIRun2016PA/katatar-Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU-f9287401c69a5473cbdda6ea20e3477d/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
