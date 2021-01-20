function! Raindrops(number) abort
  let new = ''
  let three = a:number % 3 == 0
  let five = a:number % 5 == 0
  let seven = a:number % 7 == 0
  if three
    let new .= 'Pling'
  endif
  if five
    let new .= 'Plang'
  endif
  if seven
    let new .= 'Plong'
  endif
  if !three && !five && !seven
    return '' . a:number
  endif
  return new
endfunction
