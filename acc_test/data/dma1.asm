;;simple block copy
;; MFIFO data buffer resource requirement SR 0 DR 16
DMAMOV SAR 0x60000000 	;; start address
DMAMOV DAR 0x20210000 	;; end address
;; loop start
DMAMOV CCR SS256 SB16 SAI DS256 DB16 

DMALP lc0 256
	DMALD
	DMAST
DMALPEND lc0
DMAWMB
DMASEV e0
DMAEND
;; start DMA program instructuion
;; this command should be placed at end of program
DMAGO c0 0x63200000