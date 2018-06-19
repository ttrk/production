### Creating the Config

Run the following to create the l1Ntuple config :

  ```bash
  ./createConfigs.sh
  ```

L1 EG capacity is to be changed for this production. 
1. Take the following file : https://github.com/ttrk/cmssw/blob/1497ff2a6e90d23c03c6a0b2b9627bdcd2bdd1b6/L1Trigger/L1TCalorimeter/src/firmware/Stage2Layer2EGammaAlgorithmFirmwareImp1.cc
     The original branch is CMSSW_9_4_0_pre3_egBypass_FGBit_ShapeBit
2. Move it to L1Trigger/L1TCalorimeter/src/firmware/Stage2Layer2EGammaAlgorithmFirmwareImp1.cc
3. Replace the lines 

  ```cpp
AccumulatingSort <l1t::EGamma> etaPosSorter(6);
AccumulatingSort <l1t::EGamma> etaNegSorter(6);
  ```
  with
  ```cpp
AccumulatingSort <l1t::EGamma> etaPosSorter(12);
AccumulatingSort <l1t::EGamma> etaNegSorter(12);
  ```
4. Compile : scram b -j4
