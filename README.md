# AlgoProphet
Author: Rafael

The purpose of this project is to identify various, possibly unknown, implementations of known arithmetic algorithms within binaries.

## Description
AlgoProphet builds a model for a given algorithm by generating a high-level data-flow graph (DFG) from its binary code. It uses the DFG model as a pattern for matching against other binary code, in order to identify other, possibly distinct, implementations of the same algorithm. To generate DFGs efficiently, AlgoProphet makes use of the SSA form of Binary Ninja's Medium Level Intermediate Language (MLIL). AlgoProphet uses a number of techniques to improve matching against disparate code, including, among others:

* Arithmetic Normalization: To make the matching algorithm order-independent, AlgoProphet normalizes arithmetic operations. For example, `a - b` (subtraction) is replaced with the semantically equivalent `a + (-1 * b)`.
* Memory Abstraction: Because the specifics of memory usage can vary widely across implementations of an algorithm and architectures, AlgoProphet abstracts the semantics of memory operations and merges them into a load operation to simplify algorithm matching.  


Currently AlgoProphet provides three functionalities through its Binary Ninja plugin:
* Model Matching: Match functions in a binary with existing algorithm models.
* Model Building: Build a model from instructions selected by the user.
* Model Adjustment: Adjust a model by removing irrelevant nodes from the DFG model based on MLIL instruction operands selected by the user.

## Model Matching

The AlgoProphet plugin's `models/` folder contains the existing models in [GML format](https://en.wikipedia.org/wiki/Graph_Modelling_Language): 

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/existing-models.png)
<br>The `models/` folder of the AlgoPropet's plugin folder</p>**

To match current function with existing models, you can right click anywhere in the function to open the plugin menu, then select `Plugins > AlgoProphet > Match Algos`.

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/rk-match-models.png)
<br>Use "Match Algos" in the AlgoProphet plugin menu to run matching</p>**  

For each model that is matched, a tag will be created, indicating which model is likely to be found at the tagged address. In the screenshot, AlgoProphet finds a match for the "summation of array" model at the tagged MLIL instruction:

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/match-model-result.png)
<br>Tagged match results can be found in the AlgoProphet section of the tags list</p>**  

AlgoProphet will also attempt to assign meaningful names to variables, according to matched algorithm. For example, in the screenshot, the variable at line 14 has been changed to `arr_sum`. This helps the user to identify that this variable might be used for the sum of the array.  

We also provide several binary samples of DFT (Discreate Fourier Transform) algorithm with different implementations on Github. Users can download the following samples to test how AlgoProphet identifies and locates DFT from the binaries.  
* [DFT samples on amd64](https://github.com/Vector35/AlgoProphet/blob/main/samples/dft-amd64-linux-O1-test2.bndb)
* [DFT samples on arm64](https://github.com/Vector35/AlgoProphet/blob/main/samples/dft-arm64-linux-O1-simple_names.bndb)

> **Note:** Functions whose names appear in `ignore.txt` will not be considered for matching.

## Model Building

It is possible to expand the algorithms that AlgoProphet can recognize by adding custom models. While it is possible to construct new model GML files by hand, the easiest way to add a model is with the plugin itself. Begin by selecting multiple instructions which you think are important features for the algorithm, and right click to get the plugin menu: `Plugins > AlgoProphet > Build a model`.  

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/highlight-build-model.png)
<br>Algebra Decompiler sidebar icon</p>**  

You can then find your generated model(`.gml` and visualized graph) in the `test/` subfolder of the plugin folder, named from the function containing the selected instructions:

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/generated-model.png)
<br>Algebra Decompiler sidebar icon</p>**  

In the screenshot, the newly generated model is `sum_with_idx.gml` and `sum_with_idx.png` is the visualized result.  

Once you have verified that the DFG corresponds to your desired model, you will need to take the following steps before AlgoProphet can use the new model:

* Add a formula entry for the  algorithm into `formula.json`:
```json
{
    ...existing...,
    "[filename].gml": [
        "the rendered algorithm you want to show in tag",
        "the meaningful name to rename variable"
    ]
}
```
Taking `summation of array` model for example, the first element would be `summation of array: += arr[index]` to be shown in tag content; the second element should be the `arr_sum` that would replace target variable with meaningful name:
```json
{
    ...existing...,
    "sum_with_idx.gml": [
        "summation of array: += arr[index]",
        "arr_sum"
    ]
}
```

* move only the `.gml` file (not the `.png` file) from `test/` to `models/`. AlgoProphet will scan any models found in `models/` to match algorithms.

## Model Adjustment

It is not always easy to build a model perfectly on the first attempt, so AlgoProphet provides an interactive window for users to decide what nodes they want to remove from their models. In order to build an effective and matchable model, it is important to keep it as simple as possible.

Before adjusting a model, ensure that the existing model’s `.gml` file is in `test/`, such as by moving the model file back from `models/`.

Looking at the generated model in previous section, it appears that the subgraph which includes `arr#0`, `4`, and `ADD#0` is not significant for this algorithm (summation of array).

To adjust the model, from the MLIL graph view of the function, right click anywhere in the function and select from the plugin menu: `Plugins > AlgoProphet > Adjust a model`. The menu includes actions  to remove either “`Operations`“ or “`SSAVars or Constants`”.

> **Note:** The “`Operations`“ action is only available in the MLIL graph view.

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/adjust-constants.png)
<br>Use the "Adjust a model" in the AlgoProphet plugin menu to fine-tune a model</p>**  

The screenshot below shows the result of selecting “`SSAVars or Constants`” with the constant `4` selected:

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/adjusted-model.png)
<br>The adjusted DFG model after removing the operand node for `4`</p>**  

In the screenshot, `4` has been removed from the graph model. The same technique can be used to remove other `SSAVars`.  

Another option is to remove Operations nodes such as `load#?` or `ADD#?` from the model. It is not visible to pick from the binary view, so AlgoProphet provides an indirect way to do it. In order to remove `ADD#0` from the model, since it is the operator of `arr#0` (from the visualized model DFG), right-click on `arr#0` and select `Plugins > AlgoProphet > Adjust a model > Operations`.

**<p align="center" style="text-align: center; width: 75%; margin-left: auto; margin-right: auto">
![Algebra Decompiler sidebar icon](screenshots/adjusted-op-model.png)
<br>The adjusted DFG model after removing the operator node for `ADD#0`</p>**

In the screenshot above, the node for `ADD#0` has been removed from the model.

After adjusting the model, it must be moved back to `models/` before using `Match Algos` again, and the information in `formula.json` and the `.gml` model file must be kept consistent.

## Limitations and Future work
AlgoProphet is a proof-of-concept prototype, using data-flow graph matching to identify different implementations of arithmetic algorithms. In its current form, it is most effective at recognizing smaller components of mathematical algorithms, such as expressions consisting of unary and binary arithmetic operations, as well as loops applying an operation over the elements of an array. Thus, it is currently best suited for locating smaller computations that can serve as distinguishing indicators of larger mathematical formulas, especially when found in close proximity to other computations that may also be components of the same larger formulas.

As part of future work, collections of such algorithmic components can be collected for a corpus of more complex known algorithms and used to automatically identify them based on occurrences of distinguishing indicators in close proximity with respect to the intra- and interprocedural control flow graphs. In general, future work for AlgoProphet will focus on completeness of intraprocedural data flow analysis in the near term, in order to extend coverage to model all of the pertinent computations within a function. In the longer term, extending model coverage to include interprocedural data flow analysis will incorporate the behavior of called functions.

Currently AlgoProphet relies on graph isomorphism for matching the DFG models for unknown binary code against known algorithms, thereby limiting the flexibility and robustness of matching in the presence of small changes due to compiler or architecture differences or variations in implementation techniques in the original source code. Future work will explore the use of machine learning both to generate models and to match decompiled code against them. This work would of course also explore enhancing or even replacing the current manual model creation process with automated model generation.

## License
This plugin is released under an [MIT license](./license).
