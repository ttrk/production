# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --era=Run2_2017 --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW2015 --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=FWCore/ParameterSet/MassReplace.massReplaceInputTag --conditions=auto:run1_data -n 100 --data --no_exec --no_output --filein=root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2015/HIMinimumBias2/RAW/v1/000/263/261/00000/0029C4B7-149B-E511-BEEE-02163E01431C.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2015/HIMinimumBias2/RAW/v1/000/263/261/00000/0029C4B7-149B-E511-BEEE-02163E01431C.root'),
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
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TEventSetupForHF1x1TPs,L1TReEmulFromRAW2015 

#call to customisation function L1TEventSetupForHF1x1TPs imported from L1Trigger.Configuration.customiseReEmul
process = L1TEventSetupForHF1x1TPs(process)

#call to customisation function L1TReEmulFromRAW2015 imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW2015(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleEMU 

#call to customisation function L1NtupleEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleEMU(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseUtils
from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 

#call to customisation function L1TTurnOffUnpackStage2GtGmtAndCalo imported from L1Trigger.Configuration.customiseUtils
process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)

# Automatic addition of the customisation function from FWCore.ParameterSet.MassReplace
from FWCore.ParameterSet.MassReplace import massReplaceInputTag 

#call to customisation function massReplaceInputTag imported from FWCore.ParameterSet.MassReplace
process = massReplaceInputTag(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag('hcalDigis')
process.caloStage2Params.egBypassShapeBit = cms.uint32(1)
