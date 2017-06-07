# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SingleGammaFlatPt10To200_pythia8_cfi.py --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM --mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 75X_mcRun2_HeavyIon_v1 --beamspot MatchHI --step GEN,SIM --scenario HeavyIons --era Run2_HI -n 50 --no_exec --python_filename SingleGammaFlatPt10To200_pythia8_Hydjet_GEN_SIM_PU.py --fileout SingleGammaFlatPt10To200_pythia8_Hydjet_GEN_SIM_PU.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_HI)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMixGEN_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedMatchHI_cff')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SingleGammaFlatPt10To200_pythia8_cfi.py nevts:50'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SingleGammaFlatPt10To200_pythia8_Hydjet_GEN_SIM_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/0041B26A-EB74-E511-BA4B-0025905C4264.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/004752C7-AD73-E511-9761-003048F2E63A.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/0049E97E-3672-E511-8316-0025904C51DA.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/00BDE5ED-5A73-E511-8389-002590AC5062.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/00CA13C1-2E73-E511-BA95-00259073E3B2.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/00F86C8B-C873-E511-BFED-549F35AD8BE3.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/00FDAD95-F073-E511-85CD-00266CF9B9F0.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/022159CB-8172-E511-9923-0025905C431A.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/0230036F-3D73-E511-9278-002590DB9232.root', '/store/himc/HiFall15/Hydjet_Quenched_MinBias_5020GeV_750/GEN-SIM/75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/10000/02BB0106-A973-E511-96C1-00266CF250C0.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v1', '')

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(200.0),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(10.0),
        ParticleID = cms.vint32(22)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single gamma pt 10 to 200')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


