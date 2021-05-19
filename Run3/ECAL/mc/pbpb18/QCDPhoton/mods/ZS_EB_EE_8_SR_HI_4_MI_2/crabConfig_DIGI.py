from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat_15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_DIGI_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"

config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI.py"
config.JobType.maxMemoryMB = 3000    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
config.JobType.inputFiles = ["EcalSRSettings_mod.db"]

## software : CMSSW_10_3_2

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = 110
config.Data.outputDatasetTag = "HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1_DIGI_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"
config.Data.outLFNDirBase = "/store/user/katatar/run3/ECAL/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_2 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
config.JobType.allowUndistributedCMSSW = True

