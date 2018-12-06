## derived from https://github.com/cms-sw/genproductions/blob/master/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_aMCatNLO_0p_LHE_pythia8_cff.py
##              https://github.com/cms-sw/genproductions/blob/0a7e8c478fdc51377190a71cf9b01f43428cb79b/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_aMCatNLO_0p_LHE_pythia8_cff.py
## discussion on HN : https://hypernews.cern.ch/HyperNews/CMS/get/generators/3044/1.html
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5020.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
        processParameters = cms.vstring(
            'TimeShower:nPartonsInBorn = 1', #number of coloured particles (before resonance decays) in born matrix element
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    )
    )
)

