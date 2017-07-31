from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_GEN_SIM_PU"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_cff_py_GEN_SIM_PU.py"
config.JobType.pyCfgParams=["maxEventsOutput=300"]
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

## CMSSW_7_5_8_patch7

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
## Filter efficiency (taking into account weights)= (130) / (60000) = 2.167e-03 +- 1.898e-04
## Filter efficiency (event-level)= (130) / (60000) = 2.167e-03 +- 1.898e-04
## After filter: final cross section = 7.489e+04 +- 6.563e+03 pb
## conservative assumption : 600 trials will give 1 events. Try 120000 units per job to output 200 events per job
TRIALPEROUTPUT = 600
OUTPUTPERJOB = 200
config.Data.unitsPerJob = TRIALPEROUTPUT * OUTPUTPERJOB
NJOBS = 400  # try total output events = 80 K
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outputDatasetTag = "Pythia8_AllQCDPhoton30_TuneCUETP8M1_5020GeV_Hydjet_Cymbal_MB_GEN_SIM_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
# config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
