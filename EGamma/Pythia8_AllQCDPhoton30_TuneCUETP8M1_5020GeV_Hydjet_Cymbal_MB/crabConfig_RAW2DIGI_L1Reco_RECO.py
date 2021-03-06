from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_RAW2DIGI_L1Reco_RECO"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO_extendEC.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

config.section_("Data")
config.Data.inputDataset = "/EGamma/katatar-Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_DIGI_L1_DIGI2RAW_HLT_PU-78b9224f3f720bc60119bbe0f2c55acd/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_RAW2DIGI_L1Reco_RECO"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
