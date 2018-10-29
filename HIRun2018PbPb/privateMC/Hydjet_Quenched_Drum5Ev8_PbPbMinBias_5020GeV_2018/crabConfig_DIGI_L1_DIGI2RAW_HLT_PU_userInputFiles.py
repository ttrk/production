from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_DIGI_L1_DIGI2RAW_HLT_PU_userInputFiles"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## software : CMSSW_10_3_0

config.section_("Data")
#config.Data.inputDataset = "/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS-100X_upgrade2018_realistic_v10_ext1-v1/GEN-SIM"
#config.Data.inputDBS = "global"
## When this job was first submitted using the "inputDataset" option above, the dataset was still being transferred from tape to disk at T2_US_MIT (~50% complete). This option did not work, crab complained that the dataset has no copy on disk.
## My workaround was to explicitly give the input as a file list (see below) instead of giving dataset path.
## The script ./dasQueryInput.sh dumps the input file list
config.Data.userInputFiles = open('inputFiles_das.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outputPrimaryDataset = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018"
config.Data.outputDatasetTag = "HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"
config.Data.publication = True

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
