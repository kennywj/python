;;simple block copy
;; MFIFO data buffer resource requirement SR 0 DR 16
DMAMOV SAR 0xF0008000 	;; start address
DMAMOV DAR 0x10000000 	;; end address
;; loop start
DMAMOV CCR SB4 SS64 DB4 DS64

DMALP lc0 256
	DMALD
	DMAST
	DMALD
	DMAST
	DMALD
	DMAST
	DMALD
	DMAST
DMALPEND lc0

DMAEND
;; start DMA program instructuion
;; this command should be placed at end of program
DMAGO c0 0x1fff0000