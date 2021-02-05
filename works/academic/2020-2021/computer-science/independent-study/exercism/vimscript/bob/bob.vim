function! Response(remark) abort
  let remark = substitute(a:remark, '\v[ \n\t\r]', '', 'g')
  let upper = toupper(remark)
  let question = remark =~ '\v\?$'
  let capital = remark ==# upper
  let contains_capital = remark =~ '[A-Z]'
  if contains_capital && capital && question
    return 'Calm down, I know what I''m doing!'
  elseif contains_capital && capital
    return 'Whoa, chill out!'
  elseif question
    return 'Sure.'
  elseif tolower(remark) =~ '^$'
    return 'Fine. Be that way!'
  else
    return 'Whatever.'
  endif
endfunction
