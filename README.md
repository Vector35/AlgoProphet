# AlgoProphet
Author: Rafael

The purpose of this project is to identify various, unknown implementations of arithmetic algorithm from given binaries.

## Description
To identify the different implementation of algorithm, AlgoProphet generates a High-level Data-flow graph as the model for the algorithm and uses it as the pattern to match the given target. To generate data-flow graph efficiently, AlgoProphet takes use of the MLIL SSA from on Binary Ninja. Following are some more efforts AlgoProphet contributes to work on different implementations:  
* To make the matching algorithm order-independent, AlgoProphet normalizes the arithmetic operators e.g., `a - b`(subtraction) should be same as `a + (-1)*b`
* Different from the source code level, they are more implementations based on memory operations. To solve this challenge on binary, AlgoProphet extracts the semantic of memory operations and merges the information into `load` operation so that matching algorithm won't be affected.  
* etc.  


Currently AlgoProphet provides three functionalities:  
* Match functions with existing models  
* Build a model based on highlighted instructions
* Adjust a model

## Match functions with existing models
In the `models/` of your plugin folder, you can find our existing models in gml format.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/existing-models.png" width=60% height=60%>

To match current function with existing models, you can right click(at any places of the function) to get the plugin menu: `Plugins > AlgoProphet > Match Algos`.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/rk-match-models.png" width=60% height=60%>  
What will happen next is that `tags` would be created. The content of tag would describe which model is likely to be found at the address. In the screenshot, AlgoProphet finds the summation of the array elements at the statement.  
<img src="https://github.com/Vector35/AlgoProphet/blob/main/screenshots/match-model-result.png" width=60% height=60%>  
You can also find that the some variable name would be **renamed** to a *meaningful* one. For example, in the screenshot, the variable at line 14 has been changed to `arr_sum`. With this work, user can identify that this variable might be used for the sum of the array.

> If you want to ignore matched instructions in some functions, just add them to `ignore.txt`.

## Build a model based on highlighted instructions
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

## Adjust a model
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
