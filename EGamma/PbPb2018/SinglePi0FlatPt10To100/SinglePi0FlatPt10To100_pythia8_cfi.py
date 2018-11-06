## created by combining the following two fragments
# https://github.com/cms-sw/cmssw/blob/master/Configuration/Generator/python/SinglePi0E10_pythia8_cfi.py
# https://github.com/cms-sw/cmssw/blob/master/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py

import FWCore.ParameterSet.Config as cms
generator = cms.EDFilter("Pythia8PtGun",
                         PGunParameters = cms.PSet(
        MaxPt = cms.double(100.),
        MinPt = cms.double(10.),
        ParticleID = cms.vint32(111),
        AddAntiParticle = cms.bool(True), # false in pythia6 version but photons are their own anti-particle
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359) ## in radians
        ),
                         Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
                         psethack = cms.string('single pi0 pt 10 to 100'),
                         firstRun = cms.untracked.uint32(1),
                         PythiaParameters = cms.PSet(parameterSets = cms.vstring())
                         )
