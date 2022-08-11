graph [
  directed 1
  node [
    id 0
    label "array#0"
    type "ssavar"
    value "array#0"
    idx 19
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 23
    base "array#1"
    base_width 8
    shift_width 8
  ]
  node [
    id 2
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 19
  ]
  node [
    id 3
    label "8"
    type "constant"
    value "8"
    idx 19
  ]
  node [
    id 4
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 21
  ]
  node [
    id 5
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 21
  ]
  node [
    id 6
    label "-1"
    type "constant"
    value "-1"
    idx 21
  ]
  node [
    id 7
    label "1"
    type "constant"
    value "1"
    idx 21
  ]
  node [
    id 8
    label "n#0"
    type "ssavar"
    value "n#0"
    idx 21
  ]
  node [
    id 9
    label "0.0"
    type "constant"
    value "0.0"
    idx 23
  ]
  node [
    id 10
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 23
  ]
  node [
    id 11
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 23
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 19
    src_name "array#0"
    dst_name "ADD#0"
  ]
  edge [
    source 1
    target 11
    weight 2
    idx 23
    src_name "load#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 19
    src_name "8"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 21
    src_name "MUL#0"
    dst_name "ADD#1"
  ]
  edge [
    source 6
    target 4
    weight 1
    idx 21
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 7
    target 4
    weight 1
    idx 21
    src_name "1"
    dst_name "MUL#0"
  ]
  edge [
    source 8
    target 5
    weight 1
    idx 21
    src_name "n#0"
    dst_name "ADD#1"
  ]
  edge [
    source 9
    target 10
    weight 1
    idx 23
    src_name "0.0"
    dst_name "FADD#0"
  ]
  edge [
    source 11
    target 10
    weight 1
    idx 23
    src_name "FMUL#0"
    dst_name "FADD#0"
  ]
]
