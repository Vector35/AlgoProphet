graph [
  directed 1
  node [
    id 0
    label "0"
    type "constant"
    value "0"
    idx 64
    output 0
  ]
  node [
    id 1
    label "6.283184"
    type "constant"
    value "6.283184"
    idx 82
    output 0
  ]
  node [
    id 2
    label "-1"
    type "constant"
    value "-1"
    idx 94
    output 0
  ]
  node [
    id 3
    label "pow#0"
    type "operation"
    value "pow"
    idx 82
    output 0
  ]
  node [
    id 4
    label "FMUL#2"
    type "operation"
    value "FMUL"
    idx 84
    output 0
  ]
  node [
    id 5
    label "N#0"
    type "ssavar"
    value "N#0"
    idx 82
    output 0
  ]
  node [
    id 6
    label "sin#0"
    type "operation"
    value "sin"
    idx 92
    output 0
  ]
  node [
    id 7
    label "cos#0"
    type "operation"
    value "cos"
    idx 87
    output 0
  ]
  edge [
    source 0
    target 4
    weight 2
    idx 82
    src_name "0"
    dst_name "FMUL#2"
  ]
  edge [
    source 1
    target 4
    weight 1
    idx 82
    src_name "6.283184"
    dst_name "FMUL#2"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 82
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 3
    target 4
    weight 1
    idx 82
    src_name "pow#0"
    dst_name "FMUL#2"
  ]
  edge [
    source 4
    target 6
    weight 1
    idx 84
    src_name "FMUL#2"
    dst_name "sin#0"
  ]
  edge [
    source 4
    target 7
    weight 1
    idx 84
    src_name "FMUL#2"
    dst_name "cos#0"
  ]
  edge [
    source 5
    target 3
    weight 1
    idx 82
    src_name "N#0"
    dst_name "pow#0"
  ]
]
