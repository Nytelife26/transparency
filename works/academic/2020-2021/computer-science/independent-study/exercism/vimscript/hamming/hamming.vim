function! Distance(strand1, strand2)
  if strlen(a:strand1) != strlen(a:strand2)
    throw 'left and right strands must be of equal length'
  endif
  let num = strlen(a:strand1)
  let prc = 0
  let dlt = 0
  while prc < num
    if a:strand1[prc] != a:strand2[prc]
      let dlt += 1
    endif
    let prc += 1
  endwhile
  return dlt
endfunction
