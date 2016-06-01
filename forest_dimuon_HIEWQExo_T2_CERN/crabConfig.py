from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_dimuon_HIEWQExo'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'

config.section_('Data')
config.Data.inputDataset = '/HIEWQExo/katatar-HIRun2015-PromptReco-v1-AOD-dimuon-skim-4f10cc0edb1df2aaccd97a62c3f32713/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dimuon-skim-FOREST'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

