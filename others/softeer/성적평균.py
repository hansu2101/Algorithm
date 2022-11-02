#
#
# # include<iostream>
# # include<cmath>
#
# using
# namespace
# std;
#
# int
# main(int
# argc, char ** argv)
# {
#     int
# n, k;
# int
# score[1000001];
#
# cin >> n >> k;
# for (int i=0;i < n;i++)
# {
#     int
# s;
# cin >> s;
# score[i] = s;
# }
#
# for (int i=0; i < k; i++){
#     int start, end;
# double sum=0;
# double answer;
# cin >> start >> end;
# for (int j=start-1; j <= end-1; j++){
# sum += score[j];
# }
# answer = sum / (end-start+1);
# answer=round(answer * 100) / 100;
# printf("%0.2f\n", answer);
# }
# return 0;
# }
#
