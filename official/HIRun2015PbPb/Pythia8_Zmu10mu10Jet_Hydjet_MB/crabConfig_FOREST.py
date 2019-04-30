from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_Pythia8_Zmu10mu10Jet_Hydjet_MB'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.maxMemoryMB = 3500
# https://github.com/CmsHI/cmssw/tree/4a2ae079f7108bbec72bf36014f136a35bb5be66

config.section_('Data')
config.Data.inputDataset = '/Pythia8_Zmu10mu10Jet_Hydjet_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/official/'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

