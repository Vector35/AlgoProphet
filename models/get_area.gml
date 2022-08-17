graph [
  directed 1
  node [
    id 0
    label "rad#0"
    type "ssavar"
    value "rad#0"
    idx 0
  ]
  node [
    id 1
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 3
  ]
  node [
    id 2
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 3
  ]
  node [
    id 3
    label "3.141592653589793"
    type "constant"
    value "3.141592653589793"
    idx 3
  ]
  edge [
    source 0
    target 1
    weight 2
    idx 0
    src_name "rad#0"
    dst_name "MUL#0"
  ]
  edge [
    source 1
    target 2
    weight 1
    idx 3
    src_name "MUL#0"
    dst_name "FMUL#0"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 3
    src_name "3.141592653589793"
    dst_name "FMUL#0"
  ]
]
