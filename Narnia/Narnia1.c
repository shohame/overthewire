#include <stdio.h>

int main(){
    int (*ret)();

    if(getenv("EGG")==NULL){
        printf("Give me something to execute at the env-variable EGG\n");
        exit(1);
    }

    printf("Trying to execute EGG!\n");
    ret = getenv("EGG");
    ret();

    return 0;
}


Dump of assembler code for function main:
   0x0804846b <+0>:     push   %ebp
   0x0804846c <+1>:     mov    %esp,%ebp
   0x0804846e <+3>:     sub    $0x4,%esp
   0x08048471 <+6>:     push   $0x8048540

   0x08048476 <+11>:    call   0x8048320 <getenv@plt>
   0x0804847b <+16>:    add    $0x4,%esp
   0x0804847e <+19>:    test   %eax,%eax
   0x08048480 <+21>:    jne    0x8048496 <main+43>     (jump 0x8048496 if eax not zero)
   0x08048482 <+23>:    push   $0x8048544
   0x08048487 <+28>:    call   0x8048330 <puts@plt>     (print "Give me something...")
   0x0804848c <+33>:    add    $0x4,%esp
   0x0804848f <+36>:    push   $0x1
   0x08048491 <+38>:    call   0x8048340 <exit@plt>    ( exit(1) )

   0x08048496 <+43>:    push   $0x8048579
   0x0804849b <+48>:    call   0x8048330 <puts@plt>    (print "Trying to execute EGG!")
   0x080484a0 <+53>:    add    $0x4,%esp
   0x080484a3 <+56>:    push   $0x8048540
   0x080484a8 <+61>:    call   0x8048320 <getenv@plt>
   0x080484ad <+66>:    add    $0x4,%esp
   0x080484b0 <+69>:    mov    %eax,-0x4(%ebp)
   0x080484b3 <+72>:    mov    -0x4(%ebp),%eax
   0x080484b6 <+75>:    call   *%eax                (call EGG)
   0x080484b8 <+77>:    mov    $0x0,%eax
   0x080484bd <+82>:    leave               ( pop    %ebp)
   0x080484be <+83>:    ret
