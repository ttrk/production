TTree* tree = (TTree*)gFile->Get("l1UpgradeEmuTree/L1UpgradeTree")
tree->GetEntries("egEt > 20 && abs(egEta) < 2.4")
tree->GetEntries("egEt > 15 && abs(egEta) < 2.4")
tree->GetEntries("egEt > 10 && abs(egEta) < 2.4")
tree->GetEntries("egEt > 5 && abs(egEta) < 2.4")
tree->GetEntries("egEt > 1 && abs(egEta) < 2.4")

