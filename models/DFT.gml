graph [
  directed 1
  node [
    id 0
    label "FMUL#6"
    type "operation"
    value "FMUL"
    idx 64
    output 0
  ]
  node [
    id 1
    label "load#1"
    type "operation"
    value "load"
    idx 62
    base "fx#3"
    base_width 16
    shift_width 16
    output 0
  ]
  node [
    id 2
    label "load#0"
    type "operation"
    value "load"
    idx 61
    base "fx#3"
    base_width 16
    shift_width 16
    output 0
  ]
  node [
    id 3
    label "FMUL#3"
    type "operation"
    value "FMUL"
    idx 60
    output 0
  ]
  node [
    id 4
    label "FMUL#4"
    type "operation"
    value "FMUL"
    idx 60
    output 0
  ]
  node [
    id 5
    label "FADD#1"
    type "operation"
    value "FADD"
    idx 60
    output 1
  ]
  node [
    id 6
    label "FNEG#0"
    type "operation"
    value "FNEG"
    idx 64
    output 0
  ]
  node [
    id 7
    label "FADD#3"
    type "operation"
    value "FADD"
    idx 64
    output 1
  ]
  node [
    id 8
    label "FMUL#5"
    type "operation"
    value "FMUL"
    idx 61
    output 0
  ]
  edge [
    source 0
    target 7
    weight 1
    idx 64
    src_name "FMUL#6"
    dst_name "FADD#3"
  ]
  edge [
    source 1
    target 4
    weight 1
    idx 58
    src_name "load#1"
    dst_name "FMUL#4"
  ]
  edge [
    source 1
    target 0
    weight 1
    idx 62
    src_name "load#1"
    dst_name "FMUL#6"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 57
    src_name "load#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 2
    target 8
    weight 1
    idx 61
    src_name "load#0"
    dst_name "FMUL#5"
  ]
  edge [
    source 3
    target 5
    weight 1
    idx 60
    src_name "FMUL#3"
    dst_name "FADD#1"
  ]
  edge [
    source 4
    target 5
    weight 1
    idx 60
    src_name "FMUL#4"
    dst_name "FADD#1"
  ]
  edge [
    source 6
    target 7
    weight 1
    idx 64
    src_name "FNEG#0"
    dst_name "FADD#3"
  ]
  edge [
    source 8
    target 6
    weight 1
    idx 61
    src_name "FMUL#5"
    dst_name "FNEG#0"
  ]
]
