;; example template for block copy, not a multiple of burst size
;; MFIFO data buffer resource requirement: SR 0 DR 16
DMAMOV SAR 0x10000000
DMAMOV DAR 0x20000000

;; start by copying 5 bursts of 16 * 8 bytes, total 0f 640 bytes
DMAMOV CCR SB16 SS64 DB16 DS64
DMALP lc0 5
   DMALD
   DMAST
DMALPEND lc0

;; now copy 1 burst of 7x8 bytes, 56+640 = 696
DMAMOV CCR SB7 SS64 DB7 DS64
DMALD
DMAST

;; now copy 1 burst of 3 x 1 bytes 3+696 = 699

DMAMOV CCR SB3 SS8 DB3 DS8
DMALD
DMAST

DMAEND

;; start DMA program instructuion
;; this command should be placed at end of program
DMAGO c0 0x1fff0000