graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 21
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 25
    base "array#1"
    base_width 8
    shift_width 8
  ]
  node [
    id 2
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 21
  ]
  node [
    id 3
    label "8"
    type "constant"
    value "8"
    idx 21
  ]
  node [
    id 4
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 23
  ]
  node [
    id 5
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 23
  ]
  node [
    id 6
    label "-1"
    type "constant"
    value "-1"
    idx 12
  ]
  node [
    id 7
    label "1"
    type "constant"
    value "1"
    idx 23
  ]
  node [
    id 8
    label "size#0"
    type "ssavar"
    value "size#0"
    idx 11
  ]
  node [
    id 9
    label "0.0"
    type "constant"
    value "0.0"
    idx 12
  ]
  node [
    id 10
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 12
  ]
  node [
    id 11
    label "SX#0"
    type "operation"
    value "SX"
    idx 12
  ]
  node [
    id 12
    label "pow#0"
    type "operation"
    value "pow"
    idx 12
  ]
  node [
    id 13
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 12
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 21
    src_name "array#0"
    dst_name "ADD#0"
  ]
  edge [
    source 1
    target 10
    weight 1
    idx 25
    src_name "load#0"
    dst_name "FADD#0"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 21
    src_name "8"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 23
    src_name "MUL#0"
    dst_name "ADD#1"
  ]
  edge [
    source 6
    target 4
    weight 1
    idx 23
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 6
    target 12
    weight 1
    idx 12
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 7
    target 4
    weight 1
    idx 23
    src_name "1"
    dst_name "MUL#0"
  ]
  edge [
    source 8
    target 5
    weight 1
    idx 23
    src_name "size#0"
    dst_name "ADD#1"
  ]
  edge [
    source 8
    target 11
    weight 1
    idx 11
    src_name "size#0"
    dst_name "SX#0"
  ]
  edge [
    source 9
    target 10
    weight 1
    idx 25
    src_name "0.0"
    dst_name "FADD#0"
  ]
  edge [
    source 9
    target 13
    weight 1
    idx 12
    src_name "0.0"
    dst_name "FMUL#0"
  ]
  edge [
    source 10
    target 13
    weight 1
    idx 12
    src_name "FADD#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 11
    target 12
    weight 1
    idx 12
    src_name "SX#0"
    dst_name "pow#0"
  ]
  edge [
    source 12
    target 13
    weight 1
    idx 12
    src_name "pow#0"
    dst_name "FMUL#0"
  ]
]
