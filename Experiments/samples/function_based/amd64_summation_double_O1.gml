graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 11
  ]
  node [
    id 1
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 11
  ]
  node [
    id 2
    label "0"
    type "constant"
    value "0"
    idx 14
  ]
  node [
    id 3
    label "LSL#0"
    type "operation"
    value "LSL"
    idx 11
  ]
  node [
    id 4
    label "3"
    type "constant"
    value "3"
    idx 11
  ]
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 12
    base "array#0"
    base_width 8
    shift_width 8
  ]
  node [
    id 6
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 13
  ]
  node [
    id 7
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 13
  ]
  node [
    id 8
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 14
  ]
  node [
    id 9
    label "1"
    type "constant"
    value "1"
    idx 14
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 11
    src_name "array#0"
    dst_name "ADD#0"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 11
    src_name "0"
    dst_name "LSL#0"
  ]
  edge [
    source 2
    target 8
    weight 1
    idx 14
    src_name "0"
    dst_name "ADD#1"
  ]
  edge [
    source 3
    target 1
    weight 1
    idx 11
    src_name "LSL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 3
    weight 1
    idx 11
    src_name "3"
    dst_name "LSL#0"
  ]
  edge [
    source 5
    target 6
    weight 2
    idx 12
    src_name "load#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 6
    target 7
    weight 1
    idx 13
    src_name "FMUL#0"
    dst_name "FADD#0"
  ]
  edge [
    source 9
    target 8
    weight 1
    idx 14
    src_name "1"
    dst_name "ADD#1"
  ]
]
