from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'HIMinimumBias20_XeXeRun2017_PromptReco_v1_Run304899_304906'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_XeXe_DATA_92X.py'
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# forest_CMSSW_9_2_13
# https://github.com/CmsHI/cmssw/commit/07838eae867f126edb5c95909fdd3cc8ddc29ad7
# runForestAOD_XeXe_DATA_92X.py commit + enable ggHiNtuplizer and turn off recoPhotonHiIsolationMap
# https://github.com/CmsHI/cmssw/commit/cb4076c4185a421678842718eeb29dbb06411949
# relevant DAS query : file run between [304899, 304906] dataset=/HIMinimumBias20/XeXeRun2017-PromptReco-v1/AOD | sum(file.nevents)

config.section_('Data')
config.Data.inputDataset = '/HIMinimumBias20/XeXeRun2017-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'Cert_304899-304906_XeXe_PromptReco_Collisions17_JSON.txt'
config.Data.runRange = '304899-304906'
config.Data.splitting = "EventAwareLumiBased"
config.Data.unitsPerJob = 5000
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'XeXeRun2017-v1-Run304899-304906'
config.Data.outLFNDirBase = '/store/user/katatar/HIRun2017XeXe/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_Vanderbilt"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
