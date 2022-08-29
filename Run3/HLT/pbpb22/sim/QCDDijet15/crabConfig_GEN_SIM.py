from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pbpb22_privateMC_QCDDijet15_pythia8_GEN_SIM" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "step1_GEN_SIM.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

## software : CMSSW_12_4_0
## gen fragment : https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00075

config.section_("Data")
config.Data.outputPrimaryDataset = "run3"
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 2000
config.Data.totalUnits = 10500000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "run3_pbpb22_privateMC_QCDDijet15_pythia8_GEN_SIM"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
