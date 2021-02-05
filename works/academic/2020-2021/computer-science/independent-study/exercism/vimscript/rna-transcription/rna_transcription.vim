function! ToRna(strand) abort
  let strand = toupper(a:strand)
  if strand !~ '^[ACGT]*$'
    return ''
  endif
  let new = ''
  for char in split(strand, '\zs')
    if char == 'A'
      let new .= 'U'
    elseif char == 'C'
      let new .= 'G'
    elseif char == 'G'
      let new .= 'C'
    elseif char == 'T'
      let new .= 'A'
    endif
  endfor
  return new
endfunction
