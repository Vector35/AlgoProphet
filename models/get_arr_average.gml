graph [
  directed 1
  node [
    id 5
    label "load#0"
    type "operation"
    value "load"
    idx 15
    base "arr#0"
    base_width 4
    shift_width 4
  ]
  node [
    id 6
    label "ADD#1"
    type "operation"
    value "ADD"
    idx 9
  ]
  node [
    id 9
    label "DIVS#0"
    type "operation"
    value "DIVS"
    idx 9
  ]
  node [
    id 10
    label "size#0"
    type "ssavar"
    value "size#0"
    idx 9
  ]
  edge [
    source 5
    target 6
    weight 1
    idx 15
    src_name "load#0"
    dst_name "ADD#1"
  ]
  edge [
    source 6
    target 9
    weight 1
    idx 9
    src_name "ADD#1"
    dst_name "DIVS#0"
  ]
  edge [
    source 10
    target 9
    weight 1
    idx 9
    src_name "size#0"
    dst_name "DIVS#0"
  ]
]
