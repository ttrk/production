# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --era=Run2_2018 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 --conditions=103X_upgrade2018_realistic_HI_v7 -n 100 --mc --no_exec --no_output --filein=root://xrootd.cmsaf.mit.edu//store/user/katatar/HIRun2018PbPb/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU/181027_093754/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_574.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.cmsaf.mit.edu//store/user/katatar/HIRun2018PbPb/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU/181027_093754/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_574.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2018_realistic_HI_v7', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAWSimCalTP 

#call to customisation function L1TReEmulMCFromRAWSimCalTP imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulMCFromRAWSimCalTP(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleEMU,L1NtupleGEN 

#call to customisation function L1NtupleEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleEMU(process)

#call to customisation function L1NtupleGEN imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleGEN(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseUtils
from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 

#call to customisation function L1TTurnOffUnpackStage2GtGmtAndCalo imported from L1Trigger.Configuration.customiseUtils
process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_4 

#call to customisation function L1TSettingsToCaloParams_2018_v1_4 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_4(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

import CalibTracker.Configuration.Common.PoolDBESSource_cfi
process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))
process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')
process.simTwinMuxDigis.DTDigi_Source = cms.InputTag('bmtfDigis')
process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag('bmtfDigis')
process.simTwinMuxDigis.RPC_Source = cms.InputTag('muonRPCDigis')

process.caloStage2Params.hiMode = cms.uint32(1)
process.caloStage2Params.egEtaCut = cms.int32(24)
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
             tag = cms.string('EcalTPGFineGrainStrip_7'),                                                                                   
             connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')                                                                                                                                    ),                                                                          
    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),                                                                                         
             tag = cms.string('EcalTPGSpike_12'),                                                                                            
             connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')                                                                                                                                    )                                                                           
    )
