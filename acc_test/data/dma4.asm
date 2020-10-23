;; gather operation - 8 bytes from the end of each 4K block
;; MFIFO data buffer resource requirement SR 0 DR 2
DMAMOV SAR 0xF0000000
DMAMOV DAR 0x10000000
DMAMOV CCR SB1 SS8 DB2 DS32
DMALP lc0 256
	DMAADDH SAR, 4064
	DMALP lc1 8
		DMALD
		DMAADDH SAR, 3
	DMALPEND lc1
	DMAST
DMALPEND lc0
DMAEND
;; start DMA program instructuion
;; this command should be placed at end of program
DMAGO c0 0x1fff0000
