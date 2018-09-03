# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --era=Run2_2018 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_2 --customise_commands=process.simTwinMuxDigis.DTDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.RPC_Source = cms.InputTag('muonRPCDigis')\n --conditions=101X_upgrade2018_realistic_v7 -n 500 --mc --no_exec --no_output --filein=/store/himc/HINPbPbSpring18DR/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM-RAW/NoPU_100X_upgrade2018_realistic_v10_ext1-v1/00001/FE243EFA-6DAB-E811-BFDE-9CB654AD72EC.root
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
    input = cms.untracked.int32(500)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/himc/HINPbPbSpring18DR/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM-RAW/NoPU_100X_upgrade2018_realistic_v10_ext1-v1/00001/FE243EFA-6DAB-E811-BFDE-9CB654AD72EC.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:500'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '101X_upgrade2018_realistic_v7', '')

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
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_2 

#call to customisation function L1TSettingsToCaloParams_2018_v1_2 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_2(process)

# End of customisation functions

# Customisation from command line

process.simTwinMuxDigis.DTDigi_Source
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)
process.caloStage2Params.egBypassShape = cms.uint32(1)
process.caloStage2Params.egBypassECALFG = cms.uint32(1)
process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)
process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)
process.caloStage2Params.egEtaCut = cms.int32(24)
process.GlobalTag.toGet = cms.VPSet(                                                                            
    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
             tag = cms.string('EcalTPGFineGrainStrip_12'),                                                                                   
             connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')                                                                                                                                    ),                                                                          
    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),                                                                                         
             tag = cms.string('EcalTPGSpike_12'),                                                                                            
             connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')                                                                                                                                    )                                                                           
    )
