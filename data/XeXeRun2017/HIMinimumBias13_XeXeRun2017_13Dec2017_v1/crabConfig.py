from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'HIMinimumBias13_XeXeRun2017_13Dec2017_v1'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_XeXe_DATA_94X.py'
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2500    # request longer runtime.
# forest_CMSSW_9_4_1
# https://github.com/CmsHI/cmssw/commit/09a79bd943eda5136a9de73943553dd2bfd30f3e
# runForestAOD_XeXe_DATA_94X.py commit + turn off trees not related to photon production analysis + add tree for standard photons
# https://github.com/CmsHI/cmssw/commit/09a79bd943eda5136a9de73943553dd2bfd30f3e
# JSON file : /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/HI/Cert_304899-304907_5TeV_PromptReco_XeXe_Collisions17_JSON.txt
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/4437.html

config.section_('Data')
config.Data.inputDataset = '/HIMinimumBias13/XeXeRun2017-13Dec2017-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'Cert_304899-304907_5TeV_PromptReco_XeXe_Collisions17_JSON.txt'
#config.Data.runRange = '304899-304906'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'XeXeRun2017-13Dec2017-v1-photonFOREST'
config.Data.outLFNDirBase = '/store/user/katatar/HIRun2017XeXe/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
