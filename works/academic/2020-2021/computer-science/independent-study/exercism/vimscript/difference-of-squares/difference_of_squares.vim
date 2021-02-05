function! DifferenceOfSquares(number) abort
  return SquareOfSum(a:number) - SumOfSquares(a:number)
endfunction

function! SquareOfSum(number) abort
  let pc = 1
  let sc = 0
  while pc <= a:number
    let sc += pc
    let pc += 1
  endwhile
  return sc * sc
endfunction

function! SumOfSquares(number) abort
  let pc = 1
  let sc = 0
  while pc <= a:number
    let sc += pc * pc
    let pc += 1
  endwhile
  return sc
endfunction
