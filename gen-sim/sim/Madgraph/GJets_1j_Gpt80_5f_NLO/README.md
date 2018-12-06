### Simulation

This directory contains files used for the event simulation. Config [step_GEN_SIM.py](step_GEN_SIM.py) takes the events defined in LHE file, hadronizes them using Pythia8 (via [this](Hadronizer_TuneCUETP8M1_5TeV_aMCatNLO_0p_LHE_pythia8_cff.py) fragment), and simulates them through the detector.

### Generation

See [this](../../../gen/Madgraph/cards/GJets_1j_Gpt80_5f_NLO/) folder for the event generation part.
