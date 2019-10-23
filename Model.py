import math

# Set of Joint Angles


# User Input
print("---Creating Player Profile---")
player_name = input('Name: ')
dominant_hand = input("Are you left (L) or right (R) handed? ")
if dominant_hand in ('R', 'r', 'right', 'Right'):
    shooting_arm = 'right'
else:
    shooting_arm = 'left'

print('What is your height?')
height_feet = int(float(input("Feet: ")))
total_height = int(12 * height_feet)
height_inches = int(float(input("Inches: ")))
total_height = int(total_height + height_inches)
print(f"{player_name} is {height_feet} feet {height_inches} inches tall")
print(f"Height in Inches: {total_height}")

print("\nPlease enter the following measurements in inches.")
upper_arm = float(input(f"Length of {shooting_arm} upper arm: "))
forearm = float(input(f"Length of {shooting_arm} forearm: "))
hand = float(input(f"Length of {shooting_arm} hand: "))


print(f"\n{player_name} has a {shooting_arm} upper shooting arm of {upper_arm} inches, forearm of {forearm} inches, "
      f"and hand length of {hand} inches.\n")

# Recommended Shooting Angle
if total_height < 60:
    recommended_angle = "56 (and up)"
elif 60 <= total_height <= 64:
    recommended_angle = "53 - 56"
elif 64 < total_height <= 68:
    recommended_angle = "52 - 55"
elif 68 < total_height <= 72:
    recommended_angle = "51 - 54"
elif 72 < total_height <= 76:
    recommended_angle = "50 - 53"
elif 76 < total_height <= 80:
    recommended_angle = "49 - 52"
elif 80 < total_height <= 84:
    recommended_angle = "48 - 51"
else:
    recommended_angle = "47 (and lower)"

print(f"For {player_name}, who is {int(height_feet)}'{int(height_inches)}\", a recommended range of 3PT line release "
      f"angles is {recommended_angle} degrees\n")

# Customize Settings
shooting_angle = float(input("Desired Shooting Angle: "))
print("Plotting your optimal shooting form release...")

# record the user data
with open('user_data.txt', 'w') as filehandle:
    filehandle.write('%s\n' % shooting_angle)
    filehandle.write('%s\n' % player_name)
    filehandle.write('%s' % dominant_hand)


# upper_arm = 9
# forearm = 8
# hand = 7

# Examples:
# 11, 9.5, 7.25

# Joint Angles Optimization

# Lists for X Coordinates
x_elbow = []
x_wrist = []
x_fingertip = []

# Lists for Y Coordinates
y_elbow = []
y_wrist = []
y_fingertip = []


# Release & Joint Angles
# shooting_angle = 48
# shoulder_angle = 20
# elbow_angle = 20
# wrist_angle = 20

# Angle Ranges

# Literature Range for Shoulder:
shoulder_min = 15
shoulder_max = 50

# Literature Range for Elbow:
elbow_min = shoulder_min + 1
elbow_max = 60

# Literature Range for Wrist:
wrist_min = 40
wrist_max = 89


shoulder_angle = shoulder_min

# Margin Sensitivity
margin_error = 0.01

# Change in angles
wrist_increment = 1
elbow_increment = 1
shoulder_increment = 1


while shoulder_angle <= shoulder_max:
    x_elbow_coord = upper_arm * math.cos(math.radians(shoulder_angle))
    y_elbow_coord = upper_arm * math.sin(math.radians(shoulder_angle))

    elbow_angle = elbow_min
    # print("changing angle")

    # loop for elbow_angle (0 - 85)
    while elbow_angle <= elbow_max:

        x_wrist_coord = x_elbow_coord + forearm * math.cos(math.radians(elbow_angle))
        y_wrist_coord = y_elbow_coord + forearm * math.sin(math.radians(elbow_angle))

        wrist_angle = wrist_min

        # loop for wrist_angle (0 - 130)
        while wrist_angle <= wrist_max:
            x_fingertip_coord = x_wrist_coord + hand * math.cos(math.radians(wrist_angle))
            y_fingertip_coord = y_wrist_coord + hand * math.sin(math.radians(wrist_angle))

            margin = math.degrees(math.atan(y_fingertip_coord/x_fingertip_coord))
            if (margin - margin_error <= shooting_angle) and (shooting_angle <= margin + margin_error):
                # Append X Coordinates
                x_elbow.append(x_elbow_coord)
                x_wrist.append(x_wrist_coord)
                x_fingertip.append(x_fingertip_coord)

                # Append Y Coordinates
                y_elbow.append(y_elbow_coord)
                y_wrist.append(y_wrist_coord)
                y_fingertip.append(y_fingertip_coord)

                # print("let's get this bread")
                # print(x_wrist_coord)
                # print(math.cos(math.radians(wrist_angle)))
                # print(x_fingertip_coord)
                # print(margin)

                # Figure out how to correctly iterate each angle joint by 0.5 degrees

            # Check if the shooting angle works for this set of joint angles
            wrist_angle += wrist_increment

        elbow_angle += elbow_increment

    shoulder_angle += shoulder_increment

# compute average of x and y coordinates of fingertip
x_sum = 0
for i in x_fingertip:
    x_sum += i
x_release = x_sum / len(x_fingertip)

y_sum = 0
for i in y_fingertip:
    y_sum += i
y_release = y_sum / len(y_fingertip)

print(f'The x release coord is: {x_release} and the y release coord is {y_release}')

with open('basketball_data.txt', 'w') as filehandle0:
    index = 0
    while index < len(x_elbow):
        filehandle0.write('%s ' % x_elbow[index])
        filehandle0.write('%s ' % y_elbow[index])
        filehandle0.write('%s ' % x_wrist[index])
        filehandle0.write('%s ' % y_wrist[index])
        filehandle0.write('%s ' % x_fingertip[index])
        filehandle0.write('%s' % y_fingertip[index])
        filehandle0.write('\n')
        index = index + 1

with open('y_elbow.txt', 'w') as filehandle1:
    for listitem in y_elbow:
        filehandle1.write('%s\n' % listitem)

with open('x_wrist.txt', 'w') as filehandle2:
    for listitem in x_wrist:
        filehandle2.write('%s\n' % listitem)

with open('y_wrist.txt', 'w') as filehandle3:
    for listitem in y_wrist:
        filehandle3.write('%s\n' % listitem)

with open('x_fingertip.txt', 'w') as filehandle4:
    for listitem in x_fingertip:
        filehandle4.write('%s\n' % listitem)

with open('y_fingertip.txt', 'w') as filehandle5:
    for listitem in y_fingertip:
        filehandle5.write('%s\n' % listitem)


# //Ball Release Properties

# Optimal Backspin is said to be 3Hz or about 3 full rotations during ball trajectory

# User Input
print("---Calculating Ball Radius and Distance of 3-Point Shot---")

print('Basketball Sizes: Size 7 (29.5"), Size 6 (28.5"), Size 5 (27.5"), Size 4 (26.5")')
ball_type = input("Please input basketball size---Size 7 (1), Size 6 (2), Size 5 (3), Size (4): ")
if ball_type == 1:
    ball_radius = 0.119  # roughly 4.695 inches
elif ball_type == 2:
    ball_radius = 0.1152  # roughly 4.536 inches
elif ball_type == 3:
    ball_radius = 0.1111  # roughly 4.377 inches
else:
    ball_radius = 0.1071  # roughly 4.218 inches

three_type = input('Corner 3? (Y/N): ')
if three_type in ('Y', 'y'):
    location = 'corner'
else:
    location = 'above-the-break'

competition_level = input("Please enter competition level---Professional (P), Collegiate (C), High School "
                          "or Lower (H): ")
if competition_level in ('P', 'p', 'Professional', 'professional'):
    classify = input("Please input the association---NBA (N), FIBA (F), or WNBA (W): ")
    if classify in ('N', 'n', 'NBA', 'nba'):
        classify = 'NBA'
        if three_type in ('Y', 'y', 'Yes', 'yes'):
            shot_distance = 6.7056
        else:
            shot_distance = 7.239
    else:
        if three_type in ('Y', 'y', 'Yes', 'yes'):
            shot_distance = 6.60
        else:
            shot_distance = 6.75
        if classify in ('F', 'f', 'FIBA', 'fiba'):
            classify = 'FIBA'
        else:
            classify = 'WNBA'

elif competition_level in ('C', 'c', 'Collegiate', 'collegiate'):
    division = input("Please input the division---I (1), II (2), III (3): ")
    classify = input("Please input the program---Men's (M), Women's (W): ")
    if classify in ('M', 'm'):
        classify = "NCAA Men's"
        if division in ('1', 'I', 'i'):
            if three_type in ('Y', 'y', 'Yes', 'yes'):
                shot_distance = 6.60
            else:
                shot_distance = 6.75
            division = ' Division I'
            classify = classify + division
        else:
            shot_distance = 6.3246
            if division in ('2', 'II', 'ii'):
                division = ' Division II'
                classify = classify + division

            else:
                division = ' Division III'
                classify = classify + division

    else:
        classify = "NCAA Women's"
        shot_distance = 6.3246
        if division in ('1', 'I', 'i'):
            division = ' Division I'
            classify = classify + division

        elif division in ('2', 'II', 'ii'):
            division = ' Division II'
            classify = classify + division

        else:
            division = ' Division III'
            classify = classify + division
else:
    shot_distance = 6.0198
    classify = 'High School or lower'
#
# # //Ball Properties
#
# # Backspin
backspin_rad = 2 * math.pi * (shot_distance + 2)/3
backspin_hz = backspin_rad * (1/(math.pi * 2))

shot_info = ("\n{a}'s {b} 3-point shot is {c:2.2f} feet from the hoop. An ideal backspin for this shot is {d:1.2} "
             "Hz.".format(a=classify, b=location, c=3.28084 * shot_distance, d=backspin_hz))
print(shot_info)

# Calculate the d_hypotenuse
d_hypotenuse = math.sqrt(x_release**2 + y_release**2)
d_hypotenuse = (d_hypotenuse/12)/3.2808
print(f'The hypotenuse is: {d_hypotenuse}')

# Calculating ltb and htb
jump_height = 0.1524  # roughly 6 inches

# Convert Height to Height in m
total_height = (total_height / 12) / 3.2808

shoulder_height = (21/25) * total_height
print(f'Shoulder height: {shoulder_height}')
htb = 3.048 - (shoulder_height + jump_height + d_hypotenuse*math.sin(math.radians(shooting_angle)) +
               ball_radius*math.sin(math.radians(shooting_angle)))
ltb = shot_distance - (d_hypotenuse*math.cos(math.radians(shooting_angle)) +
                       ball_radius*math.cos(math.radians(shooting_angle)))
print(f"The length to basket is l: {ltb} and the height to basket is h: {htb}")

gravity = 9.81

holder0 = math.tan(math.radians(shooting_angle)) - htb/ltb
holder1 = ((math.cos(math.radians(shooting_angle)))**2)*holder0
ball_velocity = math.sqrt((gravity*ltb)/(2*holder1))
print('\nThe ball velocity is: {a:2.2f} m/s'.format(a=ball_velocity))

# //Fingertip Components

# Acceleration
fingertip_acc_hor = ball_radius*(backspin_hz**2)*math.cos(math.radians(shooting_angle))
fingertip_acc_ver = ball_radius*(backspin_hz**2)
fingertip_acc = math.sqrt((fingertip_acc_hor**2) + (fingertip_acc_ver**2))
print('The x-direction fingertip acceleration is {a:2.2f} m/s^2\nThe y-direction fingertip acceleration is'
      ' {b:2.2f} m/s^2\nThe overall fingertip acceleration is {c:2.2f} m/s^2.\n'.format(a=fingertip_acc_hor,
                                                                                        b=fingertip_acc_ver,
                                                                                        c=fingertip_acc))

# Velocity
fingertip_vel_hor = ball_velocity*math.cos(math.radians(shooting_angle)) + \
                    ball_radius*backspin_hz*math.sin(math.radians(shooting_angle))
fingertip_vel_ver = ball_velocity*math.sin(math.radians(shooting_angle)) - \
                    ball_radius*math.cos(math.radians(shooting_angle))
fingertip_vel = math.sqrt((fingertip_vel_hor**2) + (fingertip_vel_ver**2))

angle = math.degrees(math.atan(fingertip_vel_ver/fingertip_vel_hor))
print('\nThe x-direction fingertip velocity is {a:2.2f} m/s\nThe y-direction fingertip velocity is '
      '{b:2.2f} m/s\nThe overall fingertip velocity is {c:2.2f} m/s.\n'.format(a=fingertip_vel_hor, b=fingertip_vel_ver,
                                                                               c=fingertip_vel))