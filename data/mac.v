`timescale 1ns/1ps
module mac(
input clk, rst_n,
input [3:0] ina, inb, coef,
output reg [7:0] mac_out
);

reg [3:0] ina_reg, inb_reg, coef_reg;
reg [7:0] shift2_reg;
reg [7:0] mul_reg;
//reg [7:0] mac_out;

always @(posedge clk, negedge rst_n) begin
	if (!rst_n) begin
		ina_reg <= 0;
		inb_reg <= 0;
		coef_reg <= 0;
	end else begin
		ina_reg <= ina;
		inb_reg <= inb;
		coef_reg <= coef;
	end
end

always @(posedge clk, negedge rst_n) begin
	if (!rst_n) begin
		shift2_reg <= 0;
		mul_reg <= 0;
	end else begin
		shift2_reg <= coef_reg * 2; // multiplier 2
		mul_reg <= ina_reg * inb_reg;
	end
end

always @(posedge clk, negedge rst_n) begin
	if (!rst_n) begin
		mac_out <= 0;
	end else begin
		mac_out <= shift2_reg + mul_reg;
	end

end

endmodule
