from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_Pythia8_Ze10e10_Hydjet_MB'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
# https://github.com/CmsHI/cmssw/tree/c86ad0ac822ec2a8ffbe0ba4660a4c7627712985

config.section_('Data')
config.Data.inputDataset = '/Pythia8_Ze10e10_Hydjet_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v13-v1-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/official/'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

