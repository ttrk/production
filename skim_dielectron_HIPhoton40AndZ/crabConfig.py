from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'skim_dielectron_HIPhoton40AndZ'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'skim_dielectron_HIPhoton40AndZ.py'

config.section_("Data")
config.Data.inputDataset = '/HIPhoton40AndZ/HIRun2015-PromptReco-v1/AOD'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = True
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dielectron-skim'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'
# derived from : https://github.com/azsigmon/UserCode/blob/855e8db4680addfa425f9c27306b056010a8cdb6/crabConfig.py
