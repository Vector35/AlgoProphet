graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 18
  ]
  node [
    id 1
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 18
  ]
  node [
    id 2
    label "0"
    type "constant"
    value "0"
    idx 19
  ]
  node [
    id 3
    label "LSL#0"
    type "operation"
    value "LSL"
    idx 18
  ]
  node [
    id 4
    label "3"
    type "constant"
    value "3"
    idx 18
  ]
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 18
    base "array#0"
    base_width 8
    shift_width 8
  ]
  node [
    id 6
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 14
  ]
  node [
    id 7
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 19
  ]
  node [
    id 8
    label "1"
    type "constant"
    value "1"
    idx 19
  ]
  node [
    id 9
    label "pow#0"
    type "operation"
    value "pow"
    idx 14
  ]
  node [
    id 10
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 14
  ]
  node [
    id 11
    label "-1"
    type "constant"
    value "-1"
    idx 14
  ]
  node [
    id 12
    label "size#0"
    type "ssavar"
    value "size#0"
    idx 14
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 18
    src_name "array#0"
    dst_name "ADD#0"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 18
    src_name "0"
    dst_name "LSL#0"
  ]
  edge [
    source 2
    target 7
    weight 1
    idx 19
    src_name "0"
    dst_name "ADD#1"
  ]
  edge [
    source 3
    target 1
    weight 1
    idx 18
    src_name "LSL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 3
    weight 1
    idx 18
    src_name "3"
    dst_name "LSL#0"
  ]
  edge [
    source 5
    target 6
    weight 1
    idx 18
    src_name "load#0"
    dst_name "FADD#0"
  ]
  edge [
    source 6
    target 10
    weight 1
    idx 14
    src_name "FADD#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 8
    target 7
    weight 1
    idx 19
    src_name "1"
    dst_name "ADD#1"
  ]
  edge [
    source 9
    target 10
    weight 1
    idx 14
    src_name "pow#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 11
    target 9
    weight 1
    idx 14
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 12
    target 9
    weight 1
    idx 14
    src_name "size#0"
    dst_name "pow#0"
  ]
]
