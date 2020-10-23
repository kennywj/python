
case 1: Do PA register devfault value check and do read/write test.

	$python3 pa_regs.py cluster.json <10.63.246.13> [log.txt] <enter> # cluster.json: test cluster registers, log.txt is a file name.
																	  # if log.txt exist, all output will write to this file.
	$python3 pa_regs.py pa.json <10.63.246.13> [log.txt] <enter> 	  # pa.json: test PA registers

	The format of register description in JSON file
		"pe_control":{				# name of register
		"offset":	"0x00000000",   # offset of registers from base address
		"type":		"rw",			# register type read only (ro), write only (wo) or read/write (rw)
		"enable":	true, 			# enable register test. if false, the registers do not test.
		"default":	"0x00040004",   # default value of register.
		"mask":		"0xff03ff03"},	# reserver bits, write only bits, enable operation or reset bits will set 1 to mask, other 0.

case 2: Do PA function test.

	$python3 pa_test.py data.json <10.63.246.13> <enter> # data.json: test case for PA function verify.

	The JSON file format
		"comments":"Kernel =3x3,16 channels, 32 Kernels,Image size=32x32,Stride=1,no Dilation,no Padding,no BN,no ReLu",
		"case1":{					# test case not
		"kernel":"3x3",				# kernel, 3x3 or 1x1
		"kernel_num":32,			# kernel number
		"channel_num":16,			# channel number
		"feature_map_high":32,		# image high (pixel)
		"feature_map_width":32,		# image width (pixel)
		"stride":1,					# stride number	1~4
		"padding":1,				# padding number 0~7
		"operation":"convlution",	# convlution,max_pool,average_pool,matrix_addition
		"de-quantized":false,		# enable de-quantized function
		"batch_normalization":false,# enable batch normalization function
		"relu":false,				# enable RELU function
		"relu6":false,				# enable RELU6 function 1:  RELU6 ( >6 => 6  , <0 => 0) 0: RELU  (  <0 => 0 )
		"yacc_output":false,		# enable YACC output
		"relu_output":true,			# enable RELU output
		"data":"data1.dat",			# input data file name
		"weight":"weight1.dat"},	# input weight file name

	To generate data file and weight file with fix pattern

	$python3 gendata.py data.json

case 3: mnist layer 1 test.
	
	$python3 pa_test.py mnist.json
		


