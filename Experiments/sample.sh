dfg="dfg.py"
int_amd64_o1="../samples/intrinsics-amd64-windows-O1.c.bndb"
int_arm64_o1="../samples/intrinsics-arm64-windows-O1.c.bndb"
sum_amd64_o1="../samples/summation-amd64-macos-O1.bndb"
sum_arm64_o1="../samples/summation-arm64-macos-O1.bndb"

int_functions=("average_double" "average_float" "accumulation_double" "sum_array_float" "summation_double" "variance_float")
sum_functions=("sum_with_while" "get_product" "sum_of_selfprod")

for f in "${int_functions[@]}"
do
    echo "$int_amd64_o1 $f"
    python3 $dfg $int_amd64_o1 $f amd64 O1
    echo "$int_arm64_o1 $f"
    python3 $dfg $int_arm64_o1 $f arm64 O1
done

for f in "${sum_functions[@]}"
do
    echo "$sum_amd64_o1 $f"
    python3 $dfg $sum_amd64_o1 $f amd64 O1
    echo "$sum_arm64_o1 $f"
    python3 $dfg $sum_arm64_o1 $f arm64 O1
done