graph [
  directed 1
  node [
    id 0
    label "-1"
    type "constant"
    value "-1"
    idx 20
    output 0
  ]
  node [
    id 1
    label "0"
    type "constant"
    value "0"
    idx 207
    output 0
  ]
  node [
    id 2
    label "6.283184"
    type "constant"
    value "6.283184"
    idx 231
    output 0
  ]
  node [
    id 3
    label "pow#0"
    type "operation"
    value "pow"
    idx 231
    output 0
  ]
  node [
    id 4
    label "FMUL#2"
    type "operation"
    value "FMUL"
    idx 233
    output 0
  ]
  node [
    id 5
    label "sin#0"
    type "operation"
    value "sin"
    idx 245
    output 0
  ]
  node [
    id 6
    label "cos#0"
    type "operation"
    value "cos"
    idx 236
    output 0
  ]
  edge [
    source 0
    target 3
    weight 1
    idx 231
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 1
    target 4
    weight 2
    idx 231
    src_name "0"
    dst_name "FMUL#2"
  ]
  edge [
    source 2
    target 4
    weight 1
    idx 231
    src_name "6.283184"
    dst_name "FMUL#2"
  ]
  edge [
    source 3
    target 4
    weight 1
    idx 231
    src_name "pow#0"
    dst_name "FMUL#2"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 233
    src_name "FMUL#2"
    dst_name "sin#0"
  ]
  edge [
    source 4
    target 6
    weight 1
    idx 233
    src_name "FMUL#2"
    dst_name "cos#0"
  ]
]
