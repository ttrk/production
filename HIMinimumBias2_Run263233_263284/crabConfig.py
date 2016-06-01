from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'HIMinimumBias2_Run263233_263284'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'

config.section_('Data')
config.Data.inputDataset = '/HIMinimumBias2/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.runRange = '263233-263284'
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-Run263233-263284'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

