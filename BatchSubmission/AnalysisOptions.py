loadLibs=[
  #"libGenVector",
	"libNtupleVariables",
  "libGoodRunsLists",
	"libPileupReweightingTool",
  "libBTaggingTools",
  "libVHTausResonances",
        "libSVFit",
  ]


loadPacks=[
    "SFrameCore.par",
   	"NtupleVariables.par",
    "GoodRunsLists.par",
   	"PileupReweightingTool.par",
    "BTaggingTools.par",
    "VHTausResonances.par",
    "SVFit.par"
	   ]

compilePacks=[
  "../NtupleVariables",
  "../GoodRunsLists",
  "../PileupReweightingTool",
  "../BTaggingTools",
  "../SVFit",
  "../VHTausResonances"
  ]

AddUserItems = [
   #general settings
   ["RecoTreeName","tree"], 
   ["OutputTreeName_eletau", "tree_eletau"],
   ["OutputTreeName_mutau", "tree_mutau"],
   ["OutputTreeName_tautau", "tree_tautau"],
   ["JetPtCut", "120."]
   ]

#End
