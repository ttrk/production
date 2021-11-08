from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HIMinimumBias2_HIRun2018A_04Apr2019_v1_userInputFiles4ECAL_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_DATA_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_3_patch1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/fff9de2a54e62debab81057f8d6f8c82c2fd3dd6
# runForestAOD_pponAA_DATA_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doSuperClusters + activate l1object + add event plane info
# https://github.com/CmsHI/cmssw/commit/1f9264da586b55e0424c6a66b66d893af792e5f6
# relevant DAS query : summary dataset=/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD
#   output on 2019.08.07 : Number of blocks: 307 Number of events: 216552298 Number of files: 35084 Number of lumis: 41170 sum(file_size): 103439723002600 (103.4TB)
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
#config.Data.inputDataset = "/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD"
#config.Data.inputDBS = "global"
config.Data.userInputFiles = open('inputFiles.txt').readlines()
## AOD in the input list are the children of following RAW
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/326/384/00000/2B7DAAED-3B7B-394C-99C6-A37AB1FDC430.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/000C6F76-951B-AE46-AC00-7A4CCEB4EAAE.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/01B5D3C4-E02B-DB44-AAF4-0BEFD10FAAD6.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/BBAA6B6D-EDE6-0A49-A98F-C669D57DB544.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/BF49D3F3-CA0C-264E-8384-3D2BECD313EB.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/D280CF2C-2B7F-8845-8144-8660C980B089.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/D7B27BE2-6F2D-2540-A90B-3EF8E6370190.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/EF63C0AC-B746-2342-A63E-6556A99AB432.root
# /store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/F40D97D6-C4B6-1B41-97F8-97F33FDC8A4A.root
#config.Data.lumiMask = "Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = ""
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/HIMinimumBias2/HIRun2018A-04Apr2019-v1-userInputFiles4ECAL-FOREST/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_Vanderbilt"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
