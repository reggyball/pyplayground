 ; This program was retrieved from https://lindevs.com/install-nasm-on-ubuntu 
section .data 
hello: db 'Hello world', 0x0A ; Define a string with a newline character 
helloLen: equ $-hello         
; Calculate string length 
section .text 
global _start                 
_start: 
mov eax, 4                    
mov ebx, 1                    
mov ecx, hello                
mov edx, helloLen             
int 0x80                      
mov eax, 1                    
xor ebx, ebx                  
int 0x80   