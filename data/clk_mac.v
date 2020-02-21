/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Ultra(TM) in wire load mode
// Version   : K-2015.06-SP5
// Date      : Sat Jan 18 08:11:34 2020
/////////////////////////////////////////////////////////////


module clk_mac ( clk, rst_n, ina, inb, coef, mac_out );
  input [3:0] ina;
  input [3:0] inb;
  input [3:0] coef;
  output [7:0] mac_out;
  input clk, rst_n;
  wire   N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16,
         n2, n34, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47,
         n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61,
         n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75,
         n76, n77;
  wire   [3:0] ina_reg;
  wire   [3:0] inb_reg;
  wire   [3:0] coef_reg;
  wire   [4:0] shift2_reg;
  wire   [7:0] mul_reg;

  dffsr coef_reg_reg_3_ ( .d(coef[3]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        coef_reg[3]) );
  dffsr coef_reg_reg_2_ ( .d(coef[2]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        coef_reg[2]) );
  dffsr coef_reg_reg_1_ ( .d(coef[1]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        coef_reg[1]) );
  dffsr coef_reg_reg_0_ ( .d(coef[0]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        coef_reg[0]) );
  dffsr ina_reg_reg_3_ ( .d(ina[3]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        ina_reg[3]) );
  dffsr ina_reg_reg_2_ ( .d(ina[2]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        ina_reg[2]) );
  dffsr ina_reg_reg_1_ ( .d(ina[1]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        ina_reg[1]) );
  dffsr ina_reg_reg_0_ ( .d(ina[0]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        ina_reg[0]) );
  dffsr inb_reg_reg_3_ ( .d(inb[3]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        inb_reg[3]) );
  dffsr inb_reg_reg_2_ ( .d(inb[2]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        inb_reg[2]) );
  dffsr inb_reg_reg_1_ ( .d(inb[1]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        inb_reg[1]) );
  dffsr inb_reg_reg_0_ ( .d(inb[0]), .ck(clk), .sb(n34), .rb(rst_n), .q(
        inb_reg[0]) );
  dffsr mul_reg_reg_7_ ( .d(N8), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[7]) );
  dffsr mul_reg_reg_6_ ( .d(N7), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[6]) );
  dffsr mul_reg_reg_5_ ( .d(N6), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[5]) );
  dffsr mul_reg_reg_4_ ( .d(N5), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[4]) );
  dffsr mul_reg_reg_3_ ( .d(N4), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[3]) );
  dffsr mul_reg_reg_2_ ( .d(N3), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[2]) );
  dffsr mul_reg_reg_1_ ( .d(N2), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[1]) );
  dffsr mul_reg_reg_0_ ( .d(N1), .ck(clk), .sb(n34), .rb(rst_n), .q(mul_reg[0]) );
  dffsr shift2_reg_reg_4_ ( .d(coef_reg[3]), .ck(clk), .sb(n34), .rb(rst_n), 
        .q(shift2_reg[4]) );
  dffsr shift2_reg_reg_3_ ( .d(coef_reg[2]), .ck(clk), .sb(n34), .rb(rst_n), 
        .q(shift2_reg[3]) );
  dffsr shift2_reg_reg_2_ ( .d(coef_reg[1]), .ck(clk), .sb(n34), .rb(rst_n), 
        .q(shift2_reg[2]) );
  dffsr shift2_reg_reg_1_ ( .d(coef_reg[0]), .ck(clk), .sb(n34), .rb(rst_n), 
        .q(shift2_reg[1]) );
  dffsr mac_out_reg_7_ ( .d(N16), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[7]) );
  dffsr mac_out_reg_6_ ( .d(N15), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[6]) );
  dffsr mac_out_reg_5_ ( .d(N14), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[5]) );
  dffsr mac_out_reg_4_ ( .d(N13), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[4]) );
  dffsr mac_out_reg_3_ ( .d(N12), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[3]) );
  dffsr mac_out_reg_2_ ( .d(N11), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[2]) );
  dffsr mac_out_reg_1_ ( .d(N10), .ck(clk), .sb(n34), .rb(rst_n), .q(
        mac_out[1]) );
  dffsr mac_out_reg_0_ ( .d(N9), .ck(clk), .sb(n34), .rb(rst_n), .q(mac_out[0]) );
  dffsr shift2_reg_reg_0_ ( .d(n2), .ck(clk), .sb(n34), .rb(rst_n), .q(
        shift2_reg[0]) );
  logic_0 U38 ( .y(n2) );
  logic_1 U39 ( .y(n34) );
  and2 U40 ( .a(inb_reg[3]), .b(ina_reg[3]), .y(n56) );
  and2 U41 ( .a(inb_reg[2]), .b(ina_reg[2]), .y(n37) );
  and2 U42 ( .a(inb_reg[3]), .b(ina_reg[1]), .y(n36) );
  and2 U43 ( .a(n37), .b(n36), .y(n52) );
  and2 U44 ( .a(ina_reg[3]), .b(inb_reg[2]), .y(n50) );
  and2 U45 ( .a(inb_reg[3]), .b(ina_reg[2]), .y(n49) );
  fa U46 ( .a(n52), .b(n50), .ci(n49), .s(n59) );
  xor2 U47 ( .a(n37), .b(n36), .y(n40) );
  and2 U48 ( .a(inb_reg[3]), .b(ina_reg[0]), .y(n43) );
  and2 U49 ( .a(ina_reg[2]), .b(inb_reg[1]), .y(n42) );
  and2 U50 ( .a(n43), .b(n42), .y(n39) );
  and2 U51 ( .a(ina_reg[3]), .b(inb_reg[1]), .y(n38) );
  fa U52 ( .a(n40), .b(n39), .ci(n38), .co(n58), .s(n62) );
  and2 U53 ( .a(ina_reg[1]), .b(inb_reg[1]), .y(n45) );
  and2 U54 ( .a(inb_reg[2]), .b(ina_reg[0]), .y(n44) );
  and2 U55 ( .a(n45), .b(n44), .y(n48) );
  and2 U56 ( .a(inb_reg[2]), .b(ina_reg[1]), .y(n46) );
  and2 U57 ( .a(ina_reg[3]), .b(inb_reg[0]), .y(n47) );
  and2 U58 ( .a(n46), .b(n47), .y(n41) );
  or2 U59 ( .a(n48), .b(n41), .y(n61) );
  xor2 U60 ( .a(n43), .b(n42), .y(n65) );
  xor2 U61 ( .a(n45), .b(n44), .y(n68) );
  and2 U62 ( .a(inb_reg[1]), .b(ina_reg[0]), .y(n70) );
  and2 U63 ( .a(ina_reg[1]), .b(inb_reg[0]), .y(n69) );
  and2 U64 ( .a(n70), .b(n69), .y(n67) );
  and2 U65 ( .a(ina_reg[2]), .b(inb_reg[0]), .y(n66) );
  fa U66 ( .a(n48), .b(n47), .ci(n46), .s(n63) );
  and2 U67 ( .a(n50), .b(n49), .y(n51) );
  or2 U68 ( .a(n52), .b(n51), .y(n54) );
  or2 U69 ( .a(n55), .b(n54), .y(n53) );
  and2 U70 ( .a(n56), .b(n53), .y(N8) );
  fa U71 ( .a(n56), .b(n55), .ci(n54), .s(N7) );
  fa U72 ( .a(n59), .b(n58), .ci(n57), .co(n55), .s(N6) );
  fa U73 ( .a(n62), .b(n61), .ci(n60), .co(n57), .s(N5) );
  fa U74 ( .a(n65), .b(n64), .ci(n63), .co(n60), .s(N4) );
  fa U75 ( .a(n68), .b(n67), .ci(n66), .co(n64), .s(N3) );
  and2 U76 ( .a(ina_reg[0]), .b(inb_reg[0]), .y(N1) );
  xor2 U77 ( .a(n70), .b(n69), .y(N2) );
  and2 U78 ( .a(shift2_reg[0]), .b(mul_reg[0]), .y(n73) );
  fa U79 ( .a(mul_reg[3]), .b(shift2_reg[3]), .ci(n71), .co(n74), .s(N12) );
  fa U80 ( .a(mul_reg[2]), .b(shift2_reg[2]), .ci(n72), .co(n71), .s(N11) );
  fa U81 ( .a(mul_reg[1]), .b(shift2_reg[1]), .ci(n73), .co(n72), .s(N10) );
  xor2 U82 ( .a(shift2_reg[0]), .b(mul_reg[0]), .y(N9) );
  fa U83 ( .a(mul_reg[4]), .b(shift2_reg[4]), .ci(n74), .co(n75), .s(N13) );
  fa U84 ( .a(mul_reg[5]), .b(shift2_reg[0]), .ci(n75), .co(n76), .s(N14) );
  fa U85 ( .a(mul_reg[6]), .b(shift2_reg[0]), .ci(n76), .co(n77), .s(N15) );
  fa U86 ( .a(shift2_reg[0]), .b(mul_reg[7]), .ci(n77), .s(N16) );
endmodule

