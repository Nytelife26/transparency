function! WordCount(phrase) abort
  let counts = {}
  let phrase = substitute(tolower(a:phrase), '\v ''([a-z0-9'']+)'' *', ' \1 ', 'g')
  let words = split(substitute(phrase, '[^a-z0-9'']', ' ', 'g'))
  for word in words
    let counts[word] = count(words, word)
    call filter(words, 'v:val != word')
  endfor
  return counts
endfunction
