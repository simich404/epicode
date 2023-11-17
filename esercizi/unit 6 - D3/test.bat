mov	edx, len   
mov	ecx, msg    
mov	ebx, 1	   
mov	eax, 4	   
int	0x80       
MOV AH,0x00
INT 0x16
mov	edx, len1
mov	ecx, msg1
mov	ebx, 1
mov	eax, 4
int	0x80
mov	eax, 1
int	0x80
msg	db	'primo numero:',0xa
msg1 db	'secondo numero:',0xa	;our dear string
len	equ	$ - msg
len1 equ $ - msg1;length of our dear string