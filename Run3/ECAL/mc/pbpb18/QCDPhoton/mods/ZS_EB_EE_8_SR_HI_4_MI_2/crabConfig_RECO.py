from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat_15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RECO.py"
config.JobType.maxMemoryMB = 9600    # Need to adjust parameters for the number of cores used. As CRAB warns you to "request the correct amount of memory since the default 'maxMemoryMB' value is meant for single core jobs".
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
config.JobType.numCores = 8   # Needs to match the "process.options.numberOfThreads" in pset config. Simply remove this line and "numberOfThreads" and "numberOfStreams" option lines from the pset config if you do not prefer to run multi-threaded

## software : CMSSW_10_3_2

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/katatar-HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1_DIGI_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2-879148316a8931ae0513dadd46ece4e7/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1_RECO_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"
config.Data.outLFNDirBase = "/store/user/katatar/run3/ECAL/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_2 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
#config.JobType.allowUndistributedCMSSW = True
