from CRABClient.UserUtilities import config
config = config()

#### General ####
config.General.requestName = "SingleGammaFlatPt10To200_pythia8_step12" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
#config.General.workArea = "CRAB3workarea"   # Defaults to the current working directory. 
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "SingleGammaFlatPt10To200_pythia8_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

#### Data ####
# config.Data.inputDataset = "/ZEE_5TeV_GEN_SIM_PU/twang-ZEE_5TeV_GEN_SIM_PU_step2-f3950ab07bbd1716ce99d1da3e903b99/USER"
# config.Data.inputDBS = "phys03"
config.Data.primaryDataset = 'ParticleGun'
config.Data.splitting = "EventBased"
config.Data.unitsPerJob = 100
config.Data.totalUnits = 100000      #  "the parameter tells how many events to generate in total"

config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.publishDataName = "SingleGammaFlatPt10To200_pythia8_step12_753p1"  # put CMSSW release

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.blacklist = ["T0","T1"].
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
