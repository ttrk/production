# Instructions
## 1. Generate database

  ```bash
  cmsRun srCondWrite_cfg.py
  ```

This creates the `EcalSRSettings_mod.db` file

## 2. Test the digitization

  ```bash
  voms-proxy-init --valid 168:00 --voms cms
  cmsRun step2_DIGI.py &> step2_DIGI.log
  ```

Run digitization for few events, e.g. 10 events as in the current code, to check it works correctly.

## 3. Submit jobs

  ```bash
  source /cvmfs/cms.cern.ch/crab3/crab.sh
  crab submit -c crabConfig_DIGI.py
  ```

# Notes
Configs in this directory are to be run on the full or a large portion of the sample. Therefore, if you want to generate the [digitization config](step2_DIGI.py) yourself, then 

1. Make sure to use `--limit=0` as `--pileup_dasoption` so that all the files from PU sample are included.
2. Insert the lines in [digiExtraLines.txt](digiExtraLines.txt) into the generated config so that ECAL settings are picked up.

# Resources

If you have questions/issue, the following can help

[Grid certificates](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid)

[CRAB guide](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab)

