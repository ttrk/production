from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'Run2015E_PromptReco_v1_Run261553_262328_FOREST'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_DATA_75X.py'
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/99526cd91246ee1085f59b9db49d74fd91be865a
# runForestAOD_pp_DATA_75X.py commit + turn off photonIsolationHIProducerpp
# https://github.com/CmsHI/cmssw/commit/e1ce10c3e81078b446dd22d37a0f37f24bbf00c5

config.section_('Data')
config.Data.inputDataset = '/MinimumBias6/Run2015E-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/2761.html
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt
config.Data.lumiMask = 'Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.runRange = '261553-262328'
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'Run2015E_PromptReco_v1_Run261553_262328_FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/ttrk/production/blob/master/HIMinimumBias2_Run263233_263284/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT", "T2_US_Vanderbilt"]
