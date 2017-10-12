#include<stdio.h>
#include<math.h>
#include "graphics.h"

void drawFunc(int i);

int main(){
  //0 - sin, 1 - cos, 2 - tan
    drawFunc(0);
    drawFunc(1);
    drawFunc(2);
    return 0;
}

void drawFunc(int curve){
  double y = 0;
  for(double x = -6.28; x < 6.29; x+=0.01){
    switch(curve){
      case 0:
        y = sin(x);
        break;
      case 1:
        y = cos(x);
        break;
      default :
        y = tan(x);
    }
    int i = x*40;
    drawRect(250+i, 150+y*100, 1, 1);
  }

}
