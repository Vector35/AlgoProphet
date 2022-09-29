# AlgoProphet
Author: Rafael

The purpose of this project is to identify various, possibly unknown, implementations of known arithmetic algorithms within binaries.

## Description
AlgoProphet builds a model for a given algorithm by generating a high-level data-flow graph (DFG) from its binary code. It uses the DFG model as a pattern for matching against other binary code, in order to identify other, possibly distinct, implementations of the same algorithm. To generate DFGs efficiently, AlgoProphet makes use of the SSA form of Binary Ninja's Medium Level Intermediate Language (MLIL). AlgoProphet uses a number of techniques to improve matching against disparate code, including, among others:
* To make the matching algorithm order-independent, AlgoProphet normalizes the arithmetic operators, e.g., `a - b` (subtraction) is replaced with the semantically equivalent `a + (-1 * b)`.
* Different from the source code level, they are more implementations based on memory operations. To solve this challenge on binary, AlgoProphet extracts the semantic of memory operations and merges the information into `load` operation so that matching algorithm won't be affected.  
* etc.  


Currently AlgoProphet provides three functionalities through its Binary Ninja plugin:  
* Model Matching: Match functions in a binary with existing algorithm models
* Model Building: Build a model from instructions selected by the user
* Model Adjustment: Adjust a model by removing irrelevant nodes from the DFG based on MLIL instruction operands selected by the user

## Model Matching

The AlgoProphet plugin's 'models/' folder contains the existing models in [GML format](https://en.wikipedia.org/wiki/Graph_Modelling_Language): 

<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/existing-models.png" width=60% height=60%>

To match current function with existing models, you can right click anywhere in the function to open the plugin menu, then select `Plugins > AlgoProphet > Match Algos`.

<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/rk-match-models.png" width=60% height=60%>  

For each model that is matched, a tag will be created, indicating which model is likely to be found at the tagged address. In the screenshot, AlgoProphet finds a match for the "summation of array" model at the tagged MLIL instruction:

<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/match-model-result.png" width=60% height=60%>  

AlgoProphet will also attempt to assign meaningful names to variables, according to matched algorithm. For example, in the screenshot, the variable at line 14 has been changed to `arr_sum`. This helps the user to identify that this variable might be used for the sum of the array.

> **Note:** Functions whose names appear in `ignore.txt` will not be considered for matching.

## Model Building

To build a model (customize the algorithm you want to find from other binaries), you can highlight multiple instructions which you think are important features for the algorithm, and right click to get the plugin menu: `Plugins > AlgoProphet > Build a model`.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/highlight-build-model.png" width=60% height=60%>  
Next, you can find your generated model(`.gml` and visualized graph) in `test/` of plugin folder.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/generated-model.png" width=60% height=60%>  
In the screenshot, generated model is `sum_with_idx.gml` and `sum_with_idx.png` as the visualized result.  

After making sure that it is the model you want to use  
Two more steps:  
* Add formula of algorithm into `formula.json`.  
```json
{
    ...existing...,
    "[filename].gml": [
        "the rendered algorithm you want to show in tag",
        "the meaningful name to rename variable"
    ]
}
```
Take `summation of array` model for example, the first element would be `summation of array: += arr[index]` to be shown in tag content; the second element should be the `arr_sum` that would replace target variable with meaningful name.  
* move the `.gml` file(only gml file!!) from `test/` to `models/`
AlgoProphet will scan the existing models in `models/` to match algorithms.

## Model Adjustment

It is hard to build model perfectly at the first time, so we build up an interactive window for users to decide what nodes they want to remove from their models.
> here comes a hint for generating good model: keep it as simple as possible

First, before we adjust a model, make sure that you have existing model put in `test/`. You can also move the model back from `models/`.  
Back to the generated model in previous section, we think that the subgraph which includes `arr#0`, `4`, and `ADD#0` is not important for this algorithm(summation of array).  
To adjust our model, you can right click(at any places of the function) to get the plugin menu: `Plugins > AlgoProphet > Adjust a model`. We can choose to remove either `Operations` or `SSAVars or Constants`.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/adjust-constants.png" width=60% height=60%>  
In screenshot, we pick `SSAVars or Constants` in order to remove `4` from our model.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/adjusted-model.png" width=60% height=60%>  
From the screenshot, we can find that `4` is already removed from the graph model. You can also use the same way to remove other `SSAVars`.  
Of course, you can just re-create a new model by highlighting different instructions, but if you want to partial nodes from instructions (e.g., you might want to remove `0` from model, but keep `load#0`), then adjust model would be your best tool!  
Another option is to remove `Operations` such as `load#?` or `ADD#?` from the model. It is invisible to pick from binary view, so we provide an *indirect* way to do it. Assume we want to remove `ADD#0` from the model, and we also know that it is the operator of `arr#0`(from visualized result), we can right-click on `arr#0` and choose the option of `Operations`.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/adjusted-op-model.png" height=60% width=60%>  
From the screenshot, we can find that `ADD#0` has been removed from the model.  
After adjusting your model, remember to put it back to `models/` before `Match Algos`, also keep the information in `formula.json` and your model consistent.

> Suggest to keep test folder clean after you move your own model

## Limitations and Future work
AlgoProphet is the prototype of the concept: using data-flow graph to identify different implementation of arithmetic algorithm. Currently, AlgoProphet requires human's effort to generate models manually on Binary View. However, based on the matching results of AlgoProphet, we are convinced that AlgoProphet can help people to identify algorithms from the binaries. What's more, in addition to the known arithmetic algorithm, AlgoProphet also allows users to define models for their own implemented algorithms! In next step, we are exploring the way to help users generate models automatically or human-in-the-loop by machine learning work(e.g., GNN based on our generated graph models).  

In future work, AlgoProphet will not only focus on completeness of **intraprocedural** data flow analysis as near-term, but also extend the work to **interprocedural** data flow analysis as longer-term so that we can define the behaviors of callee(e.g., semantic summary extraction based on Infer).

## License
This plugin is released under an [MIT license](./license).
