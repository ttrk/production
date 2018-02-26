from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Ze10e10_Hydjet_MB_RAW2DIGI_L1Reco_RECO_extendEC"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO_extendEC.py"
config.JobType.maxMemoryMB = 2750    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2880    # request longer runtime, 48 hours.

config.section_("Data")
config.Data.inputDataset = "/Pythia8_Ze10e10_Hydjet_MB/katatar-HiFall15-75X_mcRun2_HeavyIon_v1_ext1-v1_DIGI_L1_DIGI2RAW_HLT_PU-45c59ec33286119d805716e48788f963/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "HiFall15-75X_mcRun2_HeavyIon_v1_ext1-v1_RAW2DIGI_L1Reco_RECO_extendEC"
config.Data.outLFNDirBase = "/store/user/katatar/EGamma/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
