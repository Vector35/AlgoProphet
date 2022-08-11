graph [
  directed 1
  node [
    id 0
    label "arg1#0"
    type "ssavar"
    value "arg1#0"
    idx 2
  ]
  node [
    id 1
    label "180.0"
    type "constant"
    value "180.0"
    idx 2
  ]
  node [
    id 2
    label "pow#0"
    type "operation"
    value "pow"
    idx 2
  ]
  node [
    id 3
    label "FMUL#1"
    type "operation"
    value "FMUL"
    idx 2
  ]
  node [
    id 4
    label "-1"
    type "constant"
    value "-1"
    idx 2
  ]
  node [
    id 5
    label "3.141592653589793"
    type "constant"
    value "3.141592653589793"
    idx 2
  ]
  edge [
    source 0
    target 3
    weight 1
    idx 2
    src_name "arg1#0"
    dst_name "FMUL#1"
  ]
  edge [
    source 1
    target 3
    weight 1
    idx 2
    src_name "180.0"
    dst_name "FMUL#1"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 2
    src_name "pow#0"
    dst_name "FMUL#1"
  ]
  edge [
    source 4
    target 2
    weight 1
    idx 2
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 5
    target 2
    weight 1
    idx 2
    src_name "3.141592653589793"
    dst_name "pow#0"
  ]
]
