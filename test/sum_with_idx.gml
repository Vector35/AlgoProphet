graph [
  directed 1
  node [
    id 0
    label "load#0"
    type "operation"
    value "load"
    idx 14
    base "x8#2"
    base_width 4
    shift_width 4
  ]
  node [
    id 1
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 14
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 14
    src_name "load#0"
    dst_name "ADD#1"
  ]
]
