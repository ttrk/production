from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_GEN_SIM" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "step1_GEN_SIM.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

#Given your input parameters, each output file will contain around 2000 lumis.
#Please modify your configuration so that the output files contain at most 1000 lumis. You can do so by increasing the 'config.JobType.eventsPerLumi' parameter or by decreasing the 'config.Data.totalUnits', 'config.Data.unitsPerJob' parameters.
config.JobType.eventsPerLumi = 1000

# software : CMSSW_12_5_0_pre5
## gen fragment : https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py
# !! modify the collision energy to sqrt(s) = 5.36 TeV and change bias2SelectionPow from 2 to 4

config.section_("Data")
config.Data.outputPrimaryDataset = "run3"
config.Data.splitting = "EventBased"
# Filter efficiency is 5.200e-03 (52 out of 10K events passed filter)
config.Data.unitsPerJob = 200000 # Events to generate per job to get ~1K events in the outout
config.Data.totalUnits = 21000000      #  "the parameter tells how many events to generate in total"

config.Data.outputDatasetTag = "run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_GEN_SIM"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
