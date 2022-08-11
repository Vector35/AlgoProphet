graph [
  directed 1
  node [
    id 0
    label "arr#0"
    type "ssavar"
    value "arr#0"
    idx 10
  ]
  node [
    id 1
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 10
  ]
  node [
    id 2
    label "0"
    type "constant"
    value "0"
    idx 13
  ]
  node [
    id 3
    label "LSL#0"
    type "operation"
    value "LSL"
    idx 10
  ]
  node [
    id 4
    label "2"
    type "constant"
    value "2"
    idx 10
  ]
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
  node [
    id 8
    label "ADD#2"
    type "operation"
    value "ADD"
    idx 13
  ]
  node [
    id 9
    label "1"
    type "constant"
    value "1"
    idx 13
  ]
  edge [
    source 0
    target 1
    weight 1
    idx 10
    src_name "arr#0"
    dst_name "ADD#0"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 10
    src_name "0"
    dst_name "LSL#0"
  ]
  edge [
    source 2
    target 7
    weight 1
    idx 12
    src_name "0"
    dst_name "ADD#1"
  ]
  edge [
    source 2
    target 8
    weight 1
    idx 13
    src_name "0"
    dst_name "ADD#2"
  ]
  edge [
    source 3
    target 1
    weight 1
    idx 10
    src_name "LSL#0"
    dst_name "ADD#0"
  ]
  edge [
    source 4
    target 3
    weight 1
    idx 10
    src_name "2"
    dst_name "LSL#0"
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
  edge [
    source 9
    target 8
    weight 1
    idx 13
    src_name "1"
    dst_name "ADD#2"
  ]
]
