//
// Description of "test_file.v"
// Date: 15.01.2018 19:05:32
// Author: nikgv
//

module test_file (
	clk,
	coefs,
	in,
	out
);

parameter IWIDTH = 16;
parameter CWIDTH = 16;
parameter TAPS = 2;
localparam MWIDTH = (IWIDTH+CWIDTH);
localparam RWIDTH = (MWIDTH+TAPS-1);

genvar i;
generate
	for(i=0; i<TAPS; i=i+1)
	begin:tap
		reg [IWIDTH-1:0] r=0;
		if(i==0)
		begin
			always @(posedge clk)
			r <= in;
		end
		else
		begin
			always @(posedge clk)
				tap[i].r <= tap[i-1].r;
		end

		wire [CWIDTH-1:0]c;
		assign c = coefs[((TAPS-1-i)*32+CWIDTH-1):(TAPS-1-i)*8];

		reg[MWIDTH-1:0]m;
		always @(posedge clk)
			m <= $signed(r) * $signed(c);

		reg [MWIDTH-1+i:0]a;
		if(i==0)
		begin
			always @*
				tap[i].a = $signed(tap[i].m);
		end		else
		begin
			always @*
				tap[i].a = $signed(tap[i].m) + $signed(tap[i-1].a);
		end
	end
endgenerate

reg [RWIDTH-1:0]result;
always @(posedge clk)
	result <= tap[TAPS-1].a;

assign out = result;

endmodule
