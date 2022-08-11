graph [
  directed 1
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 11
    base "arr#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 6
    label "MUL#0"
    type "operation"
    value "MUL"
    idx 12
  ]
  node [
    id 7
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 12
  ]
  edge [
    source 5
    target 6
    weight 2
    idx 11
    src_name "load#0"
    dst_name "MUL#0"
  ]
  edge [
    source 6
    target 7
    weight 1
    idx 12
    src_name "MUL#0"
    dst_name "ADD#1"
  ]
]
