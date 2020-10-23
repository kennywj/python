;; block copy with endianness reversal equal to data beat size
;; MFIFO data buffer resource requirement: SR 0 DR 4
DMAMOV SAR 0xF0008000
DMAMOV DAR 0x10000000
DMAMOV CCR SB16 SS32 DB16 DS32 ES32
DMALP lc0 64
	DMALD
	DMAST
DMALPEND lc0
DMAEND
;; start DMA program instructuion
;; this command should be placed at end of program
DMAGO c0 0x1fff0000