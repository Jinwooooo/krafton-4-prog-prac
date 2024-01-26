	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 2
	.globl	_foo                            ; -- Begin function foo
	.p2align	2
_foo:                                   ; @foo
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #80
	.cfi_def_cfa_offset 80
	stp	x29, x30, [sp, #64]             ; 16-byte Folded Spill
	add	x29, sp, #64
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	sub	x8, x29, #12
	str	x8, [sp, #32]                   ; 8-byte Folded Spill
	mov	w9, #10
	stur	w9, [x29, #-12]
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	stur	x0, [x29, #-24]                 ; 8-byte Folded Spill
	bl	_printf
	mov	x9, sp
	adrp	x8, l_.str.2@PAGE
	add	x8, x8, l_.str.2@PAGEOFF
	str	x8, [sp, #16]                   ; 8-byte Folded Spill
	str	x8, [x9]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	str	x0, [sp, #24]                   ; 8-byte Folded Spill
	bl	_printf
	ldur	x0, [x29, #-24]                 ; 8-byte Folded Reload
	ldur	x8, [x29, #-8]
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	ldur	x0, [x29, #-24]                 ; 8-byte Folded Reload
	ldur	x8, [x29, #-8]
	ldr	x8, [x8]
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [sp, #24]                   ; 8-byte Folded Reload
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [sp, #24]                   ; 8-byte Folded Reload
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	ldr	x8, [sp, #32]                   ; 8-byte Folded Reload
	ldur	x0, [x29, #-24]                 ; 8-byte Folded Reload
	ldur	x9, [x29, #-8]
	str	x8, [x9]
	ldur	x8, [x29, #-8]
	ldr	x8, [x8]
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	ldp	x29, x30, [sp, #64]             ; 16-byte Folded Reload
	add	sp, sp, #80
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	.cfi_def_cfa_offset 48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w8, #0
	str	w8, [sp, #12]                   ; 4-byte Folded Spill
	stur	wzr, [x29, #-4]
	sub	x8, x29, #8
	mov	w9, #4
	stur	w9, [x29, #-8]
	add	x0, sp, #16
	str	x8, [sp, #16]
	bl	_foo
	ldr	w0, [sp, #12]                   ; 4-byte Folded Reload
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%p\n"

l_.str.1:                               ; @.str.1
	.asciz	"%s\n"

l_.str.2:                               ; @.str.2
	.asciz	"---------------------"

.subsections_via_symbols
