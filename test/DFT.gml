graph [
  directed 1
  node [
    id 0
    label "pow#0"
    type "operation"
    value "pow"
    idx 52
    output 0
  ]
  node [
    id 1
    label "ADD#3"
    type "operation"
    value "ADD"
    idx 75
    output 1
  ]
  node [
    id 2
    label "x0#3"
    type "operation"
    value "x0"
    idx 53
    output 0
  ]
  node [
    id 3
    label "__sincos#0"
    type "operation"
    value "__sincos"
    idx 53
    output 1
  ]
  node [
    id 4
    label "FMUL#2"
    type "operation"
    value "FMUL"
    idx 52
    output 1
  ]
  node [
    id 5
    label "1"
    type "constant"
    value "1"
    idx 75
    output 0
  ]
  node [
    id 6
    label "5.0"
    type "constant"
    value "5.0"
    idx 52
    output 0
  ]
  node [
    id 7
    label "v0#5"
    type "operation"
    value "v0"
    idx 53
    output 0
  ]
  node [
    id 8
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 65
    output 1
  ]
  node [
    id 9
    label "-1"
    type "constant"
    value "-1"
    idx 52
    output 0
  ]
  node [
    id 10
    label "6.2831852"
    type "constant"
    value "6.2831852"
    idx 52
    output 0
  ]
  node [
    id 11
    label "0"
    type "constant"
    value "0"
    idx 75
    output 0
  ]
  node [
    id 12
    label "x1#3"
    type "operation"
    value "x1"
    idx 53
    output 0
  ]
  edge [
    source 0
    target 4
    weight 1
    idx 52
    src_name "pow#0"
    dst_name "FMUL#2"
  ]
  edge [
    source 2
    target 3
    weight 1
    idx 53
    src_name "x0#3"
    dst_name "__sincos#0"
  ]
  edge [
    source 5
    target 8
    weight 1
    idx 65
    src_name "1"
    dst_name "ADD#1"
  ]
  edge [
    source 5
    target 1
    weight 1
    idx 75
    src_name "1"
    dst_name "ADD#3"
  ]
  edge [
    source 6
    target 0
    weight 1
    idx 52
    src_name "5.0"
    dst_name "pow#0"
  ]
  edge [
    source 7
    target 3
    weight 1
    idx 53
    src_name "v0#5"
    dst_name "__sincos#0"
  ]
  edge [
    source 9
    target 0
    weight 1
    idx 52
    src_name "-1"
    dst_name "pow#0"
  ]
  edge [
    source 10
    target 4
    weight 1
    idx 52
    src_name "6.2831852"
    dst_name "FMUL#2"
  ]
  edge [
    source 11
    target 4
    weight 2
    idx 52
    src_name "0"
    dst_name "FMUL#2"
  ]
  edge [
    source 11
    target 8
    weight 1
    idx 65
    src_name "0"
    dst_name "ADD#1"
  ]
  edge [
    source 11
    target 1
    weight 1
    idx 75
    src_name "0"
    dst_name "ADD#3"
  ]
  edge [
    source 12
    target 3
    weight 1
    idx 53
    src_name "x1#3"
    dst_name "__sincos#0"
  ]
]
