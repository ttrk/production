from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
#### General ####
config.General.requestName = "RelValZEEMM_13_HI_GlobalEcalReco_FOREST" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
#config.General.workArea = "CRAB3workarea"   # Defaults to the current working directory. 
#config.General.transferLogs = True

config.section_("JobType")
#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "HeavyIonsAnalysis/JetAnalysis/test/runForest_PbPb_MIX_75X.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

config.section_("Data")
#### Data ####
config.Data.inputDataset = "/RelValZEEMM_13_HI/katatar-RelValZEEMM_13_HI_GlobalEcalReco_753p1-22cda6e9a70d6e0d44fe751202e88772/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/'
### config.Data.outLFNDirBase = "/store/user/katatar/"

config.Data.publishDataName = "RelValZEEMM_13_HI_GlobalEcalReco_753p1_FOREST"  # put CMSSW release

config.section_('Site')
#### Site ####
config.Site.storageSite = 'T2_CH_CERN'
###config.Site.storageSite = "T2_US_MIT"
### #config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
###config.Site.whitelist = ["T2_US_MIT"]
### #config.Site.blacklist = ["T0","T1"].
###config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
