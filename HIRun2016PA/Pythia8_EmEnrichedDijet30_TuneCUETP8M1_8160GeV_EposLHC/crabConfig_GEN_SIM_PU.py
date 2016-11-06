from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU.py"
config.JobType.pyCfgParams=["maxEventsOutput=200"]
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_8_0_22
## gen fragment : https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/pPb8TeV/Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_SingleParticleFilter_cff.py

config.section_("Data")
config.Data.outputPrimaryDataset = "HIRun2016PA"
config.Data.splitting = "EventBased"
## Filter efficiency (taking into account weights)= (10) / (2096) = 4.771e-03 +- 1.505e-03
## Filter efficiency (event-level)= (10) / (2096) = 4.771e-03 +- 1.505e-03
## conservative assumption : 4000 trials will give 10 events. Try 80000 units per job to output 200 events per job
TRIALPEROUTPUT = 400
OUTPUTPERJOB = 200
config.Data.unitsPerJob = TRIALPEROUTPUT * OUTPUTPERJOB
NJOBS = 250
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outputDatasetTag = "Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
