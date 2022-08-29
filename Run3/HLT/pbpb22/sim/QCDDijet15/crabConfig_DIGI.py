from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time.
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

## software : CMSSW_12_4_0

config.section_("Data")
config.Data.inputDataset = "/run3/katatar-run3_pbpb22_privateMC_QCDDijet15_pythia8_GEN_SIM-74c80934a1def651c98c06c83ff8f216/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.outputDatasetTag = "run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_2 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
#config.JobType.allowUndistributedCMSSW = True

