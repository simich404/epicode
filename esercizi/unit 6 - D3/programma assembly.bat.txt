org  0x100
mov  dx, msg      ; the address of or message in dx
mov  ah, 9        ; ah=9 - "print string" sub-function
int  0x21         ; call dos services
    mov  dl, 0x0d     ; put CR into dl
    mov  ah, 2        ; ah=2 - "print character" sub-function
    int  0x21         ; call dos services
mov  dx, msg      ; the address of or message in dx
mov  ah, 9        ; ah=9 - "print string" sub-function
int  0x21         ; call dos services

mov  ah, 0x4c     ; "terminate program" sub-function
int  0x21         ; call dos services

aval  db 'valore di a: ', 0x0d, 0x0a, '$'   ; $-terminated message
bval  db 'valore di a: ', 0x0d, 0x0a, '$'   ; $-terminated message