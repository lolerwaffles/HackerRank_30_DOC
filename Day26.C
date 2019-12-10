#include <stdio.h>

int main() {
    int OutDay;
    int OutMonth;
    int OutYear;
    int InDay;
    int InMonth;
    int InYear;
    int LateFee = 0;

    scanf("%d", &OutDay);
    scanf("%d", &OutMonth);
    scanf("%d", &OutYear);
    
    scanf("%d", &InDay);
    scanf("%d", &InMonth);
    scanf("%d", &InYear);

    if((OutYear - InYear) > 0){
        printf("10000");
    }else if((OutMonth - InMonth) > 1 && OutYear == InYear){
        printf("%d",(OutMonth - InMonth) * 500);
    }else if((OutDay - InDay) > 1 && OutMonth == InMonth && OutYear == InYear){
        printf("%d", (OutDay - InDay) * 15);
    }else{
        printf("0");
    }

    return 0;
}
