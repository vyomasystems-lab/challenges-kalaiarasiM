module fspeed(clk,reset,requested_speed,Up,Down,fspeed);

input clk,reset;
input [4:0] requested_speed;

output reg[1:0] Up;
output reg[1:0] Down;
//output reg[1:0] wait_floor;
output [4:0] fspeed;

reg [4:0] current_speed ;

always @ (posedge clk)
    begin
        if(reset)
        begin
            current_speed=4'd0;
            Up=1'd0;
            Down=1'd0;
        end
        else
        begin
            if(requested_speed < 4'd5)
            begin
                if(requested_speed < current_speed)
                begin
                    current_speed=current_speed-1;
                    Up=1'd0;
                    Down=1'd1;
                end
                else if (requested_speed > current_speed)
                begin
                    current_speed = current_speed+1;
                    Up=1'd1;
                    Down=1'd0;
                end
                else if(requested_speed == current_speed)
                begin
                    current_speed = requested_speed;
                    Up=1'd0;
                    Down=1'd0;
                end
            end
        end
    end
    
assign fspeed = current_speed;

endmodule