from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_Pythia8_Ze10e10'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
# config.JobType.maxMemoryMB = 3500
# https://github.com/CmsHI/cmssw/commit/4040e9a38ec26f96541a07c17d09efec9c99db51
# runForestAOD_pp_MC_75X.py commit
# https://github.com/CmsHI/cmssw/commit/746b5cde271c0e27629823699677aaf5d2162f26

config.section_('Data')
config.Data.inputDataset = '/Pythia8_Ze10e10/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3_ext1-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3_ext1-v1-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/official/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

