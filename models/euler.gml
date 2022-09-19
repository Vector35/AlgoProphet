graph [
  directed 1
  node [
    id 0
    label "6.2831852"
    type "constant"
    value "6.2831852"
    idx 52
    output 0
  ]
  node [
    id 1
    label "pow#0"
    type "operation"
    value "pow"
    idx 52
    output 0
  ]
  node [
    id 2
    label "FMUL#2"
    type "operation"
    value "FMUL"
    idx 53
    output 0
  ]
  node [
    id 3
    label "-1"
    type "constant"
    value "-1"
    idx 52
    output 0
  ]
  node [
    id 4
    label "sin#0"
    type "operation"
    value "sin"
    idx 61
    output 0
  ]
  node [
    id 5
    label "cos#0"
    type "operation"
    value "cos"
    idx 62
    output 0
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 52
    src_name "6.2831852"
    dst_name "FMUL#2"
  ]
  edge [
    source 1
    target 2
    weight 1
    idx 52
    src_name "pow#0"
    dst_name "FMUL#2"
  ]
  edge [
    source 2
    target 4
    weight 1
    idx 53
    src_name "FMUL#2"
    dst_name "sin#0"
  ]
  edge [
    source 2
    target 5
    weight 1
    idx 53
    src_name "FMUL#2"
    dst_name "cos#0"
  ]
  edge [
    source 3
    target 1
    weight 1
    idx 52
    src_name "-1"
    dst_name "pow#0"
  ]
]
