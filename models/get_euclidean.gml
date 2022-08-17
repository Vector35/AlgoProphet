graph [
  directed 1
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 26
    base "arr1#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 9
    label "load#1"
    type "operation"
    value "load"
    idx 26
    base "arr2#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 10
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 26
  ]
  node [
    id 11
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 29
  ]
  node [
    id 12
    label "-1"
    type "constant"
    value "-1"
    idx 26
  ]
  node [
    id 13
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 30
  ]
  node [
    id 14
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 13
  ]
  node [
    id 18
    label "FSQRT#0"
    type "operation"
    value "FSQRT"
    idx 13
  ]
  edge [
    source 5
    target 11
    weight 1
    idx 26
    src_name "load#0"
    dst_name "ADD#2"
  ]
  edge [
    source 9
    target 10
    weight 1
    idx 26
    src_name "load#1"
    dst_name "MUL#0"
  ]
  edge [
    source 10
    target 11
    weight 1
    idx 26
    src_name "MUL#0"
    dst_name "ADD#2"
  ]
  edge [
    source 11
    target 13
    weight 2
    idx 29
    src_name "ADD#2"
    dst_name "FMUL#0"
  ]
  edge [
    source 12
    target 10
    weight 1
    idx 26
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 13
    target 14
    weight 1
    idx 30
    src_name "FMUL#0"
    dst_name "FADD#0"
  ]
  edge [
    source 14
    target 18
    weight 1
    idx 13
    src_name "FADD#0"
    dst_name "FSQRT#0"
  ]
]
