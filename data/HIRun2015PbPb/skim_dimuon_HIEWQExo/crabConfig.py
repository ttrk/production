from WMCore.Configuration import Configuration

config = Configuration()

# derived from : https://github.com/azsigmon/UserCode/blob/855e8db4680addfa425f9c27306b056010a8cdb6/crabConfig.py
config.section_("General")
config.General.requestName   = 'skim_dimuon_HIEWQExo'
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'skim_dimuon_HIEWQExo.py'
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.

config.section_("Data")
config.Data.inputDataset = '/HIEWQExo/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dimuon-skim'
config.Data.outLFNDirBase = '/store/user/katatar/'

config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
