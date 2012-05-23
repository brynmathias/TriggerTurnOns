TriggerTurnOns
==============

Make turn on curves for the alphaT and HT triggers

To use:
First check out
git clone git@github.com:brynmathias/pyRootUtils.git or git://github.com/brynmathias/pyRootUtils.git (read only)
and run the setup script there, this just adds the directory to your python path.

then we input the histograms we want in to MakeTurnOns.py in the sums = {} dictionary
in the format:


"HT275AlphaT":([
  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v12",
  
],"./HT275.root"),

- Trigger name/HT bin name (if AlphaT is in the name it makes turn ons as a fn of alphaT otherwise it makes them in terms of HT)
- Triggers to test in list (these are summed at the end)
- Root file to read from.


To make the input files
=======================

checkout the ICF susy code:
- svn co svn+ssh://bm409@svn.cern.ch/reps/icfsusy/trunk/AnalysisV2
set up as per usual.
- Make trigger evolution plot
  - cd allhadronic/python
  
    
    Edit trigger_cfg.py to use the latest json file.
    
    Run trigger_cfg.py
    
  - cd ../scripts
    root -l
    .L trigger_hadd.C+
    trigger_hadd()
    
 


- cd bryn/python/

- Edit TriggerTurnOns.py, so that it contains your triggers. alphaT and or HT and the correct reference triggers, taken from the code above.

- Run TriggerTurnOns.py, hadd files and use as input to the MakeTurnOns.py script.

Bask in the knoledge that our triggers are efficient!