graph [
  directed 1
  node [
    id 0
    label "arg_fx#0"
    type "ssavar"
    value "arg_fx#0"
    idx 66
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 61
    base "fx#3"
    base_width 16
    shift_width 16
  ]
  node [
    id 2
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 56
  ]
  node [
    id 3
    label "8"
    type "constant"
    value "8"
    idx 56
  ]
  node [
    id 4
    label "load#1"
    type "operation"
    value "load"
    idx 62
    base "fx#3"
    base_width 16
    shift_width 16
  ]
  node [
    id 5
    label "FMUL#3"
    type "operation"
    value "FMUL"
    idx 60
  ]
  node [
    id 6
    label "FMUL#4"
    type "operation"
    value "FMUL"
    idx 60
  ]
  node [
    id 7
    label "0.0"
    type "constant"
    value "0.0"
    idx 64
  ]
  node [
    id 8
    label "FADD#1"
    type "operation"
    value "FADD"
    idx 60
  ]
  node [
    id 9
    label "FMUL#5"
    type "operation"
    value "FMUL"
    idx 61
  ]
  node [
    id 10
    label "FNEG#0"
    type "operation"
    value "FNEG"
    idx 64
  ]
  node [
    id 11
    label "FMUL#6"
    type "operation"
    value "FMUL"
    idx 64
  ]
  node [
    id 12
    label "FADD#3"
    type "operation"
    value "FADD"
    idx 64
  ]
  node [
    id 13
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 66
  ]
  node [
    id 14
    label "16"
    type "constant"
    value "16"
    idx 76
  ]
  node [
    id 15
    label "arg_fu#0"
    type "ssavar"
    value "arg_fu#0"
    idx 76
  ]
  node [
    id 16
    label "ADD#4"
    type "operation"
    value "ADD"
    idx 76
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 56
    src_name "arg_fx#0"
    dst_name "ADD#0"
  ]
  edge [
    source 0
    target 13
    weight 1
    idx 66
    src_name "arg_fx#0"
    dst_name "ADD#2"
  ]
  edge [
    source 1
    target 5
    weight 1
    idx 57
    src_name "load#0"
    dst_name "FMUL#3"
  ]
  edge [
    source 1
    target 9
    weight 1
    idx 61
    src_name "load#0"
    dst_name "FMUL#5"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 56
    src_name "8"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 6
    weight 1
    idx 58
    src_name "load#1"
    dst_name "FMUL#4"
  ]
  edge [
    source 4
    target 11
    weight 1
    idx 62
    src_name "load#1"
    dst_name "FMUL#6"
  ]
  edge [
    source 5
    target 8
    weight 1
    idx 60
    src_name "FMUL#3"
    dst_name "FADD#1"
  ]
  edge [
    source 6
    target 8
    weight 1
    idx 60
    src_name "FMUL#4"
    dst_name "FADD#1"
  ]
  edge [
    source 7
    target 8
    weight 1
    idx 60
    src_name "0.0"
    dst_name "FADD#1"
  ]
  edge [
    source 7
    target 12
    weight 1
    idx 64
    src_name "0.0"
    dst_name "FADD#3"
  ]
  edge [
    source 9
    target 10
    weight 1
    idx 61
    src_name "FMUL#5"
    dst_name "FNEG#0"
  ]
  edge [
    source 10
    target 12
    weight 1
    idx 64
    src_name "FNEG#0"
    dst_name "FADD#3"
  ]
  edge [
    source 11
    target 12
    weight 1
    idx 64
    src_name "FMUL#6"
    dst_name "FADD#3"
  ]
  edge [
    source 14
    target 13
    weight 1
    idx 66
    src_name "16"
    dst_name "ADD#2"
  ]
  edge [
    source 14
    target 16
    weight 1
    idx 76
    src_name "16"
    dst_name "ADD#4"
  ]
  edge [
    source 15
    target 16
    weight 1
    idx 76
    src_name "arg_fu#0"
    dst_name "ADD#4"
  ]
]
