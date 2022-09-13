graph [
  directed 1
  node [
    id 0
    label "arr#0"
    type "ssavar"
    value "arr#0"
    idx 13
    output 0
  ]
  node [
    id 1
    label "load#0"
    type "operation"
    value "load"
    idx 14
    base "x8#2"
    base_width 4
    shift_width 4
    output 0
  ]
  node [
    id 2
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 14
    output 1
  ]
  node [
    id 3
    label "0"
    type "constant"
    value "0"
    idx 14
    output 0
  ]
  edge [
    source 1
    target 2
    weight 1
    idx 14
    src_name "load#0"
    dst_name "ADD#1"
  ]
  edge [
    source 3
    target 2
    weight 1
    idx 14
    src_name "0"
    dst_name "ADD#1"
  ]
]
