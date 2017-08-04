from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_dielectron_HIPhoton40AndZ'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
# config.JobType.maxMemoryMB = 3500
# https://github.com/CmsHI/cmssw/commit/4040e9a38ec26f96541a07c17d09efec9c99db51
# runForestAOD_PbPb_DATA_75X.py commit
# https://github.com/CmsHI/cmssw/commit/6cc1e195d3f16a7fd5278191dde31321d13058a4

config.section_('Data')
config.Data.inputDataset = '/HIPhoton40AndZ/azsigmon-HIRun2015E-PromptReco-AOD-DielectronSkim-ElePt8-v3-f8ca4a1d94c645c1a352f0d31009e079/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dielectron-skim-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT", "T2_HU_Budapest"]
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

