graph [
  directed 1
  node [
    id 0
    label "0"
    type "constant"
    value "0"
    idx 10
  ]
  node [
    id 1
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 9
  ]
  node [
    id 2
    label "arr#0"
    type "ssavar"
    value "arr#0"
    idx 9
  ]
  node [
    id 3
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 9
  ]
  node [
    id 4
    label "LSL#0"
    type "operation"
    value "LSL"
    idx 9
  ]
  node [
    id 5
    label "2"
    type "constant"
    value "2"
    idx 9
  ]
  node [
    id 6
    label "load#0"
    type "operation"
    value "load"
    idx 9
    base "arr#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 7
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 10
  ]
  node [
    id 8
    label "1"
    type "constant"
    value "1"
    idx 10
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 9
    src_name "0"
    dst_name "ADD#0"
  ]
  edge [
    source 0
    target 4
    weight 1
    idx 9
    src_name "0"
    dst_name "LSL#0"
  ]
  edge [
    source 0
    target 7
    weight 1
    idx 10
    src_name "0"
    dst_name "ADD#2"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 9
    src_name "arr#0"
    dst_name "ADD#1"
  ]
  edge [
    source 4
    target 3
    weight 1
    idx 9
    src_name "LSL#0"
    dst_name "ADD#1"
  ]
  edge [
    source 5
    target 4
    weight 1
    idx 9
    src_name "2"
    dst_name "LSL#0"
  ]
  edge [
    source 6
    target 1
    weight 1
    idx 9
    src_name "load#0"
    dst_name "ADD#0"
  ]
  edge [
    source 8
    target 7
    weight 1
    idx 10
    src_name "1"
    dst_name "ADD#2"
  ]
]
