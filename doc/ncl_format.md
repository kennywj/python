
### NCL format 轉換範例 

case 1: 

	input ackin ; 

    INPUT(ackin)

case 2:

	input [3:0] f_coef ;

	INPUT(f_coef[3])
	INPUT(f_coef[2])
	INPUT(f_coef[1])
	INPUT(f_coef[0])

case 3:

	output ackout ;
	OUTPUT(ackout)

case 4:

	output [7:0] f_mac_out ;

	OUTPUT(f_mac_out[7])
	OUTPUT(f_mac_out[6])
	OUTPUT(f_mac_out[5])
	OUTPUT(f_mac_out[4])
	OUTPUT(f_mac_out[3])
	OUTPUT(f_mac_out[2])
	OUTPUT(f_mac_out[1])
	OUTPUT(f_mac_out[0])

case 5:

	th23  U52_U_U_2 (.a ( f_n38 ) , .b ( f_n40 ) , .c ( f_n39 ) , .y ( f_n58 ));

	f_n58=TH23(f_n38, f_n40, f_n39)

case 6:

	drlatr  shift2_reg_reg_2__0_U_0 (.rsb ( bufnet_0 ) , .ackout ( n1_N_9 ) , .ackin ( n2_N_9 ) , .f_d ( f_q1_N_9 ) , .t_d ( t_q1_N_9 ) , .f_q ( f_q2_N_9 ) , .t_q ( t_q2_N_9 ));
	
	(f_q2_N_9, t_q2_N_9)=DRLATR(f_q1_N_9, t_q1_N_9)

case 7:

	drlatr  ina_reg_reg_2__0_U_0 (.rsb ( bufnet_0 ) , .ackout ( n1_N_26 ) , .ackin ( n2_N_26 ) , .f_d ( f_q1_N_26 ) , .t_d ( t_q1_N_26 ) , .f_q ( f_q2_N_26 ) , .t_q ( t_q2_N_26 ));
	
	(f_q2_N_26, t_q2_N_26)=DRLATR(f_q1_N_26, t_q1_N_26)

case 8:

	and2  constcell0_0_U (.y ( f_constnet0 ) , .b ( acknet0 ) , .a ( bufnet_0 ));
	
	f_constnet0=AND2(acknet0, bufnet_0)

case 9:

	logic_0  constcell0_0_U_0 (.y ( t_constnet0 ));
	
	t_constnet0=LOGIC_0()

case 10:

	inv8x  bufcomp_0 (.a ( bufnet ) , .y ( bufnet_0 ));
	
	bufnet_0=INV8X(bufnet)

case 11:

	inv  bufcomp_2 (.y ( bufnet_2 ) , .a ( bufnet_1 ));
	
	bufnet_2=INV(bufnet_1)


搜尋路線需要忽略ack相關訊號與邏輯, 如下所示…

	INPUT(ackin)
	OUTPUT(ackout)
	acknet42=TH33(acknet41,acknet40,acknet39)
	acknet41=TH44(acknet26,acknet29,acknet32,acknet21)
	acknet40=TH44(acknet25,acknet28,acknet31,acknet23)
	acknet39=TH44(acknet24,acknet27,acknet30,acknet22)
	acknet38=TH22(acknet37,acknet36)
	acknet37=TH44(acknet7,acknet2,acknet5,acknet8)
	acknet36=TH44(acknet3,acknet6,acknet1,acknet4)
	acknet35=TH22(acknet34,acknet33)
	acknet34=TH44(acknet13,acknet20,acknet15,acknet18)
	acknet33=TH44(acknet16,acknet19,acknet14,acknet17)
	f_constnet0=AND2(acknet0,bufnet_0)
	bufnet_1=INV4X(ackin)
