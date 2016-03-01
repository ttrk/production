from CRABClient.UserUtilities import config
config = config()

#### General ####
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_FOREST" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
#config.General.workArea = "CRAB3workarea"   # Defaults to the current working directory. 
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "HeavyIonsAnalysis/JetAnalysis/test/runForest_PbPb_MIX_75X_PhotonGun.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

#### Data ####
config.Data.inputDataset = "/ParticleGun/katatar-SingleGammaFlatPt10To200_pythia8_step3_753p1-8464e7c32dba41b93ae62574ea53b62c/USER"
config.Data.inputDBS = "phys03"
# config.Data.primaryDataset = "ParticleGun"   # Analysis job type with input dataset does not accept a primary dataset name to be specified.
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.publishDataName = "SingleGammaFlatPt10To200_pythia8_FOREST_753p1"  # put CMSSW release

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.blacklist = ["T0","T1"].
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
