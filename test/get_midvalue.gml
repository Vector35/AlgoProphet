graph [
  directed 1
  node [
    id 0
    label "a#0"
    type "ssavar"
    value "a#0"
    idx 1
  ]
  node [
    id 1
    label "b#0"
    type "ssavar"
    value "b#0"
    idx 1
  ]
  node [
    id 2
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 2
  ]
  node [
    id 3
    label "ADD#0"
    type "operation"
    value "ADD"
    idx 1
  ]
  node [
    id 4
    label "LSR#0"
    type "operation"
    value "LSR"
    idx 1
  ]
  node [
    id 5
    label "31"
    type "constant"
    value "31"
    idx 1
  ]
  node [
    id 6
    label "ASR#0"
    type "operation"
    value "ASR"
    idx 2
  ]
  node [
    id 7
    label "1"
    type "constant"
    value "1"
    idx 2
  ]
  edge [
    source 0
    target 2
    weight 1
    idx 1
    src_name "a#0"
    dst_name "ADD#1"
  ]
  edge [
    source 1
    target 2
    weight 1
    idx 1
    src_name "b#0"
    dst_name "ADD#1"
  ]
  edge [
    source 2
    target 6
    weight 1
    idx 2
    src_name "ADD#1"
    dst_name "ASR#0"
  ]
  edge [
    source 3
    target 4
    weight 1
    idx 1
    src_name "ADD#0"
    dst_name "LSR#0"
  ]
  edge [
    source 4
    target 2
    weight 1
    idx 1
    src_name "LSR#0"
    dst_name "ADD#1"
  ]
  edge [
    source 5
    target 4
    weight 1
    idx 1
    src_name "31"
    dst_name "LSR#0"
  ]
  edge [
    source 7
    target 6
    weight 1
    idx 2
    src_name "1"
    dst_name "ASR#0"
  ]
]
