function! FindAnagrams(candidates, subject) abort
  let comparator = join(sort(split(tolower(a:subject), '\zs')), '')
  let valid = []
  for candidate in a:candidates
    if candidate ==? a:subject
      continue
    endif
    if join(sort(split(tolower(candidate), '\zs')), '') ==? comparator
      call add(valid, candidate)
    endif
  endfor
  return valid
endfunction
