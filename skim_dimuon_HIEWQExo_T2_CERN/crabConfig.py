from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'skim_dimuon_HIEWQExo'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'skim_dimuon_HIEWQExo.py'

config.section_("Data")
config.Data.inputDataset = '/HIEWQExo/HIRun2015-PromptReco-v1/AOD'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = True
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dimuon-skim'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
# derived from : https://github.com/azsigmon/UserCode/blob/855e8db4680addfa425f9c27306b056010a8cdb6/crabConfig.py