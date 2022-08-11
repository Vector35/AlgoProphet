graph [
  directed 1
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 18
    base "array#0"
    base_width 8
    shift_width 8
  ]
  node [
    id 6
    label "FADD#0"
    type "operation"
    value "FADD"
    idx 14
  ]
  edge [
    source 5
    target 6
    weight 1
    idx 18
    src_name "load#0"
    dst_name "FADD#0"
  ]
]
