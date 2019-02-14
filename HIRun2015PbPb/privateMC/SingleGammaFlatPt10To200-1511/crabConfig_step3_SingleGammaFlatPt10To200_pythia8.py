from CRABClient.UserUtilities import config
config = config()

#### General ####
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_step3" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
#config.General.workArea = "CRAB3workarea"   # Defaults to the current working directory. 
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

#### Data ####
config.Data.inputDataset = "/ParticleGun/katatar-SingleGammaFlatPt10To200_pythia8_step12_753p1-900878243c0911c39eb1d36b043f870b/USER"
config.Data.inputDBS = "phys03"
# config.Data.primaryDataset = "ParticleGun"   # Analysis job type with input dataset does not accept a primary dataset name to be specified.
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.publishDataName = "SingleGammaFlatPt10To200_pythia8_step3_753p1"  # put CMSSW release

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.blacklist = ["T0","T1"].
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
