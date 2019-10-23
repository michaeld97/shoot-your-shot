fid = fopen('basketball_data.txt');
fid2 = fopen('user_data.txt');

x_elbow = [];
y_elbow = [];

x_wrist = [];
y_wrist = [];

x_fingertip = [];
y_fingertip = [];

if fid2 == -1
    disp('File open not succesful')
else
      shooting_angle = fgetl(fid2);
      player_name = fgetl(fid2);
      dominant_hand = fgetl(fid2);
      % name's (hand) Release Optimization of Set of Joint Angles for a [angle] degree Release Angle
      title_string = strcat(player_name, "'s ", "Release Optimization of Joint Angles\nfor a ", shooting_angle, "° Release Angle");
      title_string = compose(title_string); 
end


if fid == -1
    disp('File open not successful')
else
    while feof(fid) == 0
        aline = fgetl(fid); % get the next line in the file
        C = strsplit(aline);
        
        % for each number on current line add to respective list
        % data format is as follows:
        % x_elbow y_elbow x_wrist y_wrist x_fingertip y_fingertip
        x_elbow = [x_elbow, str2double(C(1))];
        y_elbow = [y_elbow, str2double(C(2))];
        x_wrist = [x_wrist, str2double(C(3))];
        y_wrist = [y_wrist, str2double(C(4))];
        x_fingertip = [x_fingertip, str2double(C(5))];
        y_fingertip = [y_fingertip, str2double(C(6))];
        
    end
end

x_avg = [0, mean(x_elbow), mean(x_wrist), mean(x_fingertip)];
y_avg = [0, mean(y_elbow), mean(y_wrist), mean(y_fingertip)];

tempX = [];
tempY = [];
index = 1;

ball_radius = 4.75;
marg = sqrt((ball_radius^2)/2);
x_limit = marg + mean(x_fingertip) + 1;
y_limit = marg + mean(y_fingertip) + 1;


while index <= length(x_elbow)
        
    % for each data point (elbow, wrist and fingertip) format the data as
    % two vectors with x and y coordinates respectively. These will be used
    % to plot the current data set. Prepend the coordinate (0,0) to
    % represent the position of the shoulder
    tempX = [0, x_elbow(index), x_wrist(index), x_fingertip(index)];
    tempY = [0, y_elbow(index), y_wrist(index), y_fingertip(index)];
    
    % plot current data set and place a hold on the plot to overlay all 
    % data sets on the same graph
    plot(tempX,tempY,'color',[0.25, 0.25, 0.25],'linestyle',':','linewidth',.7)
    plot(x_avg, y_avg, 'color','r','linewidth',4)
    grid on
    t = title(title_string,'FontName', 'Bahnschrift');
    xlabel("Horizontal Displacement (inches)",'FontName', 'Bahnschrift');
    ylabel("Vertical Displacement (inches)", 'FontName', 'Bahnschrift');
    xlim([0 x_limit+1])
    ylim([-1 y_limit])
    hold on

    % update index of while loop
    index = index + 1;
end

ball_radius = 4.75;
circle2(mean(x_fingertip) + marg, mean(y_fingertip) + marg, ball_radius);
hold off

yline(0, '-.b'); 
yline(mean(y_elbow), '-.b');
yline(mean(y_wrist), '-.b');

% format bank
wrist_angle = atand(mean(y_fingertip) - mean(y_wrist)/(mean(x_fingertip) - mean(x_wrist)));
elbow_angle = atand((mean(y_wrist) - mean(y_elbow)/ (mean(x_wrist) - mean(x_elbow))));
shoulder_angle = atand(mean(y_elbow)/mean(x_elbow));

wrist_angle_text = append(num2str(wrist_angle,3),'°');
elbow_angle_text = append(num2str(elbow_angle,3),'°');
shoulder_angle_text = append(num2str(shoulder_angle,3),'°');


w_txt = text(16.5, mean(y_wrist) + 2, wrist_angle_text,'HorizontalAlignment', 'left');
e_txt = text(16.5, mean(y_elbow) + 2, elbow_angle_text, 'HorizontalAlignment', 'left');
s_txt = text(16.5, 2, shoulder_angle_text, 'HorizontalAlignment', 'left');

w_txt.FontName = 'Bahnschrift';
e_txt.FontName = 'Bahnschrift';
s_txt.FontName = 'Bahnschrift';
w_txt.FontWeight = 'bold';
e_txt.FontWeight = 'bold';
s_txt.FontWeight = 'bold';
w_txt.FontSize = 12;
e_txt.FontSize = 12;
s_txt.FontSize = 12;


d_hyp = distance(x_avg(4), 0, y_avg(4),0);
d_hyp = InchToMeter(d_hyp)



% h_below = 3.048 - (

function h = circle2(x,y,r)
d = r*2;
px = x-r;
py = y-r;
h = rectangle('Position',[px py d d],'Curvature',[1,1],'FaceColor',[0.8500, 0.3250, 0.0980],'EdgeColor',[0.8500, 0.3250, 0.0980]);
daspect([1,1,1])
end

function r = distance(x_one, x_two, y_one, y_two)
x_portion = (x_one - x_two)^2;
y_portion = (y_one - y_two)^2; 
r = sqrt(x_portion + y_portion);
end

function i = InchToMeter(inch_value)
i = (inch_value/12)/3.2808;
end