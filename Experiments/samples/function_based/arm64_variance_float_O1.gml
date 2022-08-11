graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 27
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 31
    base "array#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 2
    label "4"
    type "constant"
    value "4"
    idx 27
  ]
  node [
    id 3
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 29
  ]
  node [
    id 4
    label "-1"
    type "constant"
    value "-1"
    idx 40
  ]
  node [
    id 5
    label "1"
    type "constant"
    value "1"
    idx 36
  ]
  node [
    id 6
    label "size#0"
    type "ssavar"
    value "size#0"
    idx 36
  ]
  node [
    id 7
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 38
  ]
  node [
    id 8
    label "load#1"
    type "operation"
    value "load"
    idx 32
    base "x0#2"
    base_width 4
  ]
  node [
    id 9
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 27
  ]
  node [
    id 10
    label "MUL#1"
    type "operation"
    value "MUL"
    idx 29
  ]
  node [
    id 11
    label "ADD#3"
    type "operation"
    value "ADD"
    idx 29
  ]
  node [
    id 12
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 38
  ]
  node [
    id 13
    label "FMUL#1"
    type "operation"
    value "FMUL"
    idx 38
  ]
  node [
    id 14
    label "SX#0"
    type "operation"
    value "SX"
    idx 37
  ]
  node [
    id 15
    label "MUL#2"
    type "operation"
    value "MUL"
    idx 36
  ]
  node [
    id 16
    label "ADD#4"
    type "operation"
    value "ADD"
    idx 39
  ]
  node [
    id 17
    label "pow#0"
    type "operation"
    value "pow"
    idx 38
  ]
  node [
    id 18
    label "FADD#2"
    type "operation"
    value "FADD"
    idx 40
  ]
  node [
    id 19
    label "FMUL#3"
    type "operation"
    value "FMUL"
    idx 38
  ]
  node [
    id 20
    label "FNEG#0"
    type "operation"
    value "FNEG"
    idx 38
  ]
  node [
    id 21
    label "SX#1"
    type "operation"
    value "SX"
    idx 40
  ]
  node [
    id 22
    label "pow#1"
    type "operation"
    value "pow"
    idx 40
  ]
  node [
    id 23
    label "FMUL#4"
    type "operation"
    value "FMUL"
    idx 40
  ]
  edge [
    source 0
    target 9
    weight 1
    idx 27
    src_name "array#0"
    dst_name "ADD#2"
  ]
  edge [
    source 1
    target 7
    weight 2
    idx 17
    src_name "load#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 1
    target 12
    weight 1
    idx 31
    src_name "load#0"
    dst_name "FADD#0"
  ]
  edge [
    source 2
    target 9
    weight 2
    idx 27
    src_name "4"
    dst_name "ADD#2"
  ]
  edge [
    source 3
    target 11
    weight 1
    idx 29
    src_name "MUL#0"
    dst_name "ADD#3"
  ]
  edge [
    source 4
    target 3
    weight 1
    idx 16
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 4
    target 10
    weight 1
    idx 29
    src_name "-1"
    dst_name "MUL#1"
  ]
  edge [
    source 4
    target 15
    weight 1
    idx 36
    src_name "-1"
    dst_name "MUL#2"
  ]
  edge [
    source 4
    target 17
    weight 1
    idx 37
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 4
    target 22
    weight 1
    idx 40
    src_name "-1"
    dst_name "pow#1"
  ]
  edge [
    source 5
    target 3
    weight 1
    idx 16
    src_name "1"
    dst_name "MUL#0"
  ]
  edge [
    source 5
    target 10
    weight 1
    idx 29
    src_name "1"
    dst_name "MUL#1"
  ]
  edge [
    source 5
    target 15
    weight 1
    idx 36
    src_name "1"
    dst_name "MUL#2"
  ]
  edge [
    source 6
    target 11
    weight 1
    idx 29
    src_name "size#0"
    dst_name "ADD#3"
  ]
  edge [
    source 6
    target 14
    weight 1
    idx 35
    src_name "size#0"
    dst_name "SX#0"
  ]
  edge [
    source 6
    target 16
    weight 1
    idx 36
    src_name "size#0"
    dst_name "ADD#4"
  ]
  edge [
    source 7
    target 18
    weight 1
    idx 38
    src_name "FMUL#0"
    dst_name "FADD#2"
  ]
  edge [
    source 8
    target 12
    weight 1
    idx 31
    src_name "load#1"
    dst_name "FADD#0"
  ]
  edge [
    source 8
    target 13
    weight 2
    idx 32
    src_name "load#1"
    dst_name "FMUL#1"
  ]
  edge [
    source 10
    target 11
    weight 1
    idx 29
    src_name "MUL#1"
    dst_name "ADD#3"
  ]
  edge [
    source 12
    target 19
    weight 2
    idx 38
    src_name "FADD#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 13
    target 18
    weight 1
    idx 38
    src_name "FMUL#1"
    dst_name "FADD#2"
  ]
  edge [
    source 14
    target 17
    weight 1
    idx 37
    src_name "SX#0"
    dst_name "pow#0"
  ]
  edge [
    source 15
    target 16
    weight 1
    idx 36
    src_name "MUL#2"
    dst_name "ADD#4"
  ]
  edge [
    source 16
    target 21
    weight 1
    idx 39
    src_name "ADD#4"
    dst_name "SX#1"
  ]
  edge [
    source 17
    target 19
    weight 1
    idx 38
    src_name "pow#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 18
    target 23
    weight 1
    idx 40
    src_name "FADD#2"
    dst_name "FMUL#4"
  ]
  edge [
    source 19
    target 20
    weight 1
    idx 38
    src_name "FMUL#3"
    dst_name "FNEG#0"
  ]
  edge [
    source 20
    target 18
    weight 1
    idx 38
    src_name "FNEG#0"
    dst_name "FADD#2"
  ]
  edge [
    source 21
    target 22
    weight 1
    idx 40
    src_name "SX#1"
    dst_name "pow#1"
  ]
  edge [
    source 22
    target 23
    weight 1
    idx 40
    src_name "pow#1"
    dst_name "FMUL#4"
  ]
]
