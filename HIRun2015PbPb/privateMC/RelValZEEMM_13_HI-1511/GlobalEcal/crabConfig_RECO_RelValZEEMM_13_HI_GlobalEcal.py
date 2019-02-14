from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
#### General ####
config.General.requestName = "RelValZEEMM_13_HI_GlobalEcalReco_RECO" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time. 
#config.General.workArea = "CRAB3workarea"   # Defaults to the current working directory. 
#config.General.transferLogs = True

config.section_("JobType")
#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO_GlobalEcal.py"
# config.JobType.maxMemoryMB = 3000    # request high memory machines.

config.section_("Data")
#### Data ####
config.Data.inputDataset = "/RelValZEEMM_13_HI/CMSSW_7_5_3_patch1-75X_mcRun2_HeavyIon_v5-v1/GEN-SIM-DIGI-RAW-HLTDEBUG"
config.Data.inputDBS = "global"
# Invalid CRAB configuration: A local DBS instance 'phys03' was specified for reading an input dataset of tier GEN-SIM-DIGI-RAW-HLTDEBUG.
# Datasets of tier different than USER must be read from the global DBS instance; this is, set Data.inputDBS = 'global'.
# If Data.inputDBS would not be specified, the default 'global' ('https://cmsweb.cern.ch/dbs/prod/global/DBSReader') would be used.
# The documentation about the CRAB configuration file can be found in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/'
### config.Data.outLFNDirBase = "/store/user/katatar/"

config.Data.publishDataName = "RelValZEEMM_13_HI_GlobalEcalReco_753p1"  # put CMSSW release

config.section_('Site')
#### Site ####
config.Site.storageSite = 'T2_CH_CERN'
###config.Site.storageSite = "T2_US_MIT"
### #config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
###config.Site.whitelist = ["T2_US_MIT"]
### #config.Site.blacklist = ["T0","T1"].
###config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
