from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCDPhoton_pThat_15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_FOREST_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_3_patch1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/fff9de2a54e62debab81057f8d6f8c82c2fd3dd6
# runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/1f9264da586b55e0424c6a66b66d893af792e5f6

config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/tsheng-HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1_RECO_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2-9d6276cdc6045615bacf105699937a6f/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = 3
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v1_FOREST_ECAL_ZS_EB_EE_8_SR_HI_4_MI_2"
config.Data.outLFNDirBase = "/store/user/katatar/run3/ECAL/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_3_patch1 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
config.JobType.allowUndistributedCMSSW = True

