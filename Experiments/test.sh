# echo "degrees_to_radians_double vs. degrees_to_radians_explicit_double"
# python3 graph_match.py ./model/amd64_degrees_to_radians_double0.gml ./model/amd64_degrees_to_radians_explicit_double0.gml
# echo "degrees_to_radians_float vs. degrees_to_radians_explicit_float"
# python3 graph_match.py ./model/amd64_degrees_to_radians_float0.gml ./model/amd64_degrees_to_radians_explicit_float0.gml
# echo "radians_to_degrees_double vs. radians_to_degrees_explicit_double"
# python3 graph_match.py ./model/amd64_radians_to_degrees_double0.gml ./model/amd64_radians_to_degrees_explicit_double0.gml
# echo "radians_to_degrees_float vs. radians_to_degrees_explicit_float"
# python3 graph_match.py ./model/amd64_radians_to_degrees_float0.gml ./model/amd64_radians_to_degrees_explicit_float0.gml
# echo "diff type: radians_to_degrees_float vs. radians_to_degrees_double"
# python3 graph_match.py ./model/amd64_radians_to_degrees_float0.gml ./model/amd64_radians_to_degrees_double0.gml
# echo "diff type(explicit): radians_to_degrees_explicit_float vs. radians_to_degrees_explicit_double"
# python3 graph_match.py ./model/amd64_radians_to_degrees_explicit_float0.gml ./model/amd64_radians_to_degrees_explicit_double0.gml

model0="./sepmodel/function-based/arr_sum.gml"
model1="./sepmodel/function-based/sum_of_selfprod.gml"

echo "======== amd64 ========"
echo "average_float"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_average_float_O1.gml
echo "\naverage_double"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_average_double_O1.gml
echo "\naccumulation_double"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_accumulation_double_O1.gml
echo "\nsum_with_while"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_sum_with_while_O1.gml
echo "\nget_product"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_get_product_O1.gml
echo "\nsum_of_products"
python3 graph_match.py $model0 $model1 ./samples/function_based/amd64_sum_of_selfprod_O1.gml

echo "\n======== arm64 ========"
echo "average_float"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_average_float_O1.gml
echo "\naverage_double"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_average_double_O1.gml
echo "\nsum_with_while"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_sum_with_while_O1.gml
echo "\nsum_array_float"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_sum_array_float_O1.gml
echo "\nsummation_double"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_summation_double_O1.gml
echo "\nvariance_float"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_variance_float_O1.gml
echo "\nsum_of_selfprod"
python3 graph_match.py $model0 $model1 ./samples/function_based/arm64_sum_of_selfprod_O1.gml