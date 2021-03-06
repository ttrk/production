from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_FOREST_userInputFiles"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/339de1c43afa0e308b5fa856f801c3d45ede01d4
## runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/339de1c43afa0e308b5fa856f801c3d45ede01d4

config.section_("Data")
#config.Data.inputDataset = "/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/katatar-HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_RAW2DIGI_L1Reco_RECO-021581694253bdfb10a34312cf24d4c7/USER"
#config.Data.inputDBS = "phys03"
config.Data.userInputFiles = open('inputFiles_das_FOREST_new.txt').readlines() # process files that became available after the 1st job, run ./grepNewInputFOREST.sh to get the list of new files wrt previous job.
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputPrimaryDataset = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018"
config.Data.outputDatasetTag = "HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

