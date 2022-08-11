graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 23
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 24
    base "array#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 2
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 35
  ]
  node [
    id 3
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 23
  ]
  node [
    id 4
    label "1"
    type "constant"
    value "1"
    idx 36
  ]
  node [
    id 5
    label "LSL#0"
    type "operation"
    value "LSL"
    idx 23
  ]
  node [
    id 6
    label "2"
    type "constant"
    value "2"
    idx 23
  ]
  node [
    id 7
    label "load#1"
    type "operation"
    value "load"
    idx 25
    base "array#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 8
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 34
  ]
  node [
    id 9
    label "FMUL#1"
    type "operation"
    value "FMUL"
    idx 35
  ]
  node [
    id 10
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 27
  ]
  node [
    id 11
    label "pow#0"
    type "operation"
    value "pow"
    idx 34
  ]
  node [
    id 12
    label "-1"
    type "constant"
    value "-1"
    idx 39
  ]
  node [
    id 13
    label "size#0"
    type "ssavar"
    value "size#0"
    idx 36
  ]
  node [
    id 14
    label "FMUL#3"
    type "operation"
    value "FMUL"
    idx 35
  ]
  node [
    id 15
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 35
  ]
  node [
    id 16
    label "FADD#2"
    type "operation"
    value "FADD"
    idx 39
  ]
  node [
    id 17
    label "MUL#1"
    type "operation"
    value "MUL"
    idx 36
  ]
  node [
    id 18
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 39
  ]
  node [
    id 19
    label "pow#1"
    type "operation"
    value "pow"
    idx 39
  ]
  node [
    id 20
    label "FMUL#4"
    type "operation"
    value "FMUL"
    idx 39
  ]
  edge [
    source 0
    target 3
    weight 1
    idx 23
    src_name "array#0"
    dst_name "ADD#0"
  ]
  edge [
    source 1
    target 2
    weight 2
    idx 15
    src_name "load#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 1
    target 8
    weight 1
    idx 24
    src_name "load#0"
    dst_name "FADD#0"
  ]
  edge [
    source 2
    target 16
    weight 1
    idx 35
    src_name "FMUL#0"
    dst_name "FADD#2"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 23
    src_name "1"
    dst_name "LSL#0"
  ]
  edge [
    source 4
    target 10
    weight 2
    idx 27
    src_name "1"
    dst_name "ADD#1"
  ]
  edge [
    source 4
    target 17
    weight 1
    idx 36
    src_name "1"
    dst_name "MUL#1"
  ]
  edge [
    source 5
    target 3
    weight 1
    idx 23
    src_name "LSL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 6
    target 5
    weight 1
    idx 23
    src_name "2"
    dst_name "LSL#0"
  ]
  edge [
    source 7
    target 8
    weight 1
    idx 24
    src_name "load#1"
    dst_name "FADD#0"
  ]
  edge [
    source 7
    target 9
    weight 2
    idx 25
    src_name "load#1"
    dst_name "FMUL#1"
  ]
  edge [
    source 8
    target 14
    weight 2
    idx 34
    src_name "FADD#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 9
    target 16
    weight 1
    idx 35
    src_name "FMUL#1"
    dst_name "FADD#2"
  ]
  edge [
    source 11
    target 14
    weight 1
    idx 34
    src_name "pow#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 12
    target 11
    weight 1
    idx 33
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 12
    target 15
    weight 1
    idx 35
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 12
    target 17
    weight 1
    idx 36
    src_name "-1"
    dst_name "MUL#1"
  ]
  edge [
    source 12
    target 19
    weight 1
    idx 39
    src_name "-1"
    dst_name "pow#1"
  ]
  edge [
    source 13
    target 11
    weight 1
    idx 33
    src_name "size#0"
    dst_name "pow#0"
  ]
  edge [
    source 13
    target 18
    weight 1
    idx 36
    src_name "size#0"
    dst_name "ADD#2"
  ]
  edge [
    source 14
    target 15
    weight 1
    idx 35
    src_name "FMUL#3"
    dst_name "MUL#0"
  ]
  edge [
    source 15
    target 16
    weight 1
    idx 35
    src_name "MUL#0"
    dst_name "FADD#2"
  ]
  edge [
    source 16
    target 20
    weight 1
    idx 39
    src_name "FADD#2"
    dst_name "FMUL#4"
  ]
  edge [
    source 17
    target 18
    weight 1
    idx 36
    src_name "MUL#1"
    dst_name "ADD#2"
  ]
  edge [
    source 18
    target 19
    weight 1
    idx 39
    src_name "ADD#2"
    dst_name "pow#1"
  ]
  edge [
    source 19
    target 20
    weight 1
    idx 39
    src_name "pow#1"
    dst_name "FMUL#4"
  ]
]
