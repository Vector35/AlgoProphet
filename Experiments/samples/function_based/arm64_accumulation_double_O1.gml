graph [
  directed 1
  node [
    id 0
    label "0.0"
    type "constant"
    value "0.0"
    idx 12
  ]
  node [
    id 1
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 11
  ]
  node [
    id 2
    label "FADD#1"
    type "operation"
    value "FADD"
    idx 12
  ]
  node [
    id 3
    label "1.0"
    type "constant"
    value "1.0"
    idx 12
  ]
  node [
    id 4
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 14
  ]
  node [
    id 5
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 14
  ]
  node [
    id 6
    label "-1"
    type "constant"
    value "-1"
    idx 14
  ]
  node [
    id 7
    label "1"
    type "constant"
    value "1"
    idx 14
  ]
  node [
    id 8
    label "n#0"
    type "ssavar"
    value "n#0"
    idx 14
  ]
  edge [
    source 0
    target 1
    weight 2
    idx 11
    src_name "0.0"
    dst_name "FADD#0"
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 12
    src_name "0.0"
    dst_name "FADD#1"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 12
    src_name "1.0"
    dst_name "FADD#1"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 14
    src_name "MUL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 6
    target 4
    weight 1
    idx 14
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 7
    target 4
    weight 1
    idx 14
    src_name "1"
    dst_name "MUL#0"
  ]
  edge [
    source 8
    target 5
    weight 1
    idx 14
    src_name "n#0"
    dst_name "ADD#0"
  ]
]
