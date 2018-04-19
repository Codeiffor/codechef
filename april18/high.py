t=int(input())
while(t>0):
    lanes,speed,width=[int(i)for i in input().split()]
    car_vel=[int(i)for i in input().split()]
    car_dir=[int(i)for i in input().split()]
    car_pos=[int(i)for i in input().split()]
    car_len=[int(i)for i in input().split()]
    time=0
    time_lane=width/speed
    for i in range(0,lanes):
        chef_pass=True
        car_dis_t=time*car_vel[i]
        car_dis=(time+time_lane)*car_vel[i]
        if(car_dir[i]==1):
            car_pos_f= car_pos[i] +car_dis
            car_pos_r= car_pos_f -car_len[i]
            car_pos_f_t= car_pos[i] +car_dis_t
            car_pos_r_t= car_pos_f_t -car_len[i]
            if(car_pos_r_t<0 and car_pos_f+0.000001>=0):
                chef_pass=False
            if(chef_pass==False):
                time+=(0-car_pos_r_t)/car_vel[i]
        else:
            car_pos_f= car_pos[i] -car_dis
            car_pos_r= car_pos_f +car_len[i]
            car_pos_f_t= car_pos[i] -car_dis_t
            car_pos_r_t= car_pos_f_t +car_len[i]
            if(car_pos_r_t>0 and car_pos_f-0.000001<=0):
                chef_pass=False
            if(chef_pass==False):
                time+=(car_pos_r_t)/car_vel[i]
        time+=time_lane
    print(round(time,6))
    t-=1
