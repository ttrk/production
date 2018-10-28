# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --mc --pileup_input dbs:/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS-100X_upgrade2018_realistic_v10-v1/GEN-SIM --eventcontent RAWSIM --pileup HiMix --pileup_dasoption=--limit=0 --datatier GEN-SIM-DIGI-RAW --conditions 103X_upgrade2018_realistic_HI_v4 --step DIGI:pdigi_hi_nogen,L1,DIGI2RAW,HLT:@fake2 --scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA --filein root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/GEN_SIM_20180629/180629_154627/0000/Pythia8_EmEnrichedDijet30_TuneCUETP8M1_5020GeV_SingleParticleFilter_cff_py_GEN_SIM_PU_100.root --fileout file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root -n 10 --no_exec --python_filename step2_DIGI_L1_DIGI2RAW_HLT_PU.py
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2018_pp_on_AA)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/GEN_SIM_20180629/180629_154627/0000/Pythia8_EmEnrichedDijet30_TuneCUETP8M1_5020GeV_SingleParticleFilter_cff_py_GEN_SIM_PU_100.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/6E79349E-BE29-E811-B541-0025901D40A6.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/F0B921C1-D724-E811-B201-002590E7DE20.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/A056FD9D-BE29-E811-8D00-0CC47A7EEDB0.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/26F5362B-3D29-E811-86A3-842B2B6F5ED7.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/30451174-4C29-E811-A7B3-90B11C418B00.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/14F3F2E0-6629-E811-91F9-1866DA7F9311.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/506A82CB-6B29-E811-AB0E-D4AE5290244F.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/18041658-7629-E811-AE12-F01FAFD8EAF2.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/C6E10C6C-7B29-E811-ADEC-842B2B6F6298.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/507470A0-B12A-E811-918C-F01FAFD1BA8A.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/D674EE67-0024-E811-AE49-D48564448738.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/2E3C1743-3229-E811-B447-001E67248732.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/4699A69E-BD29-E811-9D0E-0CC47A71F7B8.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/864F780B-1624-E811-B253-7845C4F8AF24.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/E89C3FB5-3E26-E811-BFEB-0025B3268672.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/54FB6EE6-EA26-E811-9EF3-002481CFE648.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/CC7054F5-2C26-E811-8227-FA163EE18696.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/2A1C5714-3926-E811-A1BD-FA163EDD0937.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/32292239-E326-E811-9A54-FA163EC2D429.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/AE514C19-3C29-E811-857C-0CC47A5FA3BD.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/38FE2640-E326-E811-AD57-AC162DACB208.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/2017F87F-D324-E811-92E2-44A842CFD5BE.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/14264634-FC23-E811-8A76-0CC47A5FC61D.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/C816B333-DB24-E811-91B8-0CC47A5FC495.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/F47FF735-E426-E811-A7EB-0242AC1C0501.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/E026F7FC-EB24-E811-9F08-B496910A9828.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/100000/32DE5F50-E326-E811-9362-A4BF01125868.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/EAA897B8-A424-E811-900F-1866DA85DDDC.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/C8CB594A-DD23-E811-A726-FA163E69C240.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/A06BAD95-F823-E811-A57B-FA163E3018B1.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/CC198004-C824-E811-AFAD-FA163E6861B6.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/88C298B2-4729-E811-BA81-FA163E217FB5.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/EED48503-BE29-E811-9F21-FA163EF5EC59.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/76A2E2FF-5529-E811-B057-90E2BACBAB00.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/221F1B9A-BE29-E811-BE8E-001E67504A65.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/DCBA0D87-DE29-E811-9A3E-B4E10FD21863.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/544CB209-E623-E811-A984-A4BF01158EC8.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/36BB9E6C-EB23-E811-B527-001E677928E2.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/4EDAFADC-EC23-E811-BD83-A4BF0112BE1E.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/EE85A391-F323-E811-96AA-A4BF01125BA0.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/B0BF499F-F823-E811-866A-A4BF0112E470.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/C8138528-C224-E811-9CFD-001E6779257C.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/90000/1A707040-AC24-E811-A3A3-001E6739A959.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/A25AB7CE-BE29-E811-89EC-D4856444779A.root', '/store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10-v1/30000/86223B19-7C29-E811-B3DD-000101000937.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2018_realistic_HI_v4', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_hi_nogen)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
import CalibTracker.Configuration.Common.PoolDBESSource_cfi
process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))
process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')
