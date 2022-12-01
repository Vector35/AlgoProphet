graph [
  directed 1
  node [
    id 0
    label "FMUL#0"
    type "operation"
    value "FMUL"
    idx 2
    output 0
  ]
  node [
    id 1
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 4
    output 0
  ]
  node [
    id 2
    label "FMUL#1"
    type "operation"
    value "FMUL"
    idx 2
    output 0
  ]
  node [
    id 3
    label "FSQRT#0"
    type "operation"
    value "FSQRT"
    idx 4
    output 1
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 2
    src_name "FMUL#0"
    dst_name "FADD#0"
  ]
  edge [
    source 1
    target 3
    weight 1
    idx 4
    src_name "FADD#0"
    dst_name "FSQRT#0"
  ]
  edge [
    source 2
    target 1
    weight 1
    idx 2
    src_name "FMUL#1"
    dst_name "FADD#0"
  ]
]
