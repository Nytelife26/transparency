function! LeapYear(year) abort
  if (a:year % 4) == 0
    if (a:year % 100) == 0
      if (a:year % 400) == 0
        return 1
      endif
      return 0
    endif
    return 1
  endif
  return 0
endfunction
