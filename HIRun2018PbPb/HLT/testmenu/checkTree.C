// code block to check the output of hltbitanalysis
TTree* tree = (TTree*)gFile->Get("hltbitanalysis/HltTree")
tree->GetEntries("HLT_GEDPhoton10 > 0")
tree->GetEntries("HLT_GEDPhoton15 > 0")
tree->GetEntries("HLT_GEDPhoton20 > 0")
tree->GetEntries("HLT_GEDPhoton30 > 0")
tree->GetEntries("HLT_GEDPhoton40 > 0")
tree->GetEntries("HLT_GEDPhoton50 > 0")
tree->GetEntries("HLT_GEDPhoton60 > 0")
