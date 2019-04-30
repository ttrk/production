from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_PyquenFW_Z30eeJet_Hydjet_MB'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
# config.JobType.maxMemoryMB = 3500
# https://github.com/CmsHI/cmssw/commit/4040e9a38ec26f96541a07c17d09efec9c99db51
# runForestAOD_PbPb_MIX_75X.py commit
# https://github.com/CmsHI/cmssw/commit/28f9801376cd4663c0580d76c2e8c98fde0a744a

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeVOfficialMC#Available_Samples
config.section_('Data')
config.Data.inputDataset = '/PyquenFW_Z30eeJet_Hydjet_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/official/'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

