#include<stdio.h>
#define SIZE 6

int push();
int pop();
int display();

int choice,item,TOP=-1,Stack[SIZE];

int main()
{
    for(;;)
    {
        printf("\n\nEnter your choice: \n 1: PUSH\n 2: POP\n 3: DISPLAY\n 4: EXIT\n\n");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1: push();
                    break;
            case 2: pop();
                    break;
            case 3: display();
                    break;
            case 4: return 0;
                    break;
            default: printf("\nINVALID CHOICE\n");
                     break;
        }
    }
}

int push()
{
    printf("\nEnter the element to be pushed: ");
    scanf("%d", &item);

    if (TOP == SIZE-1)
    {
        printf("\nStack Overflow\n");
        return 0;
    }
    else
    {
        Stack[++TOP] = item;
        printf("\nThe element pushed is %d\n",item);
        return 0;
    }
}

int pop()
{
    if(TOP<=-1)
    {
        printf("\nStack Underflow\n");
        return 0;
    }
    else
    {
        item=Stack[TOP--];
        printf("\nThe element popped is %d\n",item);
        return 0;
    }
}

int display()
{
    printf("\nTOP is: %d\n",TOP);
    if(TOP==SIZE-1)
    {
        printf("\nStack Overflow\n");
        return 0;
    }
    else if(TOP<=-1)
    {
        printf("\nStack Underflow\n");
        return 0;
    }
    printf("\nPrinting elements after PUSH and POP: \n");
    for(int i=TOP;i>=0;i--)
    {
        printf("\n%d ",Stack[i]);
        return 0;
    }
}
