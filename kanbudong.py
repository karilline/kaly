#include<stdio.h>
int main()
{
 float salary,tax=0;
 scanf("%f",&salary);
 if(salary-1000<=0)
 printf("收入为%f,应交税%f的，实际报酬为%f",salary,tax,salary-tax);
 else if(salary-1000>0&&salary-2000<=0)
 {
  tax=(salary-1000)*0.05;
  printf("收入为%f,应交税%f，实际报酬为%f",salary,tax,salary-tax);}
  else if(salary>2000&&salary<=4000)
  {
   tax=50+(salary-2000)*0.1;
   printf("收入为%f,应交税%f，实际报酬为%f",salary,tax,salary-tax);
  }
  else if(salary>4000&&salary<=6000){
   tax=50+200+(salary-4000)*0.15;
   printf("收入为%f,应交税%f，实际报酬为%f",salary,tax,salary-tax);
   }
   else if (salary>6000)
   {
    tax=50+200+300+(salary-6000)*0.2;
    printf("收入为%f,应交税%f，实际报酬为%f",salary,tax,salary-tax);
   }
 return 0;
}
