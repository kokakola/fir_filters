//
// Description of "test_file_tb.v"
// Date: 15.01.2018 19:05:32
// Author: nikgv
//

`timescale 1ns / 1ns

module test_file_tb ();

reg tb_clk;
initial tb_clk = 0;
always
	#25 tb_clk = ~tb_clk;

real PI=3.14159265358979323846;
real last_time = 0;
real current_time = 0;
real angle = 0;
real frequency = 100;
integer freq_x100kHz = 0;
reg signed [15:0]sin16;

function real sin;
input x;
real x;
real x, y, y2, y3, y5, y7, sum, sign;
	begin
		sign = 1.0;
		x1 = x;
		if (x1<0)
		begin
			x1 = -x1;
			sign = -1.0;
		end
		while (x1 > PI/2.0)
		begin
			x1 = x1 - PI;
			sign = -1.0*sign;
		end
		y = x1*2/PI;
		y2 = y*y;
		y3 = y*y2;
		y5 = y3*y2;
		y7 = y5*y2;
		sum = 1.570794*y - 0.645962*y3 + 0.079692*y5 - 0.004681712*y7;
		sin = sign*sum;
	end
endfunction
