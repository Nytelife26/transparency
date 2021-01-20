function! Score(word) abort
  let cur = 0
  for char in split(tolower(a:word), '\zs')
    if char =~ '[aeioulnrst]'
      let cur += 1
    elseif char =~ '[dg]'
      let cur += 2
    elseif char =~ '[bcmp]'
      let cur += 3
    elseif char =~ '[fhvwy]'
      let cur += 4
    elseif char == 'k'
      let cur += 5
    elseif char =~ '[jx]'
      let cur += 8
    elseif char =~ '[qz]'
      let cur += 10
    endif
  endfor
  return cur
endfunction
