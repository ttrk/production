from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCD_pThat_30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8_DIGI_ECAL_ZS_EB_EE_4_SR_HI_4_MI_2"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI.py"
config.JobType.maxMemoryMB = 3500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
config.JobType.inputFiles = ["EcalSRSettings_mod.db"]

## software : CMSSW_10_3_2
# relevant DAS query : summary dataset=/QCD_pThat-30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8/HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v2/GEN-SIM
#   output on 2021.10.21 : Number of blocks: 3 Number of events: 1112949 Number of files: 293 Number of lumis: 1756 sum(file_size): 1015866211485 (1.0TB)

config.section_("Data")
config.Data.inputDataset = "/QCD_pThat-30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8/HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v2/GEN-SIM"
config.Data.inputDBS = "global"
#Invalid CRAB configuration: Parameter Data.splitting has an invalid value ('EventBased').
#Analysis job type only supports the following splitting algorithms (plus 'Automatic' as of CMSSW_7_2_X): ['FileBased', 'LumiBased', 'EventAwareLumiBased', 'Automatic'].
#The documentation about the CRAB configuration file can be found in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 2 # --> Aim to split a file into ~3 jobs, there are ~6 lumis per file
config.Data.totalUnits = 880 # --> Aim to process ~1/2 of the dataset, it has ~1760 lumis in total
config.Data.outputDatasetTag = "HINPbPbAutumn18GSHIMix-103X_upgrade2018_realistic_HI_v11-v2_DIGI_ECAL_ZS_EB_EE_4_SR_HI_4_MI_2"
config.Data.outLFNDirBase = "/store/user/katatar/run3/ECAL/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_2 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
config.JobType.allowUndistributedCMSSW = True

