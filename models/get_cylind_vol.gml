graph [
  directed 1
  node [
    id 0
    label "rad#0"
    type "ssavar"
    value "rad#0"
    idx 5
  ]
  node [
    id 1
    label "3.141592653589793"
    type "constant"
    value "3.141592653589793"
    idx 5
  ]
  node [
    id 2
    label "FMUL#2"
    type "operation"
    value "FMUL"
    idx 5
  ]
  node [
    id 3
    label "height#0"
    type "ssavar"
    value "height#0"
    idx 5
  ]
  edge [
    source 0
    target 2
    weight 2
    idx 5
    src_name "rad#0"
    dst_name "FMUL#2"
  ]
  edge [
    source 1
    target 2
    weight 1
    idx 5
    src_name "3.141592653589793"
    dst_name "FMUL#2"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 5
    src_name "height#0"
    dst_name "FMUL#2"
  ]
]
