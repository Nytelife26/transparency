let s:alphabet = split('abcdefghijklmnopqrstuvwxyz', '\zs')
let s:alatbash = split('zyxwvutsrqponmlkjihgfedcba', '\zs')

function! Swap(text, from, to, group) abort
  let text = split(substitute(tolower(a:text), '\v[^a-z0-9]', '', 'g'), '\zs')
  let new = ''
  if a:group
    let sc = 0
  endif
  for char in text
    if char =~ '[0-9]'
      let new .= char
    else
      let new .= a:to[index(a:from, char)]
    endif

    if a:group
      let sc += 1
      if sc % 5 == 0 && sc < len(text)
        let new .= ' '
      endif
    endif
  endfor
  return new
endfunction

function! AtbashDecode(cipher) abort
  return Swap(a:cipher, s:alatbash, s:alphabet, 0)
endfunction

function! AtbashEncode(plaintext) abort
  return Swap(a:plaintext, s:alphabet, s:alatbash, 1)
endfunction
