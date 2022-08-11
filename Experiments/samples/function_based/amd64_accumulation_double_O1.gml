graph [
  directed 1
  node [
    id 0
    label "1.0"
    type "constant"
    value "1.0"
    idx 14
  ]
  node [
    id 1
    label "FADD#1"
    type "operation"
    value "FADD"
    idx 14
  ]
  node [
    id 2
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 16
  ]
  node [
    id 3
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 16
  ]
  node [
    id 4
    label "-1"
    type "constant"
    value "-1"
    idx 16
  ]
  node [
    id 5
    label "1"
    type "constant"
    value "1"
    idx 16
  ]
  node [
    id 6
    label "n#0"
    type "ssavar"
    value "n#0"
    idx 16
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 14
    src_name "1.0"
    dst_name "FADD#1"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 16
    src_name "MUL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 2
    weight 1
    idx 16
    src_name "-1"
    dst_name "MUL#0"
  ]
  edge [
    source 5
    target 2
    weight 1
    idx 16
    src_name "1"
    dst_name "MUL#0"
  ]
  edge [
    source 6
    target 3
    weight 1
    idx 16
    src_name "n#0"
    dst_name "ADD#0"
  ]
]
