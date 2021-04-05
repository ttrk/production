# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py --mc --pileup HiMixGEN --pileup_input dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM --pileup_dasoption=--limit=200 --eventcontent RAWSIM --datatier GEN-SIM --conditions 103X_upgrade2018_realistic_HI_v11 --beamspot RealisticPbPbCollision2018 --step GEN,SIM --scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA --fileout file:step1_GEN_SIM.root -n 150000 --no_exec --python_filename step1_GEN_SIM.py
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2018_pp_on_AA)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMixGEN_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealisticPbPbCollision2018_cfi')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(150000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PYTHIA 8, Tune CP5, (unquenched) photons in NN (pt-hat > 15 GeV) at sqrt(s) = 5.02 TeV')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step1_GEN_SIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/CE7BFE52-90D6-544B-AD3E-2E4B85EBDD90.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/AFE78A9A-A00D-754E-8F99-23C7C5CB4303.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/F9E7DB6C-14B9-6246-8938-52924248EC77.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/91F3FC4F-1EE8-974D-96FA-EBB4F3993C64.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/B0AC6B93-5CCE-5344-8DE2-902A2A28E3A2.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/040E8E2D-65FD-1B4D-8059-D6CF07EE910A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/E3CD2F69-3DA2-2847-B890-12660551FE50.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/AE473330-8740-D446-B66E-E2CAF806B5DA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/7BB97AC8-C896-484C-ACB9-49437746009F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/33ACD025-2567-4A44-A7B6-44D16F7CE648.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280004/047EA5F7-8639-6E49-9459-C94D8B891234.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/6A407BBA-2A1D-E34A-AACB-C0E2A3AF3F41.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/562600E6-F65C-5E42-A6B6-D6C6674DE4A1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/0AD1FD3C-01BD-4E48-BF6D-38FA6F7F251F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/F82AFBA8-4C35-5441-A62B-EF6010E37B33.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/96CD0FFF-4BB1-0B4D-92CE-8A9436A5A3A1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/A50B46FE-7356-664E-AFA8-E0208626E117.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/4B600E95-F39E-234F-9B42-40B8018C8815.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/31422315-EC97-DA47-A3DA-7856FE43BB60.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/FCE3859F-177F-CB4C-95BB-5499AE387B18.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/6F9585E9-BA9F-4C43-B02F-2A283CD856BB.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/7A89C2AD-49FC-8948-8BBF-6C903E3CE4DA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/CC012761-6E32-7147-BA64-B8495CE28FCA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/B0398749-A51C-7E4C-A562-3E50EE800D8B.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/3A5F37C7-2B07-EC4B-96DE-C04C7F64E8A6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/6C5E9338-71A7-7B44-AAA5-3F84D0FE0F77.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/F6954DEE-3952-D841-922C-D8F241090213.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/34D52395-21A3-5642-AF78-87A408EF3FC0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/577BC79A-6E2A-6F4C-8826-69B4D409A736.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/03A39B47-16DA-6041-A5A4-C1986F555C2C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/E2E294F3-4430-6740-8304-8F61923C91A3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/A637E3A6-91D7-A740-B6CB-D7FB79B05CB4.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/CA90C44C-7B11-3A44-9D9B-6577DAACD0D3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/EF20C2AC-D3B4-F040-A25F-1FE4D4F82223.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/C2E80D44-3611-FD45-A92B-920DA34111E2.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/C2EEDB3E-1BF7-2B4B-81DA-D19B5361405E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/1C46A6D6-8912-7044-BFF0-585B0E5B06A9.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/D320B58E-A42E-D44E-8849-DD40580D19A0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/E7AAAF73-8C47-C44F-8930-496385FF904D.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/623D3533-5289-A249-8657-8AB95B3EC7C8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/F22FADF0-EC62-3E4B-ACF4-7CF40A52FBA0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/EFD09F6B-8B8B-C848-8CBA-BECE4BA00E70.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/31DCF65B-F122-EA44-8012-699B693D1BA8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/88FD9885-E383-EA49-9CEC-E5F06AC26A4E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/8B9E1FF8-51B4-7C43-8ABD-275250DA30EA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/9E4FE5D7-8241-AA44-993A-DD1B297D31D1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/5EDC4163-8A8A-F64E-A809-3ADC6B7D45D1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/C5E3BBEE-C18B-F948-99B6-1D4C6E8F8CF6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/4386523E-1D55-AA41-A26F-5C96CD1CE72E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/F1637C5A-A887-334F-8560-6D0EF6E56E1F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/3E1124A2-0767-2243-8163-E70918A4BE01.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280007/68E7E69F-BADA-BA44-AE8E-9093EB1142C6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/2F5B96E5-2635-1C4C-825F-F6AE07C45B56.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280005/7AA0005A-B298-6243-8B5A-5ED1D1D2DD58.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/1815C9CB-923C-164B-A02F-C37598F42F81.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/F5506F97-6227-8543-83A7-9145452234BC.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/2A7E9021-539D-614E-9C00-640029CCE030.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/E467DB5B-E98A-D04E-9830-821680F8A8D5.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/61F04F40-6C9B-9644-93C0-8F1B21235C6E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/6807450D-598D-6D4D-A5AD-26AFE626657D.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/95F4EADB-AD7A-CC43-95E0-362A57190564.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/6C812BDE-D211-8E4F-8360-AB52DC37C669.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/E224EF7F-CF27-DA4D-9A4D-2F7B3F225FB0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/67AE1D7E-34D0-6C48-B6C3-66D1C2CBC8F8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/59591280-A897-FB47-8381-60ECE1F01E2B.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/365208D5-FB5F-B74A-A1C1-67E4434C4993.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/630C6073-E249-3B4B-9F74-E70EE863669A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/FB6BAED7-DE22-0F41-B9CA-08A6108E51A6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/53016009-B146-A24D-A788-727A3CFF0FA8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D63B9909-FCF1-DF4F-A43D-CF18FD34B533.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/DB1B5B3A-4F65-4144-BB4A-91329E756D9E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D3EBD449-CF23-614E-88C3-598660BD7998.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/913E2C81-8475-0D48-B330-B35EEED25CF7.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/BE7E2201-5909-0940-ABB0-BABE31AAD335.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/335C32F5-12D4-8449-B483-7123E3D351E7.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/75D9AA37-1B08-D64E-9F75-EC1D762A1F65.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/0B71A83D-9081-0540-80C1-C75330F30776.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/4F03C03A-CDF5-C942-9E76-33480A25756F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/6E7D523F-B45C-2144-8E72-34ED10843AB3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/2D3D800D-2645-C643-9E58-CB4851684270.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/66727E4E-346F-B049-9B3B-8F2707EE2AA0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/6F7EE61D-BD83-DD44-A071-8EAFDB8CEEAB.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/AC5B4C3A-4131-E444-9150-F651EBFB6FF9.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/0D2C5587-AC78-FF4F-A108-920D60E6FB92.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/F3C3FEBE-B433-AE4F-9E76-3B92BC7F2C28.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D68DD195-F41B-EF48-963B-B583507AB77C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/AFD28876-19F9-9E4A-B3F8-5D02EC8FB9BD.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/C32579D2-5734-E143-A4F9-750197BF0BC0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/6761B357-6297-2942-848D-0CDD3F0A65FF.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/72874EE3-A873-E240-AD22-760640EE2380.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/5AECD8E8-191D-D24D-9364-1BF04D19B844.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/36326439-A0C9-E940-91F4-333F4B3C72BD.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/E4AD2C26-A38D-254A-BDCA-6A7D801AF342.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/F4C8AEE6-7EE8-E740-BF8B-3EC19DD79C94.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/A1EF9DE2-B94B-234E-A731-D2C1A699B1C8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/0F6AA0E4-5FC2-E344-A71C-01409D119BDA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/0263E174-0912-3A43-916B-C1E57D57427B.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/5E1DE7C2-1E0B-D54C-B974-7E9D0C4468DD.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/81712A2A-9EDD-7146-B9F7-920F0D8F411F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/E802987F-2F0F-8644-8411-11239AB3B7FD.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/D40AF727-2CC0-E74A-B602-FC06D66E2491.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/5FB752A9-67F3-D542-B292-DE9F7CAE570E.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/34433245-7125-EA46-A928-0198A7A555E6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/2E0C5ADF-579C-684D-B009-20C94F966039.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/8ECB8ED5-9E1E-924C-ADCD-08DC8A322D83.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/089F1182-03B0-B349-91BE-27A502F51DFF.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/12196F4F-D769-7D48-83FF-A4F8360EF014.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/954E6B4F-6795-E747-8635-9EAB5BBE8566.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/E3976863-6806-F040-AA31-14A7133CA3D8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/663B5C18-E902-CE48-8237-E2FB23AB330F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/EE4BC78E-40DD-F145-BCB0-045698A5B0B6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/17BE0918-2745-8641-B424-72A6FD7AFADC.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/C1B83769-570F-0C42-842E-C786B9960585.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/0F74475B-9C2E-B54F-AB87-7FE9032703F4.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/20B23062-C8A1-324F-951C-EF64C0165948.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/5DAEE75B-4EDE-0342-BCBF-8DC7038CA6A6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/9C642F49-5B9D-B347-8590-C47AEEECECCF.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/2DBD2D70-1568-4841-AAC3-05CF13D741A6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/CD91927A-EDE0-4C4F-8B6D-4098D915E1D8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/2D3D5A70-DDE3-F646-B5D8-31FB666652C6.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/8A066670-0B7A-E340-AE9A-9BCC38ABB5D1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/802E469B-8C5B-9A48-AF2E-1FFFB48E13CB.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/0C692B25-B1D1-AA4E-BF98-9B0988965743.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/14F1BB8C-5B49-8D46-885B-EB8E547F0288.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280005/87F3DFCB-EE86-B345-8800-C7C563BE537F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/1C06BB9E-55F2-884D-BCA4-6520048A6433.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/E14D6E01-7006-8046-963F-F125BC2BEBC2.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/0B38D429-99E1-C941-B88A-96464347E17C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/F81F45B1-43C7-B24F-988C-1E9C5A83CA5D.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/D835600F-DCEA-5543-979A-A3444092D901.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/523FBABE-F353-7441-B1F4-410CD96A26AE.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/038CAE81-76FE-8344-99BC-7CB4AA8F15D3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/15A484A4-D182-5F4E-AE82-CB6E7F417CAB.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/587AA120-9381-744E-B38C-A320EDDD7C5C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/1009A6A0-63DD-1740-99B7-C806837DD751.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/67A4E438-DE13-A741-9599-F0F74414D549.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/239AFA9D-676D-B048-BBAA-5CFF96BA68C0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/A5C978DE-F395-2345-A03A-133223E08245.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/9A8A3E6C-D1D3-E44C-873B-F617FAB66B8A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/8C4E7998-4F3D-3D40-A268-74355F34E3E0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/45632F6A-6B6E-5441-BA18-D4456DD8093D.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/F2067D1E-1348-1C44-92F9-A4E6093F5BCA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/E80B2767-D005-B84B-B815-8146E275D676.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/E576C786-A745-344B-B078-659AD1138BA1.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/057B80D5-5E8F-DA46-8037-711177721F99.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/63096570-C744-B348-B0DC-B310286FD38C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/7E22BC2D-367E-D540-B4FE-EF09EA787A19.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/47901FBA-C77F-7743-A9E9-BF86A437ED9A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/D6F6FE0E-726C-A54C-BA37-AC080E8CDAF8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/058ABB10-624D-F949-BC08-53C560136BE3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280001/FCE7A34E-B972-9A40-91EB-18FB153EBA62.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/DF6F23BE-F80A-1844-9E6C-0541AC56F526.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/AB2C5AC0-1A73-C442-A467-79D19A01DF36.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/EC88CB94-120A-9848-8D25-29301B7380E7.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/668611B4-9C45-8C4B-BD6D-F05FF18E1478.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/05157B8F-3ADF-234F-89A0-3BD2F8B2F523.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/90A2A95E-3BED-5941-BD1D-D12912B07D39.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/C359C407-96F6-5F46-8ED5-09BE9C2094A9.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/231BA451-96B9-9E49-91F9-F02E7CF54285.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/465B5BB9-E940-4744-834D-6B961B13C790.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/AE5EB487-401B-324D-9563-2F0F026AA3C0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/1A5CC51A-CB56-3A47-822F-BBB3FE1C1E92.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/7F9F8F3C-6C22-184C-8FFD-6FA5F91A316B.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280006/9BF627D3-D69B-0349-AAE2-661675578127.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D20096BE-FFD2-D845-B60B-92C3C3F4F803.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280007/0849DA19-0496-2848-8CF3-DA52BA5C5A7A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/A97C4479-BFDE-6549-8A2E-7C7CF78C2221.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D490A698-32CE-F247-BEEB-78CF62FB51C9.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/32BC5E18-13CA-0A4E-B175-559F8D5051DB.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280007/9B3F0BBA-59F6-8247-9033-57247DE1BC46.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/C2DC4037-188B-DB4A-AAF0-BFDD93258119.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/75BDDA95-FB58-474B-969A-8AA02F52ADDA.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/DAECEE1D-BA7B-4941-86F2-48DD3640EAC3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/428D663B-9922-DA4E-9AB6-377E2A7D8E1A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/92FA264C-4A3C-8C4D-9C04-1BAF59F47C41.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/D385A368-C7D1-CB4A-AFEF-21D1A8E7939A.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/33F99196-1F9B-F34D-9F48-F2E92FCDDB77.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/1B2CD201-B904-2F43-A392-0EFA5BFC9B7D.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280002/B2DF72D3-0580-7546-ADC9-2ECCB285C7ED.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/BDF6C25C-C35A-C74E-8549-06640A3FB187.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/5514E890-C165-1F41-9F55-B9EEAE90BDD0.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280000/22F9DB5E-3D7F-6F4D-A76F-1C925B31F6C3.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/A93894A8-4C5A-5447-A57B-5BF2CD4251D7.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/777AA350-E611-2943-90C2-213987415168.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/295210D1-2B8F-3F4E-8941-F87085E8DFFF.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/28AA2993-0EAD-FA42-8AFF-35044E370F5C.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/2F30EF36-A684-8B4E-B269-8592CA25C520.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/F074AF9E-0A66-8548-8694-91C07758CC39.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/9AA2BBC3-5994-A64D-ACE7-94DEC78EAA48.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/821BF288-381A-9242-A728-DE951AAACDB8.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/5D34F4A0-133D-EC44-B28C-3C5F47BC4C50.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/3594BA15-287B-3845-ABB7-E5DAA687D843.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/4DE22136-B3B7-B64F-B04D-A76900682B43.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/2BB9BF24-12A8-B945-B4E8-7AE639679B89.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/6152F627-1C78-4A4A-8C77-F5F11D4AE039.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/F82DA98B-883A-FC4D-8CEF-15EF12020A23.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/1CD8FCA1-272D-9E41-B47E-F82E69E01501.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/B74B67FA-E644-9E41-A11C-C9D85C68516F.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/386F8096-D432-BE45-8E40-C3096F0B6A42.root', '/store/himc/HINPbPbAutumn18GS/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM/103X_upgrade2018_realistic_HI_v11-v1/280003/415EFA3E-5D58-BF4A-BC13-516924031B1D.root'])
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2018_realistic_HI_v11', '')

process.photonFilter = cms.EDFilter("PythiaFilterMultiMother",
    MinPt = cms.untracked.double(15.0),
    MotherIDs = cms.untracked.vint32(
        1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, -22, -21, -20, 
        -19, -18, -17, -16, -15, 
        -14, -13, -12, -11, -10, 
        -9, -8, -7, -6, -5, 
        -4, -3, -2, -1
    ),
    ParticleID = cms.untracked.int32(22),
    Status = cms.untracked.int32(1)
)


process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'HardQCD:all = on', 
            'PromptPhoton:all = on', 
            'PhaseSpace:pTHatMin = 15.', 
            'PhaseSpace:pTHatMax = 9999.', 
            'PhaseSpace:bias2Selection = on', 
            'PhaseSpace:bias2SelectionPow = 2.0', 
            'PhaseSpace:bias2SelectionRef = 30'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(5020.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.photonFilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
process.Timing=cms.Service("Timing", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))
